import numpy as np
import sys

#Creates a seed for reproducibility
np.random.seed(1234)

#Used the words from AlgoMonster for the vocab because I couldn't come with other words to use
vocab = ['the', 'cat', 'dog', 'sat', 'ran', 'on', 'mat', 'house', 'a', 'big',
        'small', 'quickly', 'slowly', 'and', 'is', 'red', 'blue', 'to',
        'PAD', 'END']

#Capturing the prompt that the user will send
prompt = input("Enter your sentence: ").lower()

#Method for making sure the input is valid
def input_validation(prompt):
    #Checking to see if the sentence is in vocab
    sentence = prompt.split()
    for word in sentence:
        if word not in vocab:
            print("One word is not in the vocabulary for the llm.")
            sys.exit()


def main():
    input_validation(prompt)

if __name__ == "__main__":
    main()
