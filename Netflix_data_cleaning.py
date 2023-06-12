import pandas as pnd

# reading csv file
netflix = pnd.read_csv('C:/Users/Nowy_użytkownik/Desktop/netflix.csv')

# overwiew of the data
netflix.head()
netflix.shape

# loooking for duplicated values
netflix.duplicated().sum()

# removing unnecessary column 
netflix = netflix.drop('show_id', axis = 1)

# checking data types 
netflix.dtypes

# converting 'date_added' column values to datetime type
netflix['date_added'] = pnd.to_datetime(netflix['date_added'])

# conversion succeded
netflix.dtypes

# copying data from 'duration' column to new column 'seasons_count'
netflix['seasons_count'] = netflix['duration']

# replacing unnecessary data from 'duration' column with '0'
netflix['duration'] = netflix['duration'].str.replace('.+Season.*','0')

# removing 'min' from 'duration' column
netflix['duration'] = netflix['duration'].str.replace('\smin','')

# replacing unnecessary data from 'seasons_count' column with '0'
netflix['seasons_count'] = netflix['seasons_count'].str.replace('\d+\smin','0')

# removing 'Season(s)' from 'seasons_count' column
netflix['seasons_count'] = netflix['seasons_count'].str.replace('\sSeason.?','')

# renaming column 
netflix = netflix.rename(columns = {'duration':'duration_min'})

# changing datatype in 'duration_min' column to integer
netflix['duration_min'] = netflix['duration_min'].astype(int)

# datatype successfully changed
netflix.dtypes

# changing datatype in 'seasons_count' column to integer
netflix['seasons_count'] = netflix['seasons_count'].astype(int)

# datatype successfully changed
netflix.dtypes

# looking for null values
netflix.isna().sum()

# changing order of columns
netflix = netflix.iloc[:,[1,0,2,3,4,5,6,7,9,8]]



