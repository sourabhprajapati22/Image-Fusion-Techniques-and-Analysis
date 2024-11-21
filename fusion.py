import pywt
import numpy as np
from sklearn.decomposition import PCA
from PIL import Image
import cv2
import tifffile as tiff

def wavelet_transform(image, wavelet='haar'):
    # Perform wavelet decomposition
    coeffs = pywt.dwt2(image, wavelet)
    return coeffs

def inverse_wavelet_transform(coeffs, wavelet='haar'):
    # Perform wavelet reconstruction
    return pywt.idwt2(coeffs, wavelet)

def apply_pca(coeff1, coeff2):
    # Combine two coefficient sets using PCA
    coeffs = np.stack((coeff1.flatten(), coeff2.flatten()), axis=1)
    pca = PCA(n_components=1)
    fused_coeff = pca.fit_transform(coeffs).reshape(coeff1.shape)
    return fused_coeff

# Load TIF images using tifffile
image1 = tiff.imread("data/composite.tif")  # Multi-band image
image2 = tiff.imread("data/PATNA_SENTINEL1_image.tif")  # Grayscale image

# Select the first band of Image 1 (assuming it's multi-band)
if len(image1.shape) == 3:
    image1 = image1[0, :, :]  # First band
elif len(image1.shape) != 2:
    raise ValueError("Unsupported dimensions for image1")

# Resize Image 2 to match the dimensions of Image 1
image2_resized = cv2.resize(image2, (image1.shape[1], image1.shape[0]), interpolation=cv2.INTER_LINEAR)

# Normalize images to range [0, 255]
image1 = ((image1 - np.min(image1)) / (np.max(image1) - np.min(image1)) * 255).astype(np.uint8)
image2_resized = ((image2_resized - np.min(image2_resized)) / (np.max(image2_resized) - np.min(image2_resized)) * 255).astype(np.uint8)

print("Image1 Shape:", image1.shape)  # Shape of image1
print("Resized Image2 Shape:", image2_resized.shape)  # Shape of resized image2

# Wavelet decomposition
coeffs1 = wavelet_transform(image1)
coeffs2 = wavelet_transform(image2_resized)

# Apply PCA to each wavelet sub-band
fused_approx = apply_pca(coeffs1[0], coeffs2[0])
fused_h = apply_pca(coeffs1[1][0], coeffs2[1][0])
fused_v = apply_pca(coeffs1[1][1], coeffs2[1][1])
fused_d = apply_pca(coeffs1[1][2], coeffs2[1][2])

# Reconstruct fused image
fused_coeffs = (fused_approx, (fused_h, fused_v, fused_d))
fused_image = inverse_wavelet_transform(fused_coeffs)

# Normalize and save as JPEG
fused_image_normalized = cv2.normalize(fused_image, None, 0, 255, cv2.NORM_MINMAX)
fused_image_uint8 = fused_image_normalized.astype(np.uint8)
cv2.imwrite("fused_image.jpg", fused_image_uint8)
