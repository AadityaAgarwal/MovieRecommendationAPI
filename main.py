from flask import Flask,request,jsonify
import csv

from DemographicFiltering import output
from ContentFiltering import getRecommendations

from Storage import AllMovies,Disliked_Movies,Liked_Movies,Did_Not_Watch_Movies

app=Flask(__name__)
@app.route('/getMovie')

def getMovie():
    MovieData={"title":AllMovies[0][19],"poster_link":[0][27],"release_date":[0][13],"overview":[0][9],"duration":[0][],"rating":[0][]}
    return jsonify({'data':MovieData,"status":"success"})

@app.route('/likedMovie',methods=["POST"])

def likedMovie():
    movie=AllMovies[0]
    AllMovies.pop(0)
    Liked_Movies.append(movie)
   
    return jsonify({"status":"success"})

@app.route('/dislikedMovie',methods=["POST"])

def disliked():
    movie=AllMovies[0]
    AllMovies.pop(0)
    Disliked_Movies.append(movie)
    return jsonify({"status":"success"})

def didNotWatch():
    movie=AllMovies[0]
    AllMovies.pop(0)
    Did_Not_Watch_Movies.append(movie)
    return jsonify({"status":"success"})

if __name__=="__main__":
    app.run()
    