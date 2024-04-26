import os
import random
import shutil

# Define the source and destination folders
source_train_negative = 'Ds_bchip/pyprojcodes/Dataset/Train/Negative'
source_train_positive = 'Ds_bchip/pyprojcodes/Dataset/Train/Positive'
source_test_negative = 'Ds_bchip/pyprojcodes/Dataset/Test/Negative'
source_test_positive = 'Ds_bchip/pyprojcodes/Dataset/Test/Positive'
source_validation_negative = 'Ds_bchip/pyprojcodes/Dataset/Validation/Negative'
source_validation_positive = 'Ds_bchip/pyprojcodes/Dataset/Validation/Positive'

destination_train_negative = 'Ds_bchip/pyprojcodes/new_ds/Train/Negative'
destination_train_positive = 'Ds_bchip/pyprojcodes/new_ds/Train/Positive'
destination_test_negative = 'Ds_bchip/pyprojcodes/new_ds/Test/Negative'
destination_test_positive = 'Ds_bchip/pyprojcodes/new_ds/Test/Positive'
destination_validation_negative = 'Ds_bchip/pyprojcodes/new_ds/Validation/Negative'
destination_validation_positive = 'Ds_bchip/pyprojcodes/new_ds/Validation/Positive'

# Define the number of images to transfer
train_images_total = 16000
test_images_total = 2000
validation_images_total = 2000

# Create the destination folders if they don't exist
os.makedirs(destination_train_negative, exist_ok=True)
os.makedirs(destination_train_positive, exist_ok=True)
os.makedirs(destination_test_negative, exist_ok=True)
os.makedirs(destination_test_positive, exist_ok=True)
os.makedirs(destination_validation_negative, exist_ok=True)
os.makedirs(destination_validation_positive, exist_ok=True)

# Get the list of image files in the source folders
train_negative_images = [file for file in os.listdir(source_train_negative) if file.endswith('.jpg')]
train_positive_images = [file for file in os.listdir(source_train_positive) if file.endswith('.jpg')]
test_negative_images = [file for file in os.listdir(source_test_negative) if file.endswith('.jpg')]
test_positive_images = [file for file in os.listdir(source_test_positive) if file.endswith('.jpg')]
validation_negative_images = [file for file in os.listdir(source_validation_negative) if file.endswith('.jpg')]
validation_positive_images = [file for file in os.listdir(source_validation_positive) if file.endswith('.jpg')]

# Shuffle the image files randomly
random.shuffle(train_negative_images)
random.shuffle(train_positive_images)
random.shuffle(test_negative_images)
random.shuffle(test_positive_images)
random.shuffle(validation_negative_images)
random.shuffle(validation_positive_images)

# Transfer images to the train folders and rename them
for i, filename in enumerate(train_negative_images[:train_images_total//2]):
    source = os.path.join(source_train_negative, filename)
    new_filename = f"Neg_{i}.jpg"
    destination = os.path.join(destination_train_negative, new_filename)
    shutil.copy(source, destination)

for i, filename in enumerate(train_positive_images[:train_images_total//2]):
    source = os.path.join(source_train_positive, filename)
    new_filename = f"Pos_{i}.jpg"
    destination = os.path.join(destination_train_positive, new_filename)
    shutil.copy(source, destination)

# Transfer images to the test folders and rename them
for i, filename in enumerate(test_negative_images[:test_images_total//2]):
    source = os.path.join(source_test_negative, filename)
    new_filename = f"Neg_{i}.jpg"
    destination = os.path.join(destination_test_negative, new_filename)
    shutil.copy(source, destination)

for i, filename in enumerate(test_positive_images[:test_images_total//2]):
    source = os.path.join(source_test_positive, filename)
    new_filename = f"Pos_{i}.jpg"
    destination = os.path.join(destination_test_positive, new_filename)
    shutil.copy(source, destination)

# Transfer images to the validation folders and rename them
for i, filename in enumerate(validation_negative_images[:validation_images_total//2]):
    source = os.path.join(source_validation_negative, filename)
    new_filename = f"Neg_{i}.jpg"
    destination = os.path.join(destination_validation_negative, new_filename)
    shutil.copy(source, destination)

for i, filename in enumerate(validation_positive_images[:validation_images_total//2]):
    source = os.path.join(source_validation_positive, filename)
    new_filename = f"Pos_{i}.jpg"
    destination = os.path.join(destination_validation_positive, new_filename)
    shutil.copy(source, destination)

print('Image transfer completed.')
