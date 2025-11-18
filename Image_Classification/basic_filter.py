from PIL import Image, ImageFilter, ImageEnhance
import matplotlib.pyplot as plt
import os
import numpy as np

def apply_blur_filter(image_path, output_path="blurred_image.png"):
    try:
        img = Image.open(image_path)
        img_resized = img.resize((128, 128))
        img_blurred = img_resized.filter(ImageFilter.GaussianBlur(radius=2))

        plt.imshow(img_blurred)
        plt.axis('off')
        plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
        plt.close()
        print(f"Processed image saved as '{output_path}'.")

    except Exception as e:
        print(f"Error processing image: {e}")

def apply_magical_filter(image_path, output_path="magical_image.png"):
    """
    Creates a magical filter effect by combining:
    - Enhanced color saturation
    - Soft glow effect
    - Edge enhancement
    - Brightness and contrast adjustments
    """
    try:
        # Open and resize the image
        img = Image.open(image_path)
        img_resized = img.resize((128, 128))
        
        # Step 1: Enhance color saturation for vibrant, magical colors
        enhancer = ImageEnhance.Color(img_resized)
        img_saturated = enhancer.enhance(1.5)  # Increase saturation by 50%
        
        # Step 2: Create a soft glow effect by blending with a blurred version
        img_blurred = img_saturated.filter(ImageFilter.GaussianBlur(radius=3))
        # Blend the original with the blurred version for a glowing effect
        img_glow = Image.blend(img_saturated, img_blurred, alpha=0.3)
        
        # Step 3: Enhance edges to make details pop
        img_edges = img_glow.filter(ImageFilter.EDGE_ENHANCE_MORE)
        # Blend edges back with the glowing image
        img_magical = Image.blend(img_glow, img_edges, alpha=0.4)
        
        # Step 4: Enhance brightness slightly for a dreamy, luminous effect
        brightness_enhancer = ImageEnhance.Brightness(img_magical)
        img_magical = brightness_enhancer.enhance(1.1)
        
        # Step 5: Enhance contrast to make colors more vibrant
        contrast_enhancer = ImageEnhance.Contrast(img_magical)
        img_magical = contrast_enhancer.enhance(1.2)
        
        # Step 6: Add a subtle color shift towards warmer/magical tones
        # Convert to numpy array for color manipulation
        img_array = np.array(img_magical)
        
        # Enhance blue and purple channels slightly for a magical hue
        if len(img_array.shape) == 3:  # Check if image has color channels
            # Boost blue channel slightly
            img_array[:, :, 2] = np.clip(img_array[:, :, 2] * 1.1, 0, 255)
            # Slightly boost red channel for warmth
            img_array[:, :, 0] = np.clip(img_array[:, :, 0] * 1.05, 0, 255)
        
        img_final = Image.fromarray(img_array.astype('uint8'))
        
        # Display and save the magical image
        plt.imshow(img_final)
        plt.axis('off')
        plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
        plt.close()
        print(f"Magical image saved as '{output_path}'.")

    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    print("Image Filter Processor (type 'exit' to quit)\n")
    print("Available filters: 'blur' or 'magical'")
    while True:
        filter_type = input("Choose filter type (blur/magical) or 'exit' to quit: ").strip().lower()
        if filter_type == 'exit':
            print("Goodbye!")
            break
        if filter_type not in ['blur', 'magical']:
            print("Please enter 'blur' or 'magical'")
            continue
        
        image_path = input("Enter image filename: ").strip()
        if not os.path.isfile(image_path):
            print(f"File not found: {image_path}")
            continue
        
        # Derive output filename based on filter type
        base, ext = os.path.splitext(image_path)
        if filter_type == 'blur':
            output_file = f"{base}_blurred{ext}"
            apply_blur_filter(image_path, output_file)
        else:  # magical
            output_file = f"{base}_magical{ext}"
            apply_magical_filter(image_path, output_file)