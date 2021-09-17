import csv

with open("movies.csv",encoding="utf-8") as f:
    csvreader=csv.reader(f)
    data=list(csvreader)
    headers=data[0]
    All_movies=data[1:]
headers.append("poster_link")

with open ("movieMerged.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    
with open("MoviePoster.csv",encoding="utf-8") as f:
    csvreader1=csv.reader(f)
    data=list(csvreader1)
    links=data[1:]
for movie in All_movies:
    poster=any(movie[8]in link_items for link_items in links)
    if poster:
        for movie_link_item in links:
            if movie[8]==movie_link_item[0]:
                movie.append(movie_link_item[1])
                if len(movie)==28:
                    with open ("movieMerged.csv","a+",encoding="utf-8") as f:
                        csvwriter1=csv.writer(f)
                        csvwriter1.writerow(movie)
