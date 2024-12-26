Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import os
import hashlib

def calculate_hash(file_path, algorithm='sha256'):
    """
    Calculates the hash of a given file using the specified algorithm.
... 
...     Args:
...         file_path (str): Path to the file.
...         algorithm (str): Hashing algorithm to use (default is 'sha256').
... 
...     Returns:
...         str: Hexadecimal hash value of the file content, or None if an error occurs.
...     """
...     # Check if the provided path is a directory
...     if os.path.isdir(file_path):
...         print(f"[Error] '{file_path}' is a directory. Please provide a valid file path.")
...         return None
... 
...     try:
...         # Create a hash object based on the specified algorithm
...         hash_func = hashlib.new(algorithm)
...         
...         # Open the file in binary mode
...         with open(file_path, 'rb') as file:
...             while chunk := file.read(8192):  # Read the file in 8KB chunks
...                 hash_func.update(chunk)     # Update the hash with the file content
... 
...         # Return the calculated hash as a hexadecimal string
...         return hash_func.hexdigest()
...     except FileNotFoundError:
...         # Handle cases where the file doesn't exist
...         print(f"[Error] File not found: {file_path}")
...         return None
...     except PermissionError:
...         # Handle permission errors when accessing the file
...         print(f"[Error] Permission denied: {file_path}")
...         return None
...     except Exception as e:
...         # Handle any unexpected errors
...         print(f"[Error] An unexpected error occurred: {e}")
...         return None
