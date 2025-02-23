import uuid
import csv

# Read the CSV file
with open('newdata.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

# Add vendor ID column
for row in rows:
    row['vendor_id'] = str(uuid.uuid4())

# Write the updated data back to the file
fieldnames = reader.fieldnames + ['vendor_id']
with open('newdata.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)