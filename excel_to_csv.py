import pandas as pd

# Read the Excel file
df = pd.read_excel('Merged_Data.xlsx')

# Save as CSV
df.to_csv('Merged_Data.csv', index=False)
print("Conversion completed! File saved as 'Merged_Data.csv'")
