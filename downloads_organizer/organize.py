import os
import shutil

# Define the path to your Downloads folder
DOWNLOADS_FOLDER = '/Users/jorgehabib/Downloads'

# Define file types and their corresponding folders
file_types = {
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Music': ['.mp3', '.wav', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.sh', '.js', '.html', '.css'],
    'Others': []
}

def organize_downloads():
    # List all files in the Downloads folder
    for filename in os.listdir(DOWNLOADS_FOLDER):
        # Get the full file path
        file_path = os.path.join(DOWNLOADS_FOLDER, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get the file extension (e.g., .pdf, .jpg)
        file_extension = os.path.splitext(filename)[1].lower()

        # Initialize a flag to check if the file was moved
        moved = False

        # Check which folder the file belongs to based on its extension
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                destination_folder = os.path.join(DOWNLOADS_FOLDER, folder)
                
                # Create the folder if it doesn't exist
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                
                # Move the file to the appropriate folder
                shutil.move(file_path, os.path.join(destination_folder, filename))
                print(f"Moved {filename} to {folder}")
                moved = True
                break

        # If no matching folder was found, move the file to "Others"
        if not moved:
            other_folder = os.path.join(DOWNLOADS_FOLDER, 'Others')
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"Moved {filename} to Others")

if __name__ == "__main__":
    organize_downloads()