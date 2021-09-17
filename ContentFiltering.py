from ast import literal_eval
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer as cvt
from sklearn.metrics.pairwise import cosine_similarity as cs

df2=pd.read_csv("movieMerged.csv")

df2=df2[df2["soup"].notna()]

count=cvt(stop_words='english')
count_matrix=count.fit_transform(df2["soup"])
cosine_sim2=cs(count_matrix,count_matrix)

df2=df2.reset_index()
indices=pd.Series(df2.index,index=df2["title"])

def getRecommendations(title,cosine_sim):
  idx=indices[title]
  sim_scores=list(enumerate(cosine_sim[idx]))
  sim_scores=sorted(sim_scores,key=lambda x:x[1],reverse=True)
  sim_scores=sim_scores[1:11]
  movie_indices=[i[0]for i in sim_scores]
  return list(df2[["Title","vote_count","vote_average","poster_link"]].iloc[movie_indices].values)
