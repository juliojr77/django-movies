# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-06 02:25
from __future__ import unicode_literals

from django.db import migrations

from movie_lens_online.models import Rater,  Movie,  Rating
import csv

from django.db.models import Avg


#Rating.objects.all().delete()

def import_ratings(apps, schema_editor):
    Rating = apps.get_model("movie_lens_online", "Rating")
    Movie = apps.get_model("movie_lens_online", "Movie")
    Rater = apps.get_model("movie_lens_online", "Rater")
    with open ('/Users/David/documents/django-movies/django-movies/Data/u.data') as ratings_file:

        ratings_dataset = csv.DictReader(ratings_file,  fieldnames=('user_id', 'movie_id', 'rating', ""), delimiter="\t")

        for row in ratings_dataset:
            movie = Movie.objects.get(movie_id=row['movie_id'])

            rater = Rater.objects.get(user_id=row['user_id'])

            rating = Rating(rating=row['rating'], movie=movie, rater=rater)

            rating.save()

    # for movie in Movie.objects.values():
    #     mov = Movie.objects.get(movie_id=movie['movie_id'])
    #     rating = Rating.objects.filter(movie_id=movie['movie_id']).aggregate(Avg('rating'))
    #     mov.avg_rating = (rating['rating__avg'])
    #     mov.save()



class Migration(migrations.Migration):

    dependencies = [
        ('movie_lens_online', '0005_auto_20160506_0218'),
    ]

    operations = [
        migrations.RunPython(import_ratings)
    ]