import pandas as pd

# Read both Excel files
df1 = pd.read_excel('heinecan sample data.xlsx')
df2 = pd.read_excel('Generated_Vendor_Data.xlsx')

# Merge the dataframes
merged_df = pd.concat([df1, df2], ignore_index=True)

# Save the merged data to a new Excel file
merged_df.to_excel('Merged_Data.xlsx', index=False)
print("Files merged successfully! Output saved as 'Merged_Data.xlsx'")
