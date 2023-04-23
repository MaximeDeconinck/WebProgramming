from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import Http404
from django.db.models import Avg, Count
from streaming.models import Movie
from .models import UserProfile, SubscriptionPlan

# Create your views here.
def index(request):
    movies = Movie.objects.all().annotate(avg_rating = Avg('reviews__rating'), num_ratings=Count('reviews')).order_by('-avg_rating')
    context = {'movies': movies}
    return render(request, 'streaming/index.html', context)

def movie(request, movie_id):
    try:
        print(Movie.objects.get(pk=movie_id))
        movie = Movie.objects.get(pk=movie_id)
        return render(request, 'streaming/movie.html', {'movie': movie})
    except ObjectDoesNotExist:
        raise Http404('Movie not found')

def user_reviews(request, id):
    user_profile = UserProfile.objects.get(id=id)
    reviews = user_profile.reviews.all()
    context = {'user_profile': user_profile, 'reviews': reviews}
    return render(request, 'streaming/user_reviews.html', context)

def subscription_plan(request, subscription_id):
    subscription = SubscriptionPlan.objects.get(id=subscription_id)
    movies = subscription.movies.all()
    context = {'subscription': subscription, 'movies': movies}
    return render(request, 'streaming/subscription_plan.html', context)