import multiprocessing
from PIL import Image # Example of an image processing library

def process_image(image_path):
    """Performs CPU-intensive image processing on a single image."""
    # Load the image
    image = Image.open(image_path)
    # Apply filters, transformations, or any desired processing
    image = image.convert('L') # Example: convert to grayscale
    # Save the processed image
    image.save(f'processed_{image_path}')

if _name_ == '__main__':
    image_paths = ['image1.jpg', 'image2.jpg', ...] # List of image paths
    # Create a pool of processes (adjust the number based on your CPU cores)
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        # Map the 'process_image' function to each image path in parallel
        pool.map(process_image, image_paths)