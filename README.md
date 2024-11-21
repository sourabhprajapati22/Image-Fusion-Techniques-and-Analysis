
# Image Fusion Techniques and Analysis

This repository contains the implementation and analysis of various image fusion techniques as part of the **CE6133: Data Science** course at **IIT Patna**. The project focuses on combining multiple images to produce a more informative fused image suitable for applications such as remote sensing, medical imaging, and surveillance.

---

## Table of Contents
- [Abstract](#abstract)
- [Techniques Implemented](#techniques-implemented)
- [Methodology](#methodology)
- [Results](#results)
- [Team Contributions](#team-contributions)

---

## Abstract
Image fusion combines multiple images from different sources into a single, more informative image. This project explores **spatial domain**, **transform domain**, and **hybrid techniques**, evaluated using metrics such as **PSNR** and **SSIM**. These techniques enhance visual quality while minimizing noise.

---

## Techniques Implemented

1. **Averaging**  
   Combines images by averaging pixel values.
   ![Averaging Technique](Fused Images\Average_fusion.png)

2. **Principal Component Analysis (PCA)**  
   Extracts significant features using PCA for fusion.
   ![PCA Technique](Fused Images\PCA.png)

3. **Wavelet Transform**  
   Uses wavelet coefficients to enhance image details.
   ![Wavelet Transform](Fused Images\wavelet_pca.jpg)

4. **Weighted Averaging**  
   Assigns weights to images for custom fusion.
   ![Weighted Averaging](Fused Images\Waited Average.png)

5. **Wavelet Fusion**  
   Combines images using wavelet decomposition and reconstruction.
   ![Wavelet Fusion](Fused Images\wavelet_pca.jpg)

6. **Band Fusion**  
   Integrates spectral bands for detailed analysis.
   ![Band Fusion](Fused Images\band fusion.png)

---

## Methodology

1. **Data Collection**  
   Images from diverse sources were pre-processed for uniformity.

2. **Image Registration**  
   Aligned images using feature-based techniques to ensure pixel-level accuracy.

3. **Fusion Techniques**  
   Applied multiple methods, combining spatial and transform domain approaches.

4. **Evaluation Metrics**  
   - **PSNR**: Measures fused image quality.
   - **SSIM**: Evaluates similarity with input images.

---

## Results
- **Enhanced Image Quality**: Significant improvement in clarity and detail.  
- **Metrics**: Quantitative evaluation confirmed the superiority of the fused images.  

![Results](path_to_results_image.png)

---

## Team Contributions

| Name                       | Contribution                         |
|----------------------------|--------------------------------------|
| Rohit Raju Kamble          | Fusing with Averaging                |
| Prianshu Prasad            | Wavelet Transform, Research          |
| Sourabh Kumar Prajapati    | Band Fusion                          |
| Shilpi Mukherjee           | Wavelet Transformation with PCA      |
| Aditi Thakur               | PCA Fusion                           |
|Udit Narayan Fusing with    |weighted Averaging and Team Management|
|Lalit Kumar Bharti          |Report                                |
|Pankaj Kumar Paswan         |Plagiarism Report                     |
|Shilpi Mukherjee            |Wavelet Transformation with PCA       |
|Ravi Kumar Paswan           |wavelet transform                     |
|Anu Kumar Tiwary            |   Report                             |
|Aashish Kumar Gupta         |Wavelet Fusion                        |
|Sonam Raj                   |Report                                |
|Ratna Priya                 |Report                                |
|Uttam Kumar                 |Report                                |
|Aditi Thakur                |PCA Fusion                            |
|Pinky Kumari                |Plagiarism Report                     |
|Amisha Kumari               |Report                                |
|Saloni Kumari               |Report                                |

---

## References
- Gonzalez, R. C., & Woods, R. E., *Digital Image Processing*.
- Mallat, S., *A Wavelet Tour of Signal Processing*.
- [Other references](#).

---
