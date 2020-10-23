from nltk.tokenize import word_tokenize
from collections import Counter

Counter(word_tokenize("""The cat is in the box. The cat box."""))