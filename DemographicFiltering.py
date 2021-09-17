import pandas as pd
import numpy as np

df2=pd.read_csv("movieMerged.csv")

c=df2["vote_average"].mean()
m=df2["vote_count"].quantile(0.9)
movie_valid_vote=df2.copy().loc[df2["vote_count"]>=m]

def weighted_rating(x,m=m,c=c):
  v=x["vote_count"]
  r=x["vote_average"]
  return (v/(v+m)*r)+(m/(v+m)*c)

movie_valid_vote["weighted_rating"]=movie_valid_vote.apply(weighted_rating,axis=1)
movie_valid_vote=movie_valid_vote.sort_values("weighted_rating",ascending=False)
output=movie_valid_vote[["Title","vote_count","vote_average","weighted_rating"]].head(20).values.to_list()