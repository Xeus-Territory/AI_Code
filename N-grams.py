# Text = "I am learning NLP"
# #Import textblob
# from textblob import TextBlob
# #For unigram : Use n = 1

# print("unique prams: ")
# print(TextBlob(Text).ngrams(1))

# print("bigrams: ")
# print(TextBlob(Text).ngrams(2))

#importing the function
from sklearn.feature_extraction.text import CountVectorizer
# Text
text = ["I love NLP and I will learn NLP in 2month "]
# create the transform
vectorizer = CountVectorizer(ngram_range=(2,2))
# tokenizing
vectorizer.fit(text)
# encode document
vector = vectorizer.transform(text)
# summarize & generating output
print(vectorizer.vocabulary_)
print(vector.toarray())


