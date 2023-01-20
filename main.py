from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/word_count/{platform}/{word}")
async def get_word_count(platform: str, word: str):
    # Load the clean_data.csv file into a dataframe
    data = pd.read_csv("./clean_data.csv")
    
    # Filter the dataframe to only include rows where the platform column is equal to the input platform
    data = data[data['platform'] == platform]
    
    # Count the number of occurrences of the input word in the title column
    count = data[data['title'].str.contains(word, case=False)].shape[0]
    
    return {"platform": platform, "count": count}



@app.get("/score_count/{platform}/{score}/{year}")
async def get_score_count(platform: str, score: int, year: int):
    # Load the clean_data.csv file into a dataframe
    data = pd.read_csv("./clean_data.csv")
    
    # Filter the dataframe to only include rows where the platform column is equal to the input platform, the score column is greater than the input score and the release_year column is equal to the input year
    data = data[(data['platform'] == platform) & (data['score'] > score) & (data['release_year'] == year) & data['type'].isin(['movie', 'tv series'])]
    
    # Count the number of rows in the filtered dataframe
    count = data.shape[0]
    
    return {"platform": platform, "count": count}


@app.get("/second_score/{platform}")
async def get_second_score(platform: str):
    # Load the clean_data.csv file into a dataframe
    try:
        data = pd.read_csv("./clean_data.csv")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except:
        raise HTTPException(status_code=500, detail="Server error")
    
    # Filter the dataframe to only include rows where the platform column is equal to the input platform, and the type column is equal to 'movie'
    data = data[(data['platform'] == platform) & (data['type'] == 'movie')]

    if data.empty:
        raise HTTPException(status_code=404, detail="No data found for the given platform")
    else:
        # Sort the dataframe by score in descending order and title in ascending order
        data = data.sort_values(by=['score', 'title'], ascending=[False, True])
        
        # Get the second row of the sorted dataframe
        second_highest_score = data.iloc[1]
        
        # Return the title and score of the second highest score movie
        return {"title": second_highest_score['title'], "score": int(second_highest_score['score'])}

@app.get("/get_longest/{plataform}/{duration_type}/{year}")
async def get_longest(plataform: str, duration_type: str, year: int):
    try:
        # Load csv as a dataframe
        data = pd.read_csv("./clean_data.csv")
        # Filter data
        filtered_data = data[(data['platform'] == plataform) & (data['duration_type'] == duration_type) & (data['release_year'] == year)]
        longest_movie = filtered_data.sort_values(by=['duration_int'], ascending=False).loc[:, ["title", "duration_int", "duration_type"]].iloc[0]
        # convert to list of dictionaries with the values only
        longest_movie_list = longest_movie.astype(str).values.tolist()
        return longest_movie_list
    except:
        raise HTTPException(status_code=404, detail="No movies found for the specified platform, duration type, and year.")



@app.get("/count_by_rating/{rating}")
async def count_by_rating(rating: str):
    # Load the clean_data.csv file into a dataframe
    data = pd.read_csv("./clean_data.csv")

    # Filter the dataframe to only include rows where the rating column is equal to the input rating
    data = data[data['rating'] == rating]

    # Count the number of rows in the filtered dataframe, grouped by the 'type' column
    count = data.groupby('rating').size().reset_index(name='count')

    return count.to_dict(orient='records')