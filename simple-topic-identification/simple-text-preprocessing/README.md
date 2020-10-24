# Simple text preprocessing

## Why preprocessing

- Helps make for better input data:
    - When performing machine learning or other statistical methods. 

## Some examples
- Tokenization to create a bag of words. 
- Lowercasing words.

## Lemmatization/Stemming 
- Shorten words to their root stems. 

--------------------------

# Text preprocessing with Python

```
from ntlk.corpus import stopwords
text = """The cat is in the box. The car likes the box. The box is over the cat."""
tokens = [w for w in word_tokenize(text.lower())
            if w.isalpha()]
no_stops = [t for t in tokens if t not in stopwords.words('english')]
Counter(no_stops).most_common(2)
```

