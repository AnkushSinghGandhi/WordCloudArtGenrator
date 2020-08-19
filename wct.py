from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

# opening file

fileName = input("Please enter text file name: ")
with open(fileName, 'r') as file:
    text = file.read().replace('\n', ' ')

# we convert the text into lowercase. We then define a set of stopwords that are to be ignored in the wordcloud. STOPWORDS comes with the wordcloud module, we can add custom stopwords via the update() method of set.

# turn to lowercase
text = text.lower()

# define words that are to be ignored in the word cloud
stopwords = set(STOPWORDS)
# stopwords.update([ ])

# we tokenize the text into a list of individual words. To normalize these words for the wordcloud, we tag them with their part-of-speech (e.g., verb, noun) and convert the words back to their original form based on these tags. E.g., “databases” becomes “database”, “developed” becomes “develop”. Finally, we merge these lemmatized words into a string, which is to be fed to the word cloud generator

# tokenize into words
words = word_tokenize(text)

# pos tagging
tags = nltk.pos_tag(words)

# lemmatization
lem = WordNetLemmatizer()
lemWords = []
for i in range(len(words)):
    word = words[i]
    tag = tags[i][1]
    if 'VB' in tag:
        lemWord = lem.lemmatize(word, "v")
    elif tag == "PRP":
        lemWord = word
    else:
        lemWord = lem.lemmatize(word)
    lemWords.append(lemWord)

finalText = ' '.join(lemWords)

w = int(input("Width: "))
h = int(input("Height: "))


