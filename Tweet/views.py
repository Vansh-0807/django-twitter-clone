from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# importing models
from .models import Tweet

from django.db.models import Q

# importing forms
from .forms import TweetForm, UserRegisteratonForm

from django.shortcuts import get_object_or_404, redirect #it is an ORM which is used for interacting with the database 

# Create your views here.

def index(request):
    return render(request, 'Tweet/index.html')

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'Tweet/tweet_list.html', {'tweets' : tweets})

@login_required #added decorator to ensure user is logged in
def tweet_create(request):
    if request.method == "POST":
        #request.POST contains text files, whereas request.FILES contains uploaded files like images, audio etc.
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit = False) #commit=False allows to make changes before final save 
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'Tweet/tweet_form.html', {'form': form})     

# edit tweet
@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk= tweet_id, user = request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance = tweet)
        if form.is_valid():
            tweet = form.save(commit = False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'Tweet/tweet_edit.html', {'form' : form})

# delete user
@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk = tweet_id, user = request.user) #get_object_or_404 is used for retrieving existing data from the database
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'Tweet/tweet_confirm_delete.html', {"tweet" : tweet})

def register(request):
    if request.method == 'POST':
        form = UserRegisteratonForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRegisteratonForm()
    return render(request, 'registration/register.html', {'form' : form})

def search(request):
    query = request.GET.get('q')

    # retrieving all tweets
    tweets = Tweet.objects.all().order_by('-created_at')

    # if there's a search query, filter the results
    if query:
        tweets = tweets.filter(
            Q(text__icontains=query) |
            Q(user__username__icontains=query)
        )
    # render them
    return render(request, 'Tweet/tweet_list.html', {
        'tweets' : tweets,
        'query' : query
    })