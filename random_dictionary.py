import random
import sys

def rand_sentence(word_count, words):
    new_sentence = ''
    for n in range(word_count):
        new_sentence += random.choice(words)[:-1] + ' '
    return new_sentence[:-1]

def main():
    try:
        word_count = int(sys.argv[1])
    except:
        return 'Please enter a correct number'

    with open('/usr/share/dict/words') as file:
        words = file.readlines()

    return rand_sentence(word_count, words)



if __name__=='__main__':
    print(main())
