"""
Usage :
-----
import os
import gensim.models.word2vec as w2v

thrones2vec = w2v.Word2Vec.load(os.path.join("trained", "thrones2vec.w2v"))

thrones2vec.most_similar("Stark")
thrones2vec.most_similar("Aerys")
thrones2vec.most_similar("direwolf")

def nearest_similarity_cosmul(start1, end1, end2):
    similarities = thrones2vec.most_similar_cosmul(
        positive=[end2, start1],
        negative=[end1]
    )
    start2 = similarities[0][0]
    print("{start1} is related to {end1}, as {start2} is related to {end2}".format(**locals()))
    return start2

nearest_similarity_cosmul("Stark", "Winterfell", "Riverrun")
nearest_similarity_cosmul("Jaime", "sword", "wine")
nearest_similarity_cosmul("Arya", "Nymeria", "dragons")
"""
# Goal: Create word vectors from a game of thrones dataset and analyse to see semantic similarity

# Step 0 - Import dependecies
from __future__ import absolute_import, division, print_function

# for word encoding
import codecs
# regex
import glob
import re
# concurrency
import multiprocessing
# dealing with OS, like file op
import os
import pprint
# natural language toolkit
import nltk
# word 2 vec
import gensim.models.word2vec as w2v
# dimensionality reduction
import sklearn.manifold
# math
import numpy as np
# plotting
# import matplotlib.pylot as plt
import pandas as pd
# import seaborn as sns

# Step 1 - Process our data
# Clean data

nltk.download('punkt') #pretrained tokenizer
nltk.download('stopwords') #words like and, the, an, a, of

#get book names, matching txt files
book_filenames = sorted(glob.glob('word2vec_data/*.txt'))
print("Found Books:")
print(book_filenames)

# initialize rawunicode
corpus_raw = u""
# open each book, read it, open it in utf 8
# append it to corpus_raw
for book_filename in book_filenames:
	print("Reading '{0}'...".format(book_filename))
	with codecs.open(book_filename, 'r', 'utf-8') as book_file:
		corpus_raw += book_file.read()
	print("Corpus is now {0} characters long".format(len(corpus_raw)))
	print()

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

# tokenize raw data
raw_sentences = tokenizer.tokenize(corpus_raw)

# convert into list of words
# remove unneccesary characters
def sentence_to_wordlist(raw):
	clean = re.sub("[^a-zA-Z]", " ", raw)
	words = clean.split()
	return words

sentences = []
for raw_sentence in raw_sentences:
	if len(raw_sentence) > 0:
		sentences.append(sentence_to_wordlist(raw_sentence))

print(raw_sentences[5])
print(sentences[5])

token_count = sum([len(sentence) for sentence in sentences])
print("The book corpus contains {0} tokens".format(token_count))

# Step 2 build our model
# define hyperparameters

# Dimentionality of the resulting word vector
# More the dimensions, more the training, but vectors are more generalised
num_features = 300

# Min word count threshold
min_word_count = 3

# Number of threads to run in parallel
num_workers = multiprocessing.cpu_count()

# Context windoe length
context_size = 7

# Downsample setting for frequent words
# rate 0 to 1e-3
# how often to use
downsampling = 1e-3

# Seed for random number generation
seed = 1

thrones2vec = w2v.Word2Vec(
	sg=1,
	seed=seed,
	workers=num_workers,
	size=num_features,
	min_count=min_word_count,
	window=context_size,
	sample=downsampling
)

thrones2vec.build_vocab(sentences)

print("Word2Vec vocab length:", len(thrones2vec.wv.vocab))

thrones2vec.train(sentences, total_words=token_count, epochs=100)

if not os.path.exists("trained"):
	os.makedirs("trained")

thrones2vec.save(os.path.join("trained", "thrones2vec.w2v"))


