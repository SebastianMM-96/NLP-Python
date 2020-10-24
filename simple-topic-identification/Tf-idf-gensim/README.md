![Gensim](https://miro.medium.com/max/700/1*GYEB8J6c5aaMiUgceMp6HQ.jpeg)

# Tf-idf with gensim

Tf-idf is a term frequency - inverse document frequency.

Allows you to determine the most important words in each document. 

Each corpus may have shared words beyond just stopwords. These words should be down-weighted in importance. 

Ensures most common words don't show up as key words. Keeps document specific frequent words weighted high.

## Tf-idf formula

<a href="https://www.codecogs.com/eqnedit.php?latex=w_{i,j}&space;=&space;t&space;f_{i,j}&space;\cdot&space;\log(\frac{N}{df_{i}})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?w_{i,j}&space;=&space;t&space;f_{i,j}&space;\cdot&space;\log(\frac{N}{df_{i}})" title="w_{i,j} = t f_{i,j} \cdot \log(\frac{N}{df_{i}})" /></a>

## Tf-idf with gensim

```
from gensim.models.tfidfmodel import TfidfModel
tfidf = TfidfModel(corpus)
tfidf[corpus[1]]
```