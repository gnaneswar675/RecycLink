#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recyclinkproj.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()



-------------------------------------------    1
import numpy as np

print("NumPy version:", np.__version__)

a = np.array([1, 2, 3, 4, 5])

b = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

c = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("\n1D Array:")
print(a)

print("\n2D Array:")
print(b)

print("\n3D Array:")
print(c)

print("\nDimensions of b:", b.ndim)
print("Shape of b:", b.shape)
print("Data type of b:", b.dtype)
print("Total elements in b:", b.size)

print("\nFirst row of 2D array:", b[0])
print("Element at position (1,2):", b[1, 2])
print("First two elements of 1D array:", a[:2])

x = np.array([
    [1, 2],
    [3, 4]
])

y = np.array([
    [5, 6],
    [7, 8]
])

print("\nMatrix x:")
print(x)

print("\nMatrix y:")
print(y)

print("\nMatrix Addition:")
print(x + y)

print("\nMatrix Subtraction:")
print(x - y)

print("\nMatrix Multiplication:")
print(np.dot(x, y))

print("\nTranspose of x:")
print(x.T)

print("\nInverse of x:")
print(np.linalg.inv(x))

arr = np.array([1, 4, 9, 16, 25])

print("\nArray for Mathematical Functions:")
print(arr)

print("\nSquare Roots:")
print(np.sqrt(arr))

print("\nExponential Values:")
print(np.exp(arr))

print("\nSine Values:")
print(np.sin(arr))

print("\nMean:")
print(np.mean(arr))

print("\nStandard Deviation:")
print(np.std(arr))



-------------------------------       1 output


NumPy version: 1.24.3

1D Array:
[1 2 3 4 5]

2D Array:
[[1 2 3]
 [4 5 6]]

3D Array:
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]

Dimensions of b: 2
Shape of b: (2, 3)
Data type of b: int32
Total elements in b: 6

First row of 2D array: [1 2 3]
Element at position (1,2): 6
First two elements of 1D array: [1 2]

Matrix x:
[[1 2]
 [3 4]]

Matrix y:
[[5 6]
 [7 8]]

Matrix Addition:
[[ 6  8]
 [10 12]]

Matrix Subtraction:
[[-4 -4]
 [-4 -4]]

Matrix Multiplication:
[[19 22]
 [43 50]]

Transpose of x:
[[1 3]
 [2 4]]

Inverse of x:
[[-2.   1. ]
 [ 1.5 -0.5]]

Array for Mathematical Functions:
[ 1  4  9 16 25]

Square Roots:
[1. 2. 3. 4. 5.]

Exponential Values:
[2.71828183e+00 5.45981500e+01 8.10308393e+03
 8.88611052e+06 7.20048993e+10]

Sine Values:
[ 0.84147098 -0.7568025   0.41211849 -0.28790332 -0.13235175]

Mean:
11.0

Standard Deviation:
8.648699324175862


----------------------------------------------------          10 

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger_eng')

text = "Artificial Intelligence is transforming the world. NLP is a branch of AI."

sentences = sent_tokenize(text)

print("\n----- Sentence Segmentation -----")
for i, sentence in enumerate(sentences, 1):
    print(f"{i}: {sentence}")

words = word_tokenize(text)

print("\n----- Word Tokenization -----")
print(words)

ps = PorterStemmer()
stem_words = [ps.stem(word) for word in words]

print("\n----- Stemming -----")
for original, stem in zip(words, stem_words):
    print(f"{original}  -->  {stem}")

lm = WordNetLemmatizer()
lemma_words = [lm.lemmatize(word) for word in words]

print("\n----- Lemmatization -----")
for original, lemma in zip(words, lemma_words):
    print(f"{original}  -->  {lemma}")



----------------------------------------------------  10 output


----- Sentence Segmentation -----
1: Artificial Intelligence is transforming the world.
2: NLP is a branch of AI.

----- Word Tokenization -----
['Artificial', 'Intelligence', 'is', 'transforming', 'the', 'world', '.', 'NLP', 'is', 'a', 'branch', 'of', 'AI', '.']

----- Stemming -----
Artificial  -->  artifici
Intelligence  -->  intellig
is  -->  is
transforming  -->  transform
the  -->  the
world  -->  world
.  -->  .
NLP  -->  nlp
is  -->  is
a  -->  a
branch  -->  branch
of  -->  of
AI  -->  ai
.  -->  .

----- Lemmatization -----
Artificial  -->  Artificial
Intelligence  -->  Intelligence
is  -->  is
transforming  -->  transforming
the  -->  the
world  -->  world
.  -->  .
NLP  -->  NLP
is  -->  is
a  -->  a
branch  -->  branch
of  -->  of
AI  -->  AI
.  -->  .
[nltk_data] Downloading package punkt to /root/nltk_data...
[nltk_data]   Package punkt is already up-to-date!
[nltk_data] Downloading package punkt_tab to /root/nltk_data...
[nltk_data]   Package punkt_tab is already up-to-date!
[nltk_data] Downloading package wordnet to /root/nltk_data...
[nltk_data]   Package wordnet is already up-to-date!
[nltk_data] Downloading package averaged_perceptron_tagger_eng to
[nltk_data]     /root/nltk_data...
[nltk_data]   Package averaged_perceptron_tagger_eng is already up-to-
[nltk_data]       date!
