# from django.db import models
#
# # Create your models here.
#
# class Rater(models.Model):
#     user_id = models.CharField(max_length=3)
#     age = models.IntegerField()
#     gender = models.CharField(max_length=1)
#     occupation = models.CharField(max_length=200)
#     zip_code = models.CharField(max_length=5)
#
#
#
# class Movie(models.Model):
#     movie_id = models.CharField(max_length=6)
#     movie_title = models.CharField(max_length=200)
#     release_date = models.DateField('release_date')
#     action = models.CharField(max_length=1)
#     avg_rating = models.FloatField(default=0)
#
#
# class Rating(models.Model):
#     user_id = models.ForeignKey(Rater, on_delete=models.CASCADE)
#     item_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     rating = models.IntegerField(default=0)

#-------------------------------------
from django.db import models

# Create your models here.
class Rater(models.Model):
    user_id = models.CharField(max_length=255, primary_key=True)
    age = models.CharField(max_length=255)
    sex = models.CharField(max_length=255, default ='')
    occupation = models.CharField(max_length=255)


class Movie(models.Model):
    movie_id = models.CharField(max_length=255, primary_key=True)
    movie_title = models.CharField(max_length=255)
    release_date = models.CharField(max_length=255)
    avg_rating = models.FloatField(default=0)
#    avg_rating = round(models.FloatField(default=0),2)

class Rating(models.Model):
    # movie_id = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    rater = models.ForeignKey(Rater, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # movie_name = models.CharField(max_length=255, default ='')
