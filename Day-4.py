import nltk

from nltk.tokenize import sent_tokenize,word_tokenize

text=" Analytics & Data science is a new function and field for Hugh & Crye, and we are excited to build our team with our first hire. Our business contains an enormous amount of data, all untapped."
#Sentences from the text created above
print(sent_tokenize(text))

#Words from the text created above
print(word_tokenize(text))

from nltk.corpus import stopwords
stop=list(stopwords.words('English'))


#stop=list(stop)
stop.append(',')
stop.append('.')

print(stop)

w=word_tokenize(text)
#Gives me the words which are not in stop list and stores in the clean_text
clean_text=[i for i in w if not i in stop]
print(clean_text)        

        #or
        
clean_text2=[]
for i in w:
    if i not in stop:
        clean_text2.append(i)
print(clean_text2)        
        
print(stop)
print(w)


#Stpowords list also comes with French
stop2=set(stopwords.words('French'))
print(stop2)


#Stemming
from nltk.stem import PorterStemmer 

ps=PorterStemmer()
#Stem from words
ps.stem('updating')
ps.stem('flying')
ps.stem('Loving')

for i in w:
    print(ps.stem(i))

for i in clean_text2:
    print(ps.stem(i))
        
    
#Lemmatize and stem are one and the same
from nltk.stem import WordNetLemmatizer 
lemmatizer=WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("ringing"))
print(lemmatizer.lemmatize("better",pos="a"))
print(lemmatizer.lemmatize("best",pos="a"))

#WordNet is a NLTK dictionary

from nltk.corpus import wordnet 

#Finding synonym
syns=wordnet.synsets("good")
print(syns)
for i in syns:
    print(i.lemmas())

print(syns[5].name())
print(syns[5].lemmas())
print(syns[1].definition())
print(syns[8].definition())
print(syns[5].examples())



#Finding synonym
syns=wordnet.synsets("pretty")
print(syns)


print(syns[1].definition())
print(syns[2].lemmas())

print(syns[8].definition())
print(syns[0].examples())

#Creating the antonyms and synonyms using lemmas()
synonyms=[]
antonyms=[]

for syn in wordnet.synsets("pretty"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
            
print("Synonyms for pretty are :",set(synonyms))   
print("Antonyms for pretty are :",set(antonyms))            
         

file=open("C:/Users/Naveen/Desktop/Questions from Avisek Kundu.txt",'r')
file.readlines()
f=file.readline(2)
f

#Requesting to internet
import requests
f_online='http://www.gutenberg.org/11111/11111.txt'
f_rawtext=requests.get(f_online).text

print(f_rawtext)


from nltk.corpus import gutenberg
textguten=gutenberg.raw("bible-kjv.txt")

print(textguten)
len(textguten)

from nltk.book import *

text1.concordance("monstrous")
text2.concordance("affection")

text1.similar('monstrous')
text2.similar('monstrous')



text1.common_contexts(['monstrous','very'])

text4.dispersion_plot(["citizens","democracy","freedom","duties","America"])

text3.count("Adam")
print("Length of Text:"+str(len(text3)))

set(text4)
print(set(text4))

len(text4)
len(set(text4))

sorted(set(text))
print("Length of Token:"+str(len(set(text3))))


#To find the lexical richness
#Finds the ratio of no of unique words to no of total words in a list
def fn(text):
    return (len(set(text))/len(text))

text2="hi How are You ji hi"
text2=word_tokenize(text2)
fn(text2)


#Occurances /length of the text
def fn2(text,word):
    return (text.count(word)/len(text))*100

#2/6=33.33%
fn2(text,'hi')
#1/6=16.66
fn2(text,'How')


#Used for classifying the documents(eg:- sports,national news)
#Gives the word with corresponding frequency
fdist=FreqDist(text1)
fdist
print(fdist)

len(fdist)
len(text1)

fdist.most_common(50)

fdist.plot(50,cumulative=True)


fdist.most_common(4)

fdist.plot(4,cumulative=True)


nltk.corpus.gutenberg.fileids()
emma=nltk.corpus.gutenberg.words('austen-emma.txt')
emma=nltk.Text(emma)
emma.concordance("surprize")


#to find the files
nltk.corpus.state_union.fileids()


#tagging
text="hi How are You ji hi"
w=word_tokenize(text)



import requests
f_online='http://www.gutenberg.org/11111/11111.txt'
f_rawtext=requests.get(f_online).text
print(f_rawtext)

raw_words=word_tokenize(f_rawtext[:100])

tags=nltk.pos_tag(raw_words,tagset='universal')
print(tags[:10])





from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
traind = state_union.raw("2005-GWBush.txt")
testd = state_union.raw("2006-GWBush.txt")
    
custom_sent_tokenizer = PunktSentenceTokenizer(traind)
tokenized = custom_sent_tokenizer.tokenize(testd)
def text_processing():
    try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            chunkGram = r"""Chunk:{<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkParser=nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            
            print(chunked)
            
            for subtree in chunked.subtrees():
                print(subtree)
            chunked.draw()   
    except Exception as e:
        print(str(e))
text_processing()  
















