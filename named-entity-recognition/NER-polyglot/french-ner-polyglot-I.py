# Create a new text object using Polyglot's Text class: txt
import polyglot
from polyglot.text import Text
txt = Text(article)

# Print each of the entities found
for ent in txt.entities:
    print(ent)
    
# Print the type of ent
print(type(ent))