# **MRI Metabolism Quantification Using 3FDG and 3FDGal**

## **Introduction**
This project introduces a Python-based tool to analyze and visualize real-time brain metabolism using MRI scans and fluorinated probes, **3FDG** and **3FDGal**. The tool aims to simplify the quantification of metabolite activity and provide researchers with valuable insights into metabolic dynamics.

---

## **Features**
1. **Input Handling**:
   - Supports TIF images:
     - Anatomical images (proton-based).
     - Metabolite-specific images (3FDG, 3FDGal).
   - Allows customizable parameters such as signal thresholds and regions of interest (ROI).

2. **Signal Analysis**:
   - Detects and quantifies metabolite signals using intensity thresholds.
   - Normalizes metabolite signals relative to anatomical images.

3. **Visualization**:
   - Time-series plots showing dynamic changes in metabolite activity.
   - Heatmaps highlighting active regions in the brain.

4. **Output**:
   - Exports results in CSV/Excel formats.
   - Saves visualizations as high-resolution images.

---

## **Technical Implementation**
- **Programming Language**: Python
- **Required Libraries**:
  - `numpy`, `pandas` for data analysis.
  - `pillow`, `scikit-image` for image processing.
  - `matplotlib`, `seaborn` for visualization.
  
---

## **Future Extensions**
1. Support for 3D MRI data (e.g., NIfTI format).
2. Integration of Signal-to-Noise Ratio (SNR) calculations.
3. Development of machine learning algorithms for ROI detection.

---

## **How to Use**
1. Clone the repository:
   ```bash
   git clone <repository_url>

