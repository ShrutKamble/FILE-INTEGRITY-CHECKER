Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import hashlib
import os
import json

# Function to calculate the hash of a given file
def calculate_hash(file_path, algorithm='sha256'):
    """
    Calculates the cryptographic hash of a file using the specified algorithm.

    Args:
        file_path (str): The path to the file.
        algorithm (str): The hashing algorithm to use (default is 'sha256').

    Returns:
        str: The hexadecimal representation of the file's hash, or None if the file doesn't exist.
    """
    try:
        # Create a new hash object based on the algorithm
        hash_func = hashlib.new(algorithm)
        
        # Open the file in binary mode to calculate the hash
        with open(file_path, 'rb') as file:
            while chunk := file.read(8192):  # Read the file in chunks
                hash_func.update(chunk)
        
        return hash_func.hexdigest()  # Return the hash value as a string
    except FileNotFoundError:
        print(f"[Error] File not found: {file_path}")
        return None

# Function to create a baseline hash for all files in a directory
def create_baseline(directory, algorithm='sha256'):
    """
    Scans a directory and generates a hash for each file to create a baseline.

    Args:
        directory (str): The path to the directory to monitor.
        algorithm (str): The hashing algorithm to use.

    Returns:
        dict: A dictionary containing file paths as keys and their hash values as values.
    """
    baseline = {}
    
    # Walk through the directory recursively
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path, algorithm)  # Calculate the file's hash
            
            if file_hash:  # If the hash is valid, add it to the baseline
                baseline[file_path] = file_hash

    return baseline

# Function to check for file integrity based on the baseline
def check_integrity(baseline, algorithm='sha256'):
    """
    Compares the current state of files to the baseline to detect changes.

    Args:
        baseline (dict): A dictionary containing the baseline file paths and hashes.
        algorithm (str): The hashing algorithm to use.

    Returns:
        dict: A summary of changes (modified, deleted, and new files).
    """
    changes = {
        "modified": [],
        "deleted": [],
        "new": []
    }

    # Check for modified or deleted files
    for file_path, old_hash in baseline.items():
        if os.path.exists(file_path):
            current_hash = calculate_hash(file_path, algorithm)
...             if current_hash != old_hash:
...                 changes["modified"].append(file_path)
...         else:
...             changes["deleted"].append(file_path)
... 
...     # Check for new files
...     current_files = set()
...     for root, _, files in os.walk(os.path.dirname(list(baseline.keys())[0])):
...         for file in files:
...             current_files.add(os.path.join(root, file))
... 
...     new_files = current_files - set(baseline.keys())
...     changes["new"].extend(new_files)
... 
...     return changes
... 
... # Function to save the baseline to a JSON file
... def save_baseline(baseline, output_file):
...     """
...     Saves the baseline data to a JSON file for future integrity checks.
... 
...     Args:
...         baseline (dict): The baseline data to save.
...         output_file (str): The name of the file to save the baseline.
...     """
...     with open(output_file, 'w') as file:
...         json.dump(baseline, file, indent=4)
...         print(f"[Info] Baseline saved to {output_file}")
... 
... # Function to load a baseline from a JSON file
... def load_baseline(input_file):
...     """
...     Loads the baseline data from a JSON file.
... 
...     Args:
...         input_file (str): The path to the JSON file containing the baseline data.
... 
...     Returns:
...         dict: The loaded baseline data.
    """
    with open(input_file, 'r') as file:
        return json.load(file)

# Main function to drive the program
def main():
    """
    Main menu to either create a new baseline or check file integrity.
    """
    print("Choose an option:")
    print("1. Create baseline")
    print("2. Check integrity")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        directory = input("Enter the directory to monitor: ")
        output_file = input("Enter the filename to save the baseline (e.g., baseline.json): ")
        
        baseline = create_baseline(directory)
        save_baseline(baseline, output_file)
        print(f"[Success] Baseline created and saved to '{output_file}'.")
    
    elif choice == "2":
        baseline_file = input("Enter the baseline file (e.g., baseline.json): ")
        
        try:
            baseline = load_baseline(baseline_file)
            changes = check_integrity(baseline)
            
            print("\nFile Integrity Check Results:")
            print("Modified Files:", changes["modified"])
            print("Deleted Files:", changes["deleted"])
            print("New Files:", changes["new"])
        except FileNotFoundError:
            print(f"[Error] Baseline file not found: {baseline_file}")
    
    else:
        print("[Error] Invalid choice! Please select either 1 or 2.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
