import pandas

df = pandas.read_csv('data.csv') #Creating a new dataframe using the read_csv function

df = df.drop(['Role'], axis = 1) # Remove 'Role' column
print(df)

#df = df.drop([3], axis = 0) # Remove row with index 3

#df['Source'] = 'Excel' # Add new column named 'Source' with each cell having value 'Excel'
 # Add new column named 'Source' with each cell having different value

print(df['Name']) # Gives the entire column 'Name'
print(df['Name'].values) # Gives the values of the column 'Name' in the form of a list

print(df.iloc[0:3,0:1]) # Obtains all the data/info available in the first 3 rows and only the first column

print(df)

df.to_csv('exported.csv') # We can export the available data frame to a csv file
