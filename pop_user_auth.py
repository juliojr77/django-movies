from django.contrib.auth.models import User
from movie_lens_online.models import Rater, Movie, Rating

for rat in Rater.objects.all():
    user1 = User.objects.create_user(username=rat.user_id, 'fakeemail@gmail.com','password')
    user1.save()
    rat['auth_u_id'] = user1
    rat.save()
