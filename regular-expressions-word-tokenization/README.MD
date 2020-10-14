# Natural Language Processing

Field of study focused on making sense of language
    - Using statistics and computers

Strings with a special syntax
Allow us to match patterns in other strings
Appliccations of regular expressions

## Common regex patterns 

\w+ -> word
\d -> digit
\s -> space
.* -> wildcard
+ or * -> greedy match
\$ -> not space
[a-z] -> lowercase group

# Tokenization
Turning a string or document into tokens (small chunks).

## nltk library

- ``` nltk ```: natural language toolkit

```
from nltk.tokenize import word_tokenize
word_tokenize("Hello friend")
```

### Other nltk tokenizers

- ``` sent_tokenize ```
- ``` regex_tokenize ```
- ``` TweetTokenizer ```

# Regex groups using or "|"

- OR is represented using ```|```
-You can define a group using ```()```
- You can define explicit character ranges using ```[]```

```
import re
match_digit_word = ('(\d+|\w+)')
re.findall(match_digit_word, 'He is 19 years old')
```