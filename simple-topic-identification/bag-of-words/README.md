# Bag of Words 

Basic method for finding topics in a text. 
This need  to first create tokens using tokenization. 

```
from nltk.tokenize import word_tokenize
from collections import Counter

Counter(word_tokenize("""Some example in this line. Some phrase in the line."""))

```