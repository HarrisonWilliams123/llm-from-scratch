"""
I learned there are multiple methods for tokenization.

1. Character Level: Break the words down into individual letters
    Ex: "dog" becomes d, o, g 
2. Word Level: Split text by spaces into whole words
    Ex: "the dog sat on a mat" becomes the, dog, sat, on, a, mat
3. Subword level: Using algorithms like Byte-Pair Encoding (which I'm using in this script)
    to split common words and keep rare words flexible.
"""
class Tokenizer():
    pass