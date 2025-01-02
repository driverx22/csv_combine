# CSV File Combiner

A Python utility that consolidates multiple CSV files into a single combined CSV file. Particularly useful for merging periodic data files, such as monthly bank statements stored in separate CSV files.

## Features
- Combines multiple CSV files from a specified directory into a single consolidated CSV file
- Uses Python's built-in libraries (`os`, `glob`, `csv`) for efficient file handling
- Preserves data structure from source files
- Ideal for merging periodic data (e.g., monthly financial statements, transaction logs)

## Requirements
- Python 3.x
- No external dependencies required! Uses only built-in Python libraries:
  - `os` for file operations
  - `glob` for file pattern matching
  - `csv` for reading/writing CSV files

## Installation
```bash
git clone https://github.com/yourusername/csv-combiner
cd csv-combine