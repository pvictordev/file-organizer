import os
import shutil
import sys

def organize_files(directory):
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
        "Documents": [".pdf", ".txt", ".doc", ".docx"],
        "Spreadsheets": [".xlsx", ".xls", ".csv"],
        "Others": [] 
    }

    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isdir(file_path):
            continue

        file_extension = os.path.splitext(filename)[1].lower()
        category_found = False

        for category, extensions in categories.items():
            if file_extension in extensions:
                category_folder = os.path.join(directory, category)
                os.makedirs(category_folder, exist_ok=True) 
                shutil.move(file_path, os.path.join(category_folder, filename))
                category_found = True
                break

        if not category_found:
            others_folder = os.path.join(directory, "Others")
            os.makedirs(others_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(others_folder, filename))

    print("Files have been organized.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_directory = sys.argv[1].strip()
    else:
        target_directory = os.getcwd()

    organize_files(target_directory)
