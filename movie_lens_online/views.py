from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.shortcuts import redirect

from .models import Rater, Movie, Rating


def index(request):

    top_twenty_list = Movie.objects.order_by('-avg_rating')[:20]

    context = {'top_twenty_list': top_twenty_list}

    return render(request, 'movies/index.html', context)

def top_twenty(request):
    return HttpResponse("Hello, world. You're at the top twenty view.")

def users(request):
    return HttpResponse("Hello, world. You're at the users view.")

def movie(request, movie_id):

    rating_list = Rating.objects.filter(movie_id=movie_id)
    grabber = (Movie.objects.get(movie_id=movie_id))
    name_finder = grabber.movie_title
    avg_rating = round(grabber.avg_rating, 2)
    #avg_rating = grabber.avg_rating

    context = {'rating_list': rating_list, 'movie_id': movie_id,
                'name_finder': name_finder, 'avg_rating': avg_rating}

    return render(request, 'movies/movie.html', context)

    # return HttpResponse('{}'.format((Movie.objects.get(movie_id=movie_id).movie_title)))

def raterer(request, user_id):
    rated_movies_list = Rating.objects.filter(rater_id=user_id)
    #grabber_2 =

    grabber = (Rater.objects.get(user_id=user_id))
    #
    # mov = Movie.objects.get(movie_id=movie['movie_id'])
    # rated_movies_title = Movie.objects.filter(movie_id=user_id)
    #
    age = grabber.age
    sex = grabber.sex
    occupation = grabber.occupation

    #movie_title = Movie.objects.get(movie_id=movie_id)
    context = {'rated_movies_list': rated_movies_list, 'user_id': user_id,
    'age':age, 'sex':sex, 'occupation': occupation}

    return render(request, 'movies/raterer.html', context)


def login_user(request):
    state = "Please log in below..."
    username = password = ''

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(username=username, password=password)
        print(request.POST)


        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                return redirect('add_rating')

            else:
                state = "Your account is not active, please contact the site admin."
                return redirect('movie')
        else:
            state = "Your username and/or password were incorrect."
            return redirect('movie')

    context = {'state':state, 'username': username}
    return render(request, 'movies/auth.html', {'state':state, 'username': username})


def add_rating(request):
    #print(dir(request))
    print(dir(request.POST))
    #print(request.POST.path)
    # print(request.POST and request.POST['Add_Rating'] == 'Add Rating')
    print(request.POST.get('Add_Rating', False))
    print (request.POST.get('movie', False))
    print(request.POST.values)

    if request.POST.get('Add_Rating', False) and request.POST.get('movie', False):


            movie_id = request.POST['movie']

            user_rating = request.POST['rating']

            user_id = request.user.id

            rater = Rater.objects.get(user_id=user_id)

            movie = Movie.objects.get(movie_id=movie_id)

            rating = Rating(rater=rater, rating=user_rating, movie=movie)

            rating.save()

    elif request.POST.get('Exit', False):
        return redirect('index')

    elif request.POST.get('username', True):

            context = {'movies': Movie.objects.all()}
            return render(request, 'movies/add_rating.html', context)


    context = {'movies': Movie.objects.all()}
    return render(request, 'movies/add_rating.html', context)
