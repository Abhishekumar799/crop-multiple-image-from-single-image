from PIL import Image

# Load the image
image_path = "E:\Rag_models\multiple passport photo\data\passport_pic.jpg"  # Update this path to your image location
image = Image.open(image_path)

# Get the size of the original image
image_width, image_height = image.size

# Define the grid dimensions: 5 columns and 5 rows (total 25 images)
cols = 5
rows = 5

# Calculate the width and height of each cropped passport image
crop_width = image_width // cols
crop_height = image_height // rows

# Store each cropped image
cropped_images = []

# Iterate through the grid to crop each photo
for row in range(rows):
    for col in range(cols):
        left = col * crop_width
        upper = row * crop_height
        right = left + crop_width
        lower = upper + crop_height
        cropped_image = image.crop((left, upper, right, lower))
        cropped_images.append(cropped_image)

# Save each cropped image with a unique name
output_paths = []
for i, cropped_image in enumerate(cropped_images):
    output_path = f"E:\Rag_models\multiple passport photo\data\cropped_photos\cropped_passport_{i+1:02}.jpg"  # Update this path to your save location
    cropped_image.save(output_path)
    output_paths.append(output_path)

# Output paths of saved images
print(output_paths)
