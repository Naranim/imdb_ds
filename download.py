import argparse
from imdbpie import Imdb
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(description='IMDB reviews downloader', formatter_class=RawTextHelpFormatter)

parser.add_argument('-o', '--output', type=str, default='reviews.json',
                    help='output file')

parser.add_argument('movies_ids', type=str, nargs='+',
                    help="""list of movie's ids to download. Eg:\n
  tt1289401 - Ghostbusters\n
  tt1386697 - Suicide Squad\n
  tt2975590 - Batman v Superman: Dawn of Justice\n
  tt2094766 - Assassin's Creed""")

args = parser.parse_args()

movies_ids = args.movies_ids
output = args.output

imdb = Imdb()

imdbid_to_movie = {}
for movie_id in movies_ids:
    imdbid_to_movie[movie_id] = imdb.get_title_by_id(movie_id)

print "Movies to download:\n"

for movie_id in movies_ids:
    movie = imdbid_to_movie[movie_id]
    print "%s (%s):" % (movie.title, movie.imdb_id)
    print "\tYear:", movie.year
    print "\tTagline:", movie.tagline
    print "\tRating:", movie.rating
    print "\tGenres:", ", ".join(movie.genres)
    print "\tDirectors:", ", ".join([person.name for person in movie.directors_summary])
    print "\n"


reviews_list = []
for movie_id in movies_ids:
    print "Downloading reviews for:", imdbid_to_movie[movie_id].title
    raw_reviews = imdb.get_title_reviews(movie_id, max_results=10000)
    reviews_list += [{"username": r.username, "text": r.text, "rating": r.rating} for r in raw_reviews]


import json
with open(output, 'w') as outfile:
    json.dump(reviews_list, outfile)
