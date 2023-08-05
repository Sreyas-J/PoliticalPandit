import nltk
from nltk.stem import PorterStemmer
from rake_nltk import Rake
from .models import *

nltk.download('stopwords')
nltk.download('punkt')

def getKeywordDB(post):
    tweet=Tweet.objects.get(keywords=post)
    return tweet.keywords

def get_keywords(text):
    ps = PorterStemmer()
    rake_nltk_var = Rake()
    rake_nltk_var.extract_keywords_from_text(text)
    phrases = rake_nltk_var.get_ranked_phrases()
    words = []

    for phrase in phrases:
        for word in phrase.split():
            words.append(ps.stem(word))

    return words

def sort_recommendations(posts, keywords):
    num_matches = {}

    for post in posts:
        count = 0
        for word in post: 
            if word in keywords: count += 1

        num_matches[tuple(post)] = count

    posts.sort(reverse = True, key = lambda x : num_matches[tuple(x)])