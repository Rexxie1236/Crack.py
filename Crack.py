import time
import sys
import os

def crack_file(file_path):
    """
    This function reads a .txt file and extracts IDs and passwords.

    Args:
        file_path (str): Path to the text file.

    Returns:
        None
    """
    try:
        if not os.path.exists(file_path):
            print(f"Error: The file {file_path} does not exist.")
            return

        print(f"Opening file: {file_path}")
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        print("Searching for IDs and passwords...")
        found = False
        for line in lines:
            # Assuming the format of each line is "ID: [some_id], Password: [some_password]"
            if "ID:" in line and "Password:" in line:
                found = True
                print(line.strip())  # Print the full matching line
        
        if not found:
            print("No IDs and passwords found in the file.")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Ensure the script has the correct arguments
    if len(sys.argv) != 2:
        print("Usage: python Crack.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]

    start_time = time.time()
    print("Starting the cracking process...")
    
    crack_file(file_path)
    
    elapsed_time = time.time() - start_time
    print(f"Time taken: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
