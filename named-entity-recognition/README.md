# Named entity recognition

NLP task to identify important named entities in the text:
    - People, places, organizations.
    - Dates, states, works of art
    - and other categories

## Example of NER 

![example](https://miro.medium.com/max/700/1*9ICjpdIPiocUWC5oF47duw.png)

## nltk and Stanford CoreNLP library 

- The Stanford CoreNLP library:
    - Integrated into Python via ```nltk```
    - Java based
    - Support for NER as well as coreference and dependency trees

## Using nltk for NER

```
import nltk

sentence = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'''

tokenized_sent = nltk.word_tokenize(sentence)
tagged_sent = nltk.pos_tag(tokenized_sent)
tagged_sent[:3]

print(nltk.ne_chunk(tagged_sent))

```