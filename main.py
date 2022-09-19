import pandas as pd

def get_sim (movie_name, user_rating):
    sim_score = sim_df[movie_name]*[user_rating-2.5]
    sim_score.sort_values(ascending=False)

    return sim_score

#importing data files
df1= pd.read_csv (r'/Users/jinyilu/opt/anaconda3/envs/movie_rec/dataset/movies.csv')
df2= pd.read_csv (r'/Users/jinyilu/opt/anaconda3/envs/movie_rec/dataset/ratings.csv')

df= pd.merge(df1,df2, on='movieId')
df= df.pivot_table(values='rating', columns='title', index='userId')
df = df.dropna(thresh=15, axis= 1)
df = df.fillna(value= 0)
sim_df = df.corr(method='pearson')

sim_movies= pd.DataFrame()

movie_name = input ("enter a movie's name\n")

movie_ratings = int (input("enter your rating (out of 5) for the movie\n"))

sim_movies = pd.DataFrame (data=get_sim(movie_name,movie_ratings))
sim_movies = sim_movies.c
sim_movies.columns = {'scores'}
sim_movies= sim_movies.sort_values(by='scores', ascending=False)
sim_movies= sim_movies.drop('1')
print (sim_movies.head(5))
