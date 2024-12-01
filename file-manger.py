import os
import shutil

# Function to change directory
def change_directory():
    try:
        new_path = input("Enter the directory to change to: ").strip()
        os.chdir(new_path)
        print(f"[*] The directory changed to: {os.getcwd()}")
    except FileNotFoundError:
        print("[*] The directory was not found!")
    except NotADirectoryError:
        print("[*] The path is not a directory!")
    except PermissionError:
        print("[*] You don't have permission to access the directory!")
    except Exception as e:
        print(f"[*] An error occurred: {e}")

# Function to list files in the current directory
def list_files():
    try:
        files = os.listdir()
        print(f"\n[*] Files in directory {os.getcwd()}:\n")
        for file in files:
            print(file)
    except PermissionError:
        print("[*] You don't have permission to access this directory!")
    except Exception as e:
        print(f"[*] An error occurred: {e}")

# Function to delete a file
def delete_file():
    try:
        file_path = input("Enter the file path to delete: ").strip()
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"[*] The file {file_path} has been deleted.")
        else:
            print(f"[*] The file {file_path} does not exist or is not a file.")
    except FileNotFoundError:
        print("[*] The file was not found!")
    except PermissionError:
        print("[*] You don't have permission to delete the file!")
    except Exception as e:
        print(f"[*] An error occurred: {e}")

# Function to copy a file
def copy_file():
    try:
        source = input("Enter the source file path: ").strip()
        destination = input("Enter the destination file path: ").strip()

        # Check if the source file exists
        if os.path.isfile(source):
            # Ensure the destination directory exists
            destination_dir = os.path.dirname(destination)
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
                print(f"[*] The destination directory {destination_dir} was created.")

            # Copy the file
            shutil.copy(source, destination)
            print(f"[*] The file {source} has been copied to {destination}")
        else:
            print(f"[*] The source file {source} does not exist.")
    except PermissionError:
        print("[*] You don't have permission to copy the file!")
    except Exception as e:
        print(f"[*] An error occurred: {e}")

# Main file manager loop
def file_manager():
    while True:
        command = input("Enter command (cd, ls, rm, cp, exit): ").strip().lower()

        if command == "cd":
            change_directory()
        elif command == "ls":
            list_files()
        elif command == "rm":
            delete_file()
        elif command == "cp":
            copy_file()
        elif command == "exit":
            print("[*] Exiting the file manager.")
            break
        else:
            print("[*] Unknown command. Please try again.")

if __name__ == "__main__":
    file_manager()
