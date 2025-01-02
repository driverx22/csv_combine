import os
import glob
import csv

# Specify the directory where the CSV files are located
directory = 'C:\Projects\old bank stmt'

# Get a list of all CSV files in the directory
csv_files = glob.glob(os.path.join(directory, '*.csv'))

# Specify the output file name
output_file = 'combined_file.csv'

# Open the output file in write mode
with open(output_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)

    # Iterate over each CSV file
    for file in csv_files:
        with open(file, 'r') as infile:
            reader = csv.reader(infile)

            # Write the rows from each file to the output file
            for row in reader:
                writer.writerow(row)

        # Add a blank row after each file's data
        writer.writerow([])

print(f"Combined CSV file '{output_file}' has been created.")