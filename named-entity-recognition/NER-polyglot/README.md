![image1](https://miro.medium.com/max/3840/1*DJQm-jjYwAzBB6X1uxSQog.jpeg)

# Multilingual NER with polyglot

NLP library which uses word vectors. 

```polyglot```
    - Vectors for many different languages
    - More than 130

![image2](https://miro.medium.com/max/5464/1*781JyRk6NKHi6SaiWPNmqg.png)

## Example

```
from polyglot.text import Text

text = """La Fiscalía capitalina lo investiga por no declarar todos los inmuebles que tiene; en la vivienda cateada el miércoles vive la hija de quien fuera la mano derecha del exjefe de Gobierno."""

ptext = Text(text)
ptext.entities

```