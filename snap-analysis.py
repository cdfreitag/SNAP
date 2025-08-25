#import SNAP Analysis CSV into dataframe
import pandas as pd
df = pd.read_csv('SNAP_Analysis.csv')
print(df)

# Replace NaN values with 0
df = df.fillna(0)

# Recalculate 'PCT_SNAP_Households' by dividing 'SNAP_Households' by 'Total_Households' and multiplying by 100
df['PCT_SNAP_Households_numeric'] = (df['SNAP_Households'] / df['Total_Households']) * 100

# Handle potential division by zero where 'Total_Households' is 0
df['PCT_SNAP_Households_numeric'] = df['PCT_SNAP_Households_numeric'].replace([float('inf'), float('-inf')], 0)

# Display 'PCT_SNAP_Households_numeric' values as percentages
df['PCT_SNAP_Households'] = df['PCT_SNAP_Households_numeric'].apply(lambda x: f'{x:.2f}%' if pd.notna(x) else '')

# Display all rows with updated % of SNAP households column
print(df)

#Change name of Community Area #9 --> 'EDISON PARK' and Community Area #54 --> 'RIVERDALE'
df.loc[df['Community_Area_Number'] == 9, 'Community_Area'] = 'EDISON PARK'
print(df[df['Community_Area_Number'] == 9])
df.loc[df['Community_Area_Number'] == 54, 'Community_Area'] = 'RIVERDALE'
print(df[df['Community_Area_Number'] == 54])

# find the community areas with least number of SNAP stores 
df_sorted = df.sort_values(by='Store_Count', ascending=True)

# Display the all 77 rows of the sorted DataFrame
print(df_sorted)

#print community areas with least number of SNAP stores
print(f"The community areas with least number of SNAP stores are: {df_sorted['Community_Area'].iloc[0]} and {df_sorted['Community_Area'].iloc[1]}") 

# find the community area with highest % of SNAP households 
df_sorted = df.sort_values(by='PCT_SNAP_Households', ascending=False)

# Display the all 77 rows of the sorted DataFrame
print(df_sorted)

#print highest percentage of SNAP households 
print(f"The highest % of SNAP households: {df_sorted['Community_Area'].iloc[0]}")

# create column for density of SNAP stores by dividing 'Store_Count' by 'Area_Sq_Mi'
df['SNAP_Store_Density'] = df['Store_Count'] / df['Area_Sq_Mi']

# Handle potential division by zero (replace inf with 0  if preferred)
df['SNAP_Store_Density'] = df['SNAP_Store_Density'].replace([float('inf'), float('-inf')], 0)

# Display the first few rows with the new column
print(df.head())

#find community area with highest density of SNAP stores 
df_sorted = df.sort_values(by='SNAP_Store_Density', ascending=False)

# Display the all 77 rows of the sorted DataFrame
print(df_sorted)

#print community area with highest density of SNAP stores
print(f"The community area with the highest density of SNAP stores is: {df_sorted['Community_Area'].iloc[0]}")

# Find the average for 'SNAP_Store_Density'
average_snap_store_density = df['SNAP_Store_Density'].mean()

# Print the average
print(f"The average SNAP Store Density is: {average_snap_store_density:.2f}")

# Sort the DataFrame by 'PCT_SNAP_Households' and 'Store_Count' in descending order
df_sorted_combined = df.sort_values(by=['PCT_SNAP_Households', 'Store_Count'], ascending=[False, False])

# Display all rows 'Community_Area', 'PCT_SNAP_Households', and 'Store_Count' columns from the sorted DataFrame
print(df[['Community_Area', 'PCT_SNAP_Households', 'Store_Count']])


# List of SNAP store type columns
store_columns = ['Convenience_Store', 'Combination_Grocery_Other', 'Large_Grocery_Store',
                 'Medium_Grocery_Store', 'Small_Grocery_Store', 'Supermarket',
                 'Super_Store', 'Meat_Poultry_Specialty', 'Delivery_Route',
                 'Military_Commissary', 'Farmers_Market', 'Bakery_Specialty', 'Unknown',
                 'Fruits_Veg_Specialty', 'Food_Buying_Coop', 'Seafood_Specialty',
                 'Wholesaler']

# Calculate the sum for each store type column
store_counts = df[store_columns].sum()

# Sort the store types by their counts in descending order
sorted_store_counts = store_counts.sort_values(ascending=False)

# Print the sorted store types and their counts
print("Store types sorted by total count:")
print(sorted_store_counts)

#Find most frequent SNAP store type across Chicago community areas
# Calculate the total count of all stores
total_stores = df[store_columns].sum().sum()

# Calculate the percentage of total stores for each store type
store_percentages = (store_counts / total_stores) * 100

# Sort the percentages in descending order
sorted_store_percentages = store_percentages.sort_values(ascending=False)

# Print SNAP store types and their percentages
print("Store types as a percentage of total stores:")
print(sorted_store_percentages.apply(lambda x: f'{x:.2f}%'))

# Find the community area with most SNAP-accepting convenience stores
# Sort the DataFrame by 'Convenience_Store' in descending order
df_sorted_convenience = df.sort_values(by='Convenience_Store', ascending=False)

# Display 'Community_Area' and 'Convenience_Store' columns from the sorted DataFrame
print(df_sorted_convenience[['Community_Area', 'Convenience_Store']])