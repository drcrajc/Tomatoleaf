import os
import random
import shutil
import uuid

# Define the source folders
train_positive_folder = 'Ds_bchip/pyprojcodes/Dataset/Train/Positive'
train_negative_folder = 'Ds_bchip/pyprojcodes/Dataset/Train/Negative'
validation_positive_folder = 'Ds_bchip/pyprojcodes/Dataset/Validation/Positive'
validation_negative_folder = 'Ds_bchip/pyprojcodes/Dataset/Validation/Negative'
test_positive_folder = 'Ds_bchip/pyprojcodes/Dataset/Test/Positive'
test_negative_folder = 'Ds_bchip/pyprojcodes/Dataset/Test/Negative'

# Define the destination folders
train_folder = 'Ds_bchip/pyprojcodes/Dataset/Train'
validation_folder = 'Ds_bchip/pyprojcodes/Dataset/Validation'
test_folder = 'Ds_bchip/pyprojcodes/Dataset/Test'

# Define the number of images to transfer
total_images = 15129
validation_images = 1892
test_images = 1892

# Calculate the proportions for each class
train_positive_images = min(int(total_images * 0.8), 8015)
train_negative_images = total_images - train_positive_images
validation_positive_images = min(int(validation_images * 0.5), 908)
validation_negative_images = validation_images - validation_positive_images
test_positive_images = min(int(test_images * 0.5), 1004)
test_negative_images = test_images - test_positive_images

# Transfer train images
train_positive_files = os.listdir(train_positive_folder)
if len(train_positive_files) < train_positive_images:
    print(f"Warning: Not enough positive images in the train folder. Available: {len(train_positive_files)}")
train_negative_files = os.listdir(train_negative_folder)
if len(train_negative_files) < train_negative_images:
    print(f"Warning: Not enough negative images in the train folder. Available: {len(train_negative_files)}")

for filename in random.sample(train_positive_files, min(train_positive_images, len(train_positive_files))):
    source = os.path.join(train_positive_folder, filename)
    unique_filename = str(uuid.uuid4()) + os.path.splitext(filename)[-1]  # Generate a unique filename
    destination = os.path.join(train_folder, 'Positive', unique_filename)
    shutil.copy(source, destination)

for filename in random.sample(train_negative_files, min(train_negative_images, len(train_negative_files))):
    source = os.path.join(train_negative_folder, filename)
    unique_filename = str(uuid.uuid4()) + os.path.splitext(filename)[-1]  # Generate a unique filename
    destination = os.path.join(train_folder, 'Negative', unique_filename)
    shutil.copy(source, destination)

print('Transferred train images successfully')

# Transfer validation images
validation_positive_files = os.listdir(validation_positive_folder)
if len(validation_positive_files) < validation_positive_images:
    print(f"Warning: Not enough positive images in the validation folder. Available: {len(validation_positive_files)}")
validation_negative_files = os.listdir(validation_negative_folder)
if len(validation_negative_files) < validation_negative_images:
    print(f"Warning: Not enough negative images in the validation folder. Available: {len(validation_negative_files)}")

for filename in random.sample(validation_positive_files, min(validation_positive_images, len(validation_positive_files))):
    source = os.path.join(validation_positive_folder, filename)
    unique_filename = str(uuid.uuid4()) + os.path.splitext(filename)[-1]  # Generate a unique filename
    destination = os.path.join(validation_folder, 'Positive', unique_filename)
    shutil.copy(source, destination)

for filename in random.sample(validation_negative_files, min(validation_negative_images, len(validation_negative_files))):
    source = os.path.join(validation_negative_folder, filename)
    unique_filename = str(uuid.uuid4()) + os.path.splitext(filename)[-1]  # Generate a unique filename
    destination = os.path.join(validation_folder, 'Negative', unique_filename)
    shutil.copy(source, destination)

print('Transferred validation images successfully')

# Transfer test images
test_positive_files = os.listdir(test_positive_folder)
if len(test_positive_files) < test_positive_images:
    print(f"Warning: Not enough positive images in the test folder. Available: {len(test_positive_files)}")
test_negative_files = os.listdir(test_negative_folder)
if len(test_negative_files) < test_negative_images:
    print(f"Warning: Not enough negative images in the test folder. Available: {len(test_negative_files)}")

for filename in random.sample(test_positive_files, min(test_positive_images, len(test_positive_files))):
    source = os.path.join(test_positive_folder, filename)
    unique_filename = str(uuid.uuid4()) + os.path.splitext(filename)[-1]  # Generate a unique filename
    destination = os.path.join(test_folder, 'Positive', unique_filename)
    shutil.copy(source, destination)

for filename in random.sample(test_negative_files, min(test_negative_images, len(test_negative_files))):
    source = os.path.join(test_negative_folder, filename)
    unique_filename = str(uuid.uuid4()) + os.path.splitext(filename)[-1]  # Generate a unique filename
    destination = os.path.join(test_folder, 'Negative', unique_filename)
    shutil.copy(source, destination)

print('Transferred test images successfully')
