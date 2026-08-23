import os
import shutil
from datetime import datetime

# Path to your Downloads directory
downloads_dir = "Downloads"

# List all files in the Downloads directory
files = os.listdir(downloads_dir)

# Iterate over each file in the Downloads folder
for file in files:
    file_path = os.path.join(downloads_dir, file) 

    # Ignore subdirectories, process files only
    if os.path.isfile(file_path):
        # Get the modification time of the file
        modified_time = os.path.getmtime(file_path)

        # Convert the modification time to a datetime object
        date = datetime.fromtimestamp(modified_time)
        year = date.year
        month = date.strftime("%B")

        # Print each file and their modification dates (for testing purposes)
        # Step 4: Comment out the testing print statement
        # print(f"File: {file}, Modified: {month} {year}")

        # Step 5: Create the directory path for the year and month
        target_dir = os.path.join(downloads_dir, str(year), month)

        # Create the directory if it doesn't exist
        os.makedirs(target_dir, exist_ok=True)

        # Step 6: Move the file to the new directory
        target_path = os.path.join(target_dir, file)
        shutil.move(file_path, target_path)

        # Step 7: Print a confirmation message
        print(f"Moved {file} to {target_dir}")


# Please be careful to follow instructions on how to run the program; review Step 3.
# The Run menu or right-click > Run do not work in the simulated environment. You must use the terminal window as directed.