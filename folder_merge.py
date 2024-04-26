import os
import shutil

# Define the root directory where the 56 numbered folders are located
root_dir = "btube_classified"

# Define the name of the new Positive and Negative folders
positive_folder_name = "Positive_merged"
negative_folder_name = "Negative_merged"

# Define the path to the new Positive and Negative folders
positive_folder_path = os.path.join(root_dir, positive_folder_name)
negative_folder_path = os.path.join(root_dir, negative_folder_name)

# Create the new Positive and Negative folders
os.makedirs(positive_folder_path, exist_ok=True)
os.makedirs(negative_folder_path, exist_ok=True)

# Merge the Positive folders
for i in range(1, 57):
    positive_folder_path_i = os.path.join(root_dir, str(i), "Positive")
    if os.path.exists(positive_folder_path_i):
        for filename in os.listdir(positive_folder_path_i):
            new_filename = f"pos_{i}_{filename}"
            shutil.copy(os.path.join(positive_folder_path_i, filename), os.path.join(positive_folder_path, new_filename))

# Merge the Negative folders
for i in range(1, 57):
    negative_folder_path_i = os.path.join(root_dir, str(i), "Negative")
    if os.path.exists(negative_folder_path_i):
        for filename in os.listdir(negative_folder_path_i):
            new_filename = f"neg_{i}_{filename}"
            shutil.copy(os.path.join(negative_folder_path_i, filename), os.path.join(negative_folder_path, new_filename))

print("Files transferred and merged folders successfully...")