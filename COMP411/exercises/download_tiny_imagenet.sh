#!/bin/bash

# Step 1: Set up directories
echo "Creating necessary directories..."
mkdir -p tiny_imagenet
cd tiny_imagenet || exit

# Step 2: Download the dataset
echo "Downloading Tiny ImageNet dataset..."
wget -q --show-progress http://cs231n.stanford.edu/tiny-imagenet-200.zip

# Step 3: Extract the dataset
echo "Extracting dataset..."
unzip -q tiny-imagenet-200.zip
cd tiny-imagenet-200 || exit

# Step 4: Organize validation images into class directories
echo "Organizing validation images..."

# Create a directory for the reorganized validation set
mkdir -p val_processed

# Step 4.1: Create directories for each class listed in wnids.txt
while read -r class_id; do
    mkdir -p val_processed/$class_id
done < wnids.txt

# Step 4.2: Move validation images into respective class directories
while read -r line; do
    image_name=$(echo $line | awk '{print $1}')      # Extract image name
    class_id=$(echo $line | awk '{print $2}')       # Extract class ID
    if [ -d "val_processed/$class_id" ]; then
        mv val/images/$image_name val_processed/$class_id/
    else
        echo "Warning: Directory val_processed/$class_id does not exist."
    fi
done < val/val_annotations.txt

# Step 4.3: Replace original validation directory with the organized one
rm -rf val/images
mv val_processed val

# Step 5: Final adjustment to fix directory structure
echo "Fixing validation directory structure..."
cd val || exit
mv val_processed/* .
rm -rf val_processed
cd ..

# Step 6: Cleanup unnecessary files
echo "Cleaning up unnecessary files..."
rm -f ../tiny-imagenet-200.zip

# Final message
echo "Tiny ImageNet dataset has been successfully downloaded and organized!"