from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.core.mail import send_mail

def create(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            # send_mail('Movie has been created', 'a new movie has been created',
            #           'ghazala@gmail.com', ['receiver@gmail.com'], fail_silently=False
            #           )
            return redirect('movies_list')

    context = {
        'form': form
    }

    return render(request, 'movies/create_movie.html', context)

def details(request,**kwargs):
    id = kwargs.get('id')
    movie = Movie.objects.get(id=id)
    context = {
        'movie': movie
    }

    return render(request, 'movies/movie_details.html', context)

def movies_list(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/movies_list.html', context)

def update(request,**kwargs):
    id = kwargs.get('id')
    movie = Movie.objects.get(id=id)
    form = MovieForm(instance=movie)
    if request.method == 'POST':
        form = MovieForm(data=request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies_list')

    context = {
        'form': form,
        'movie': movie
    }

    return render(request, 'movies/update_movie.html', context)


def delete(request,**kwargs):
    id = kwargs.get('id')
    name = kwargs.get('name')
    Movie.objects.get(id=id).delete()
    messages.success(request, 'Movie {} deleted successfully!'.format(name))
    return redirect('movies_list')

def register(request):
    if request.method=='POST':
        first_name= request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password= request.POST['password']
        password2= request.POST['password2']

        if (password==password2):
            user= User.objects.create_user(username=username, first_name=first_name,last_name=last_name,  email=email, password=password)
            user.save()
            auth.login(request,user)
            return redirect('movies_list')

    return render(request, 'movies/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('movies_list')

    return render(request, 'movies/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('movies_list')

