
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
   ![Averaging Technique](Fused%20Images/Average_fusion.png)

2. **Principal Component Analysis (PCA)**  
   Extracts significant features using PCA for fusion.
   ![PCA Technique](Fused%20Images/PCA.png)

3. **Wavelet Transform**  
   Uses wavelet coefficients to enhance image details.
   ![Wavelet Transform](Fused%20Images/wavelet_pca.jpg)

4. **Weighted Averaging**  
   Assigns weights to images for custom fusion.
   ![Weighted Averaging](Fused%20Images/Waited%20Average.png)

5. **Wavelet Fusion**  
   Combines images using wavelet decomposition and reconstruction.
   ![Wavelet Fusion](Fused%20Images/wavelet_pca.jpg)

6. **Band Fusion**  
   Integrates spectral bands for detailed analysis.
   ![Band Fusion](Fused%20Images/band%20fusion.png)

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
 1. Gonzalez, R. C., & Woods, R. E. (2018). Digital Image Processing (4th ed.).
 Pearson.
 ○ Referenced for foundational concepts in image fusion methodologies,
 including spatial and transform domains.
 2. Mallat, S. (2008). A Wavelet Tour of Signal Processing: The Sparse Way (3rd
 ed.). Academic Press.
 ○ Utilized for understanding wavelet-based fusion techniques and
 multi-resolution analysis.
 3. Kaur, P., & Goyal, D. (2015). "An overview of image fusion methods."
 International Journal of Advanced Research in Computer and Communication
 Engineering, 4(2), 223–227.
 ○ Usedfor acomparative understanding of common fusion techniques
 such as PCA and weighted averaging.
 4. Li, S., Kwok, J. T., & Wang, Y. (2002). "Using the discrete wavelet frame
 transform to merge Landsat TM and SPOT panchromatic images." Information
 Fusion, 3(1), 17–23.
 ○ Basis for the integration of wavelet-based and PCA fusion
 methodologies.

---
