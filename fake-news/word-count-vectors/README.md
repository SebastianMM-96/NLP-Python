# Building word count vectors with scikit-learn

- Dataset consisting of movie plots and corresponding genre. 
- GOAL: Create a bag-of-word vector for the movie plots. 

## Count vectorizer with Python

```
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

df = # Load data
y  = df['Sci-Fi']
X_train, X_test, y_train, y_test = train_test_split(
    df['plot'], y, test_size=0.33, random_state=53)

count_vectorizer = CountVectorizer(stop_words='english')
count_train = count_vectorizer.fit_transform(X_train.values)
count_test = count_vectorizer.transform(X_test.values) 
```