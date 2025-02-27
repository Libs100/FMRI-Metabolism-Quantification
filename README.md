# 🧬 **F-MRI Metabolism Quantification Using 3FDG and 3FDGal**  
### 🔬 **Automated Metabolic Imaging Analysis using MRI**  
## **Introduction**
Brain metabolism plays a pivotal role in understanding neurological processes, including normal function and disease states. This project aims to develop a Python-based analytical tool to quantify and visualize real-time metabolic changes in the brain using MRI data and fluorinated probes, **3FDG** and **3FDGal**.

The tool will focus on automating data analysis and providing researchers with intuitive visualizations of metabolite activity, enabling in-depth insights into biochemical dynamics over time.

---

## **Features**
1. **Image Analysis**:
   - Supports TIF image files for:
     - **Anatomical data** (proton-based images).
     - **Metabolite-specific data** (e.g., 3FDG and 3FDGal signals).

2. **Signal Quantification**:
   - Automatically identifies and quantifies metabolite-specific signals.
   - Focuses on key regions of interest (ROIs) defined by users.

3. **Visualization**:
   - Time-series plots to show changes in metabolite activity over time.
   - Heatmaps to highlight active regions in the brain.

4. **Output**:
   - Generates clear visualizations for presentations or publications.
   - Exports quantified data in CSV or Excel formats for further analysis.

---

## **Future Extensions**
1. **Enhanced Input Formats**:
   - Support for 3D MRI data, such as NIfTI files, to enable broader compatibility.

2. **Signal-to-Noise Ratio (SNR)**:
   - Incorporate SNR calculations to filter and quantify high-quality signals more accurately.

3. **Automated ROI Detection**:
   - Develop machine learning models to identify regions of interest (ROIs) automatically.

4. **Integration of Clinical Data**:
   - Extend functionality to compare brain metabolism under different conditions (e.g., healthy vs. pathological states).

---
## 🎯 How to Use the Tool  

### 🛠 Step 1: Download & Set Up  

🔹 **1. Clone or Download the Repository**  

Run in the terminal (Git Bash or Anaconda Prompt):  
git clone https://github.com/Libs100/FMRI-Metabolism-Quantification.git
cd FMRI-Metabolism-Quantification

Alternatively, download the ZIP file, extract it, and place it in a directory of your choice.


🔹 **2. open Jupyter Notebook**
Then, open scripts/the script you want to run.ipynb inside Jupyter


---


### 🛠 **Step 2: Configure Your Settings** 
Before running the script, update the following variables inside Jupyter Notebook

🔹 **1. Set Your Image Directory (Update Path)**
directory = r"YOUR_LOCAL_PATH_HERE/example_images_3FDGal"  # 🔄 Change this to match your folder location

🔹 **2. Choose Your Probe Type**
probe = "p2"  # Select "p1" for 3FDG or "p2" for 3FDGal

🔹 **3. Define Output Directory**
output_directory = r"YOUR_LOCAL_PATH_HERE/output_images"

🔍 Make sure you use the correct folder for 3FDG or 3FDGal images.

---


📊 Step 3: Run the Analysis

🔹 Execution Order:

1️⃣ load_and_display_mri.ipynb – Loads and visualizes raw MRI images for the selected probe.

2️⃣ compute_snr_analysis.ipynb – Computes and displays SNR values for each image.

3️⃣ save_snr_to_excel.ipynb – Saves the computed SNR values into an organized Excel file.

4️⃣ load_and_display_colormaps.ipynb – Loads and displays colormap images for visualization.

5️⃣ apply_colormap_snr.ipynb – Applies external colormaps to highlight metabolite signals.

6️⃣ merge_mri_with_signal.ipynb – Overlays the processed signal maps onto anatomical MRI images.

7️⃣ plot_snr_time_series.ipynb – Generates a time-series plot of SNR changes over time.

🚀 Follow this order to ensure smooth data processing and visualization!

✅ Final Output Example:
After running the script, your results will be automatically saved in output_images/.

🔹 MRI Image Processing Output

---

## **Conclusion**
This project lays the foundation for an innovative tool to quantify and analyze brain metabolism in real time using **3FDG** and **3FDGal** probes. By automating data processing and visualization, the tool will provide researchers with an efficient, user-friendly solution for metabolic research, paving the way for future studies in neuroscience.


---

## **📧 Contact & Support**
📩 For questions or collaboration, contact:
libi.saad@weizmann.ac.il

---

