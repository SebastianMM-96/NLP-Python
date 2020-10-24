![Gensim](https://miro.medium.com/max/700/1*GYEB8J6c5aaMiUgceMp6HQ.jpeg)

# Introduction to Gensim

Gensim is:
- Popular open source NLP library.
- Uses top academic models to perform complex tasks.
    * Building document of word vectors. 
    * Performing topic identification and document comparison.

## Word vector

Some examples of word vector

![example1](https://www.google.com/search?q=word+vector&sxsrf=ALeKk02fv8g1bJo7-IG34nq_JMuoGz2WDA:1603564837632&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiAtJXE8M3sAhUBXKwKHRWyCNMQ_AUoAXoECAYQAw&biw=1920&bih=937#imgrc=PI3w_qltVFUwSM)

![example2](https://developers.google.com/machine-learning/crash-course/images/linear-relationships.svg)

## Example using Gensim

```
from gensim.corpora.dictionary import Dictionary
from nltk.tokenize import word_tokenize
my_document = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
              'Praesent ullamcorper dolor metus, non porttitor ligula imperdiet vel.',
              'Sed turpis diam, scelerisque non turpis eget, pharetra sagittis ligula.',
              'Duis egestas, elit sit amet imperdiet lobortis, enim lectus finibus felis',]
```

```
tokenized_docs = [word_tokenize(doc.lower())
                for doc in my_documents]
dictionary = Dictionary(tokenized_docs)
dictionary.token2id
```

## Gensim corpus

```
corpus = [dictionary.doc2bow(doc) for doc in tokenized_docs]
```

- ```gensim``` models can be easily saved, updated, and reused. 
- Our dictionary can also be updated.
