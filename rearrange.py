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
    for word in words:
        rand_index = random.randint(0, len(words) - 1)
        scramble_words.append(words[rand_index])
    return set(scramble_words)

if __name__ == '__main__':
    quote = random_python_quote()
    print(quote)

# Manually filter out duplicate words (stretch challenge)
# def random_python_quote():
#     scramble_words_index = []
#     if len(words) == 0:
#         return 'No words were given'
#     while len(scramble_words_index) == len(words):
#         rand_index = random.randint(0, len(words) - 1)
#         scramble_words_index.append(rand_index)
#     return words[rand_index]
