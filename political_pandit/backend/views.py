from django.shortcuts import render,redirect
from .models import *
from .get_keywords import *
from django.contrib import messages

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

    if request.method=='POST':
        text=request.POST.get('tweet')
        #print(text)
        like=request.POST.get('tweet_id')
        if text:
            
            if profanity(text):
                points=profile.points
                points=points-1
                profile.points=points
                profile.save()

            words=get_keywords(text)
            msg=Tweet(body=text)
            msg.save()
            profile.tweets.add(msg)

            for word in words:
                key,created=Keyword.objects.get_or_create(word=word)
                if created:
                    key.save()
                msg.keyword.add(key)
                profile.keywords.add(key)
            msg.save()
            profile.save()

        if like:
            words=get_keywords(tweet.body)
            for word in words:
                key,created=Keyword.objects.get_or_create(word=word)
                if created:
                    key.save()
                profile.keywords.add(key)
                #print('liked')

    return render(request,'home.html',context)

def quiz(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    this_quiz=None

    for quiz in Quiz.objects.all():
        if profile not in quiz.users.all():
            this_quiz=quiz
            break
    if this_quiz== None:
        messages.error(request,"You have attempted all the quizes")
        return redirect('home')

    if request.method == 'POST':
        for question in this_quiz.questions.all():
            ans = request.POST.get(str(question.query))
            print(str(question.query))
            if ans == question.answer.name:
                points = profile.points
                points += 1
                profile.points = points
                profile.save()
        return redirect('quiz2')
    if this_quiz.id==1:
        return render(request, 'quiz1.html', {'questions': this_quiz.questions.all()})
    else:
        return render(request, 'quiz2.html', {'questions': this_quiz.questions.all()})
    
def quiz2(request):
    return render(request,'quiz2.html')

def home2(request):
    user=request.user
    profile=Profile.objects.get(user=user)

    context={'points':profile.points}
    return render(request,'home2.html',context)

def wheel(request):
    return render(request,'wheel.html')

def task(request):
    return render(request,'task.html')