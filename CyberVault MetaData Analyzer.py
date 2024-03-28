import exifread
import pyfiglet
from tkinter import Tk, filedialog

def get_file_path():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

def extract_metadata(file_path):
    try:
        with open(file_path, 'rb') as image_file:
            tags = exifread.process_file(image_file)
            return tags
    except Exception as e:
        print("Error:", e)
        return None

def main():
    while True:
        print(pyfiglet.figlet_format("CyberVault Metadata Analyzer", font='big'))  # Print CyberVault in big letters
        print("Welcome to CyberVaults Metadata Analyzer!")
        print("Select an option:")
        print("1. Select a file")
        print("2. Drag and drop a photo")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            print("Opening file dialog...")
            file_path = get_file_path()
            if not file_path:
                print("No file selected. Exiting...")
                return
        elif choice == '2':
            print("Please drag and drop a photo into the command prompt then click Enter:")
            file_path = input().strip()
            if not file_path:
                print("No file dropped. Exiting...")
                return
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        print("Analyzing metadata for:", file_path)

        metadata = extract_metadata(file_path)

        if metadata:
            print("\nMetadata:")
            for tag in metadata.keys():
                print(tag, ":", metadata[tag])
        else:
            print("No metadata found in the selected image file.")
        print("")
        print("")
        print("Select an option:")
        print("4. Analyze another photo")
        print("5. Exit")
        choice = input("\nEnter your choice (4 or 5): ")
        if choice == '5':
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
