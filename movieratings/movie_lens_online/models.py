from django.db import models

# Create your models here.

class Rater(models.Model):
    user_id = models.CharField(max_length=3)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=5)



class Movie(models.Model):
    movie_id = models.CharField(max_length=6)
    movie_title = models.CharField(max_length=200)
    release_date = models.DateField('release_date')
    action = models.CharField(max_length=1)


class Rating(models.Model):
    user_id = models.ForeignKey(Rater, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)


#timestamp.
