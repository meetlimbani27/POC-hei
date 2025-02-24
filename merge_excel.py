import pandas as pd

# Read the first Excel file (heinecan sample data)
df1 = pd.read_excel('heinecan sample data.xlsx', skiprows=1)  # Skip the header row
# Drop the first empty column and the Sr. number column
df1 = df1.iloc[:, 2:]
# Rename columns to match the desired structure
df1.columns = ['Vendor company name', 'Vendor name', 'Industry', 'Description', 'Contact number', 'Email id']

# Read the second Excel file (Generated_Vendor_Data)
df2 = pd.read_excel('Generated_Vendor_Data.xlsx')

# Ensure both dataframes have the same columns
required_columns = ['Vendor company name', 'Vendor name', 'Industry', 'Description', 'Contact number', 'Email id']

# Clean up the data
for df in [df1, df2]:
    # Remove any leading/trailing whitespace
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].str.strip()
    
    # Replace any None or NaN values with empty strings
    df.fillna('', inplace=True)

# Merge the dataframes
merged_df = pd.concat([df1, df2], ignore_index=True)

# Ensure all columns are present and in the correct order
merged_df = merged_df[required_columns]

# Remove any duplicate rows
merged_df.drop_duplicates(inplace=True)

# Save the merged data to a new Excel file
merged_df.to_excel('Merged_Data.xlsx', index=False)
print("Files merged successfully! Output saved as 'Merged_Data.xlsx'")
print(f"Total number of records: {len(merged_df)}")
