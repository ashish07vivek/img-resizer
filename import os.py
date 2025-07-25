import os
from PIL import Image

input_folder = 'input_images'      
output_folder = 'resized_images'    
target_size = (800, 800)            
output_format = 'JPEG'             

os.makedirs(output_folder, exist_ok=True)

extensions = ['.jpg', '.jpeg', '.png', '.webp', '.bmp']

# Process images
for filename in os.listdir(input_folder):
    ext = os.path.splitext(filename)[1].lower()
    if ext in extensions:
        try:
            img_path = os.path.join(input_folder, filename)
            with Image.open(img_path) as img:
                img = img.convert('RGB')  # To avoid alpha-channel issues in JPEG
                img_resized = img.resize(target_size)

                output_name = os.path.splitext(filename)[0] + '.' + output_format.lower()
                output_path = os.path.join(output_folder, output_name)

                img_resized.save(output_path, output_format)
                print(f"Processed: {filename} → {output_name}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
