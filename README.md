# FILE-INTEGRITY-CHECKER

**COMPANY**: CODTECH IT SOLUTIONS

**NAME**: SHRUT RAJENDRA KAMBLE

**INTERN ID**: CT6WGTJ

**DOMAIN**: CYBERSECURITY & ETHICAL HACKING

**BATCH DURATION**: DEC 25TH,2024 TO FEB 10TH 2025

**MENTOR NAME**: NEELA SANTHOSH

# This project is a Python-based tool designed to monitor changes in files within a specified directory and ensure file integrity. It works by calculating and comparing hash values (using algorithms like SHA256 or MD5) to detect modifications, deletions, or the addition of new files. The tool creates a baseline of file hashes, stores it in a JSON file for future reference, and provides a detailed report of changes when integrity is checked. It is ideal for securing file systems and ensuring data authenticity.

How It Works:

Create a Baseline: Run the program, select the option to create a baseline, and provide the directory to monitor. The tool generates a JSON file containing hash values for all files in the directory.
Check Integrity: Run the program again, select the integrity check option, and provide the baseline file. The tool compares current file states with the baseline to identify changes.
