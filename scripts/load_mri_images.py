import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

def load_mri_images(directory, probe):
    """
    Loads MRI images from a specified directory and converts them to numpy arrays.
    Supports two probes: 'p1' (3FDG) and 'p2' (3FDGal).

    📌 Filename Structure:
    - 'p1'  → 3FDG Probe
    - 'p2'  → 3FDGal Probe
    - 't1'  → 1 hour after injection
    - 't2'  → 2 hours after injection
    - 't3'  → 3 hours after injection
    - 'm1'  → First metabolite (Glucose/Galactose)
    - 'm3'  → Second metabolite (Gluconic Acid/Galactonic Acid)
    - 'm4'  → Third metabolite (Sorbitol/Galactitol)

    Parameters:
    - directory (str): The path where MRI images are stored.
    - probe (str): The probe type ('p1' for 3FDG, 'p2' for 3FDGal).

    Returns:
    - A dictionary containing image filenames as keys and numpy image arrays as values.
    """
    images = {}

    # Define filename patterns based on the probe type
    probe_prefix = "712" if probe == "p1" else "711"  # 712 → 3FDG, 711 → 3FDGal

    for file_name in os.listdir(directory):
        if file_name.startswith(probe_prefix) and file_name.endswith(".tif"):
            file_path = os.path.join(directory, file_name)
            img = Image.open(file_path)
            img_array = np.array(img)
            images[file_name] = img_array

    if not images:
        print(f"⚠ No images found for probe {probe.upper()} in {directory}!")

    return images

def format_title(file_name, probe):
    """
    Formats the filename into a user-friendly title with metabolite and time info.

    Parameters:
    - file_name (str): The original image filename.
    - probe (str): The probe type ('p1' for 3FDG, 'p2' for 3FDGal).

    Returns:
    - Formatted title for the image.
    """
    parts = file_name.replace(".tif", "").split("_")
    if len(parts) < 4:
        return file_name  # Return as is if format is unexpected

    # Define time mapping
    time_map = {"t1": "1 hr", "t2": "2 hrs", "t3": "3 hrs"}

    # Define metabolite mappings based on the probe
    metabolite_map = {
        "p1": {"m1": "3FDGlucose", "m3": "3FDGluconic Acid", "m4": "3FDSorbitol"},
        "p2": {"m1": "3FDGalactose", "m3": "3FDGalactonic Acid", "m4": "3FDGalactitol"}
    }

    # Extract time and metabolite name
    time = time_map.get(parts[2], parts[2])
    metabolite = metabolite_map[probe].get(parts[3], parts[3])

    return f"{metabolite} - {time}"

def display_images(images, probe):
    """
    Displays the MRI images in a well-formatted layout with clear titles.

    Parameters:
    - images (dict): Dictionary with filenames as keys and image arrays as values.
    - probe (str): The probe type ('p1' for 3FDG, 'p2' for 3FDGal).
    """
    num_images = len(images)
    if num_images == 0:
        print("⚠ No images to display.")
        return

    cols = min(3, num_images)
    rows = (num_images // cols) + (num_images % cols > 0)

    fig, axes = plt.subplots(rows, cols, figsize=(cols * 4, rows * 5), constrained_layout=True)
    axes = np.array(axes).reshape(-1)  # Flatten in case of multiple rows

    for ax, (file_name, img) in zip(axes, images.items()):
        ax.imshow(img, cmap="gray")
        ax.set_title(format_title(file_name, probe), fontsize=14, fontweight='bold', color="blue")
        ax.axis("off")

    # Hide unused subplots
    for ax in axes[len(images):]:
        ax.axis("off")

    plt.suptitle(f"MRI Images - {probe.upper()} Probe", fontsize=16, fontweight="bold", color="darkred")
    plt.show()

# ** Example Usage **
if __name__ == "__main__":
    # Change this path to the correct MRI images directory
    directory = r"../data/mri_images"

    # Choose probe ('p1' for 3FDG, 'p2' for 3FDGal)
    probe = "p2"

    # Load and display images
    images = load_mri_images(directory, probe)
    display_images(images, probe)

