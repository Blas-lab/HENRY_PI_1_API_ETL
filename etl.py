import pandas as pd

# Load the dataset files into separate dataframes

amazon_data = pd.read_csv("./Datasets/amazon_prime_titles-score.csv")
disney_data = pd.read_csv("./Datasets/disney_plus_titles-score.csv")
hulu_data = pd.read_csv("./Datasets/hulu_titles-score (2).csv")
netflix_data = pd.read_csv("./Datasets/netflix_titles-score.csv")

# Add platform column to each dataframe and set the value to the corresponding platform name

amazon_data['platform'] = 'amazon_prime'
disney_data['platform'] = 'disney_plus'
hulu_data['platform'] = 'hulu'
netflix_data['platform'] = 'netflix'

# Display the first few rows of each dataframe to check if the column was added correctly

print(amazon_data.head())
print(disney_data.head())
print(hulu_data.head())
print(netflix_data.head())

# Concatenate the dataframes into one

data = pd.concat([amazon_data, disney_data, hulu_data, netflix_data])

# Display the first few rows of the concatenated dataframe

print(data.head())

# Concatenate the dataframes into one

data = pd.concat([amazon_data, disney_data, hulu_data, netflix_data])

# Display the first few rows

print(data.head())

# Create id column

data['id'] = data['show_id'].apply(lambda x: 'as' + x)

# Normalize the value of duration column to singular

data['duration'] = data['duration'].str.rstrip('s')

# Create duration_int and duration_type columns

data.dropna(subset=['duration'], inplace=True)
data['duration_int'] = data['duration'].apply(lambda x: int(x.split()[0]))
data['duration_type'] = data['duration'].apply(lambda x: x.split()[1])

# Create season colum containing duration_int value if duration_type column is = to tv show

data['season'] = data.apply(lambda x: x['duration_int'] if x['duration_type'] == 'tv show' else None, axis=1)

# Replace null values in rating column with "G"

data['rating'].fillna("G", inplace=True)

# Convert date_added to "yyyy-mm-dd" format

data['date_added'] = data['date_added'].str.strip()
data['date_added'] =  pd.to_datetime(data['date_added'], format='%B %d, %Y').dt.strftime('%Y-%m-%d')

# Display first few rows

print(data.head())

# Normalize the values of the text columns

data['type'] = data['type'].str.lower()
data['title'] = data['title'].str.lower()
data['director'] = data['director'].str.lower()
data['cast'] = data['cast'].str.lower()
data['country'] = data['country'].str.lower()
data['listed_in'] = data['listed_in'].str.lower()
data['description'] = data['description'].str.lower()


# Colum printing for check

print(data.columns)

# Checking for the colum season

if 'season' in data.columns:
    grouped_data = data.groupby(['title', 'season'], as_index=False).mean(numeric_only=True)
else:
    print("The 'season' column does not exist in the dataframe.")

#Convert the 'duration_int' and 'score' columns to integer data type, to prevent the issue of compatibility with JSON serializable


data['duration_int'] = data['duration_int'].astype(int)
data['score'] = data['score'].astype(int)

# Create the dataframe

data_df = pd.DataFrame(data)

# Print the dataframe

print(data_df)

# Export the dataframe as "clean_data.csv"

data_df.to_csv(r'C:\Users\miauchis\Desktop\PIs\PI-Data-Engineering\ETL_API\my_project\clean_data.csv', index=False)


# Group the data by 'platform', 'title', and 'score'

platform_title_score = data.groupby(['platform', 'title', 'score'], as_index=False).mean(numeric_only=True)

# Group the data by 'platform', 'title', and 'rating'

platform_title_rating = data.groupby(['platform', 'title', 'rating'], as_index=False).mean(numeric_only=True)

# Group the data by 'title', and 'score'

title_score = data.groupby(['title', 'score'], as_index=False).mean(numeric_only=True)

# Group the data by 'platform', 'title', 'score', and 'season'

platform_title_score_season = data.groupby(['platform', 'title', 'rating', 'season'], as_index=False).mean(numeric_only=True)

# Group the data by 'type', 'rating', and 'score'

type_rating_score = data.groupby(['type', 'rating', 'score'], as_index=False).mean(numeric_only=True)



