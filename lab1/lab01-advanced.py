#!/usr/bin/python

from __future__ import print_function, division
from string import punctuation
from math import sqrt
from collections import Counter


def t_test(c1, c2, c12, N):
    # simplified t-test in terms of raw counts
    return (c12 - c1 * c2 / N) / sqrt(c12)

text = open('data/pandp12.txt', 'rU').read()
# replace emdash "--" with spaces to separate words
# add space before possessive "'s" to match Penn Treebank tokenization
text = text.replace('--', ' ').replace("'s", " 's")

# split words, strip punctuation, and remove empty strings
words = list(filter(None, [w.strip(punctuation) for w in text.split()]))

nwords = len(words)
unigrams = Counter(words)
bigrams = Counter(zip(words, words[1:]))

for w1, w2 in bigrams:
    bigrams[w1, w2] = t_test(unigrams[w1], unigrams[w2], bigrams[w1, w2], nwords)

for (w1, w2), score in bigrams.most_common(100):
    print(score, w1, w2)
