from django.shortcuts import render
from .models import *
from .get_keywords import *

def home(request):
    tweets = Tweet.objects.all()
    post_lists = [[keyword.word for keyword in tweet.keyword.all()] for tweet in tweets]
    new_tweets=[]
    
    user=request.user
    profile=Profile.objects.get(user=user)
    keyword_words = [keyword.word for keyword in profile.keywords.all()]
    sort_recommendations(post_lists,keyword_words)

    matching_tweets = Tweet.objects.filter(keyword__word__in=keyword_words)

    # Exclude visited tweets
    not_visited_tweets = []
    for tweet in matching_tweets:
        if tweet not in profile.visited.all():
            not_visited_tweets.append(tweet)
            profile.visited.add(tweet)
            
    if not_visited_tweets:
        context = {'tweets': not_visited_tweets}
    else:
        for tweet in tweets:
            new_tweets.append(tweet)
            profile.visited.add(tweet)
        context={'tweets':new_tweets}

    return render(request,'home.html',context)