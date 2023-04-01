import pandas as pd
import requests

df = pd.DataFrame()
print(df)

for i in range(1,548):
    response = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=eb89cf568719687d6242b0e5c10e54e4&language=en-US&page={}".format(i))
    temp_df = df = pd.DataFrame(response.json()['results'])[['id','title','overview','vote_average']]
    df.append(temp_df, ignore_index = True)
    
df.to_csv("movies.csv")