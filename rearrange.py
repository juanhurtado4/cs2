import sys
import random

words = sys.argv[1:] # Command line arguments

def random_python_quote():
    '''
    Functions scrambles the order of the elements in the list "words"
    Returns a set of strings which is a scrambled version of words list.
    '''
    scramble_words = []
    if len(words) == 0:
        return 'No words were given'
    while len(words) > 0:
        rand_index = random.randint(0, len(words) - 1)
        scramble_words.append(words.pop(rand_index))
    return scramble_words

if __name__ == '__main__':
    quote = random_python_quote()
    print(quote)
