"""
Standalone script to apply the magical filter to an image.
This script will process the image in the assets folder.
"""
from basic_filter import apply_magical_filter
import os

if __name__ == "__main__":
    # Path to the image in assets folder
    image_path = "assets/Image_Classification_unsplash.jpg"
    
    if not os.path.isfile(image_path):
        print(f"Error: Image not found at {image_path}")
        print("Please make sure the image is in the assets folder.")
    else:
        # Output will be saved in the assets folder with _magical suffix
        base, ext = os.path.splitext(image_path)
        output_path = f"{base}_magical{ext}"
        
        print(f"Applying magical filter to {image_path}...")
        apply_magical_filter(image_path, output_path)
        print(f"\nMagical filter applied! Output saved to: {output_path}")

