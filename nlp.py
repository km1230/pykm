import nltk
syn = nltk.corpus.wordnet.synsets("hello")
print(syn[0].definition())
