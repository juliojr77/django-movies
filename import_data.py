
import csv
import django
#export DJANGO_SETTINGS_MODULE="movieratings.settings"  ----> Commandline instruction
#echo $DJANGO_SETTINGS_MODULE
django.setup()
from movie_lens_online.models import Movie, Rater, Rating
from django.utils import timezone
import datetime

Movie.objects.all().delete()
Rater.objects.all().delete()
Rating.objects.all().delete()



#----------------------------------------------
# #Filling Movie table with dataset U.item
with open ('/Users/Pipita/movie_lenses/Data/u.item', encoding='latin_1') as movie_file:

    movie_dataset = csv.DictReader(movie_file, fieldnames=('movie_id', 'movie_title', 'release_date'), delimiter="|")

    for row in movie_dataset:

        cln_date = datetime.datetime.strptime(row['release_date'], "%d-%b-%Y").date()

        movie_row = Movie(movie_id=row['movie_id'], movie_title=row['movie_title'], release_date=cln_date) #action=row['action']
        movie_row.save()
#
#
# # -------------------------------------------
# # Filling Rater table with dataset U.user
with open ('/Users/Pipita/movie_lenses/Data/u.user') as user_file:

    user_dataset = csv.DictReader(user_file, fieldnames=('user_id', 'age', 'sex','occupation',  ""), delimiter="|") # 'zip_code',

    for row_1 in user_dataset:

        rater_row = Rater(user_id=row_1['user_id'], age=row_1['age'], sex=row_1['sex'], occupation=row_1['occupation']) #zip_code=row_1['zip_code']
        rater_row.save()


# --------------------------------------------
# Filling Ratings table with dataset U.data
with open ('/Users/Pipita/movie_lenses/Data/u.data') as ratings_file:

    ratings_dataset = csv.DictReader(ratings_file,  fieldnames=('user_id', 'movie_id', 'rating', ""), delimiter="\t")

    for row_2 in ratings_dataset:
        movie = Movie.objects.get(movie_id=row_2['movie_id'])

        rater = Rater.objects.get(user_id=row_2['user_id'])

        rating_row = Rating(rating=row_2['rating'], item_id=movie, user_id=rater)

        rating_row.save()


#____________________________________________________________

mov = Movie.objects.filter(movie_id = movie['movie_id'])
movie['avg_rating']=rating['rating__avg']

for movie in Movie.objects.values():
    mov = Movie.objects.get(movie_id=movie['movie_id'])
    print(mov.movie_id)
    rating = Rating.objects.filter(movie_id=movie['movie_id']).aggregate(Avg('rating'))
    mov.avg_rating = (rating['rating__avg'])
    mov.save()
