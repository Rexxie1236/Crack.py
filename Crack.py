import zipfile
import os
import time

def crack_zip(zip_file, wordlist_file):
    # Check if the zip file exists
    if not os.path.exists(zip_file):
        print(f"Error: The zip file {zip_file} does not exist.")
        return
    
    # Check if the wordlist file exists
    if not os.path.exists(wordlist_file):
        print(f"Error: The wordlist file {wordlist_file} does not exist.")
        return

    # Open the zip file
    with zipfile.ZipFile(zip_file) as zipf:
        # Open the wordlist file
        with open(wordlist_file, 'r') as wordlist:
            for line in wordlist:
                # Strip the newline character from each line
                password = line.strip()
                try:
                    # Try extracting with the password
                    zipf.setpassword(password.encode())
                    zipf.testzip()  # This will attempt to extract the zip and check the password
                    print(f"Password found: {password}")
                    return  # Exit the loop once the password is found
                except RuntimeError:
                    # Password is incorrect, continue trying
                    continue

    print("Password not found in the wordlist.")

if __name__ == "__main__":
    # File paths (make sure these are correct)
    zip_file = 'path_to_your_zip_file.zip'
    wordlist_file = 'path_to_your_wordlist.txt'

    # Record start time for performance monitoring
    start_time = time.time()

    # Call the cracking function
    crack_zip(zip_file, wordlist_file)

    # Print how long the process took
    print(f"Time taken: {time.time() - start_time:.2f} seconds")
