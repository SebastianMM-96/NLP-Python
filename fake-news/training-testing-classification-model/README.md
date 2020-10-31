# NaiveBayes classifier

```
from sklearn.naive_bayes import MultinomialNB
from sklearn import metric
snb_classifier = MultinomialNB()

nb_classifier.fit(count_train, y_train)
# test accuracy
pred = nb_classifier.predict(count_test)
# measure the accuracy
metrics.accuracy_score(y_test, pred)
```

## Confusion Matrix 

```
metrics.confusion_matrix(y_test, pred, labels=[0,1])
```