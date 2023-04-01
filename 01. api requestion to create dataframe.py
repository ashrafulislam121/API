import pandas as pd
import requests

# id
# title
# release_date
# overview
# popularity
# vote_average
# vote_count

response = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=eb89cf568719687d6242b0e5c10e54e4&language=en-US&page=2")
df = pd.DataFrame(response.json()['results'])

df = df[['id','title','overview','vote_average']]