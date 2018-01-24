#Day-5
import random
import nltk
from nltk.corpus import movie_reviews

#nltk.corpus.movie_reviews.fileids()

#list Comprehension
#For each file , token them into words
#For 2000 files check the documents in variable explorer
documents= [(list(movie_reviews.words(fileid)),category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]    


random.shuffle(documents)

all_words=[]
for w in movie_reviews.words():
    all_words.append(w.lower())
    
all_words=nltk.FreqDist(all_words)
print(all_words.most_common(15))  
print(all_words["stupid"]) 



word_features=list(all_words.keys())[:3000]


def find_features(document):
    words=set(document)
    features={}
    for w in word_features:
        features[w]=(w in words)
        
    return features

featuresets=[(find_features(rev),category) for (rev,category) in documents]  



#Classification using Naive bayes

#Creating the training set and testing set out of featuresets

train_set=featuresets[:1900]
test_set=featuresets[1900:]


#Train the classifier
classifier=nltk.NaiveBayesClassifier.train(train_set)

print("Classifier accuracy percent",(nltk.classify.accuracy(classifier,test_set))*100)



























