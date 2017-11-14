import random
import sys
import re
import string

def get_clean_data(raw_data):
    '''
    raw_data: String
    Function cleans raw_data from punctuations, numbers, spaces etc, to only leave words
    Returns list
    '''

    crowd_reaction_removed = re.sub('\(\w*\)', '', raw_data)

    crowd_reaction_removed = re.sub('\(\w*\s\w*\)', '', crowd_reaction_removed)

    numbers_removed = re.sub('\d\w*', '', crowd_reaction_removed)

    punctuationless_data = ''.join([char for char in numbers_removed
                                    if char not in string.punctuation])# Removes punctuation from data

    clean_data = re.split('\s*', punctuationless_data)[:-1]  # Splits data based on whitespace

    return clean_data

def get_random_word(histogram):
    '''
    Histogram: Key Value pair. Key: String, Value: Int
    Returns a single word at random
    '''
    # {
        # 'fish': {'one': 1, 'red: 2'},
        # 'red': {'fish': 1, 'one': 2}
    # }

    rand_num = random.random()

    cummulitive_wght = 0

    for key, value in histogram.items():

        word_likelyhood_percent = value / sum(histogram.values())

        cummulitive_wght += word_likelyhood_percent

        if rand_num <= cummulitive_wght:
            random_word = key
            break



    # print('----------random number:', rand_num)
    # print('\n')
    # print('----------Final result------------')
    # print('\n')
    # print('----------cummulitive_wght:', cummulitive_wght)
    # print('\n')
    # print('----------random number:', rand_num)
    # print('\n')
    # print('----------random word:', random_word)
    # print()
    return random_word
'''
One solution to iterate through nested dictionaries
stop = ''
for outer_key, outer_value in histogram.items():
    if stop == True:
        break
    for inner_key, inner_value in outer_value.items():
        word_likelyhood_percent = inner_value / sum(outer_value.values())

        cummulitive_wght += word_likelyhood_percent

        print('----------cummulitive_wght:', cummulitive_wght)
        if rand_num <= cummulitive_wght:
            random_word = inner_key
            stop = True
            break
        '''

def sentence_generator(num_words_in_sentence, histogram):
    '''
    Num_words_in_sentence: Int
    Histogram: Key Value pair. Key: String | Value: Int
    Function generates a sentence from a source text
    Returns a string
    '''
    sentence = ''

    counter = 0

    list_of_words = list(histogram)

    starting_word = random.choice(list_of_words)

    while counter != num_words_in_sentence:

        rand_word = get_random_word(histogram[starting_word])

        sentence += rand_word + ' '

        starting_word = rand_word

        counter += 1

    return sentence.strip().capitalize()

def get_histogram(word_list):
    result = {}
    for index, word in enumerate(word_list):
        try:
            next_word = word_list[index + 1]
        except:
            break

        if word not in result:

            result[word] = {next_word: 1}

        else:
            # {
                # 'fish': {'one': 1, 'red: 2'},
                # 'red': {'fish': 1, 'one': 2}
            # }

            if next_word not in result[word]:
                result[word].update({next_word: 1})
            else:
                 result[word][next_word] += 1
    return result

if __name__=='__main__':
    with open('obama_speech.txt') as file:

        raw_data = file.read().lower()

    clean_data = get_clean_data(raw_data)
    histogram = get_histogram(clean_data)
    print(sentence_generator(10, histogram))

    # histogram = {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}
    # histogram = {'one': {'fish': 1}, 'fish': {'two': 1, 'red': 1, 'blue': 1}, 'two': {'fish': 1}, 'red': {'fish': 1}, 'blue': {'fish': 1}}

'''
# -----------------------------------------

# Final format of how we want our histogram to be modeled
# Follow this format
{
    'one': {'fish': 1},
    'fish': {'blue': 1, 'red': 1, 'two': 1},
    'blue': {'fish': 1},
    'two': {'fish': 1},
    'red': {'fish': 1}
}


# List of words
['one', 'fish', 'blue', 'fish', 'red', 'fish', 'two', 'fish']

# Step 1) Get a word
# Step 2) Get the word that comes after
# Step 3) Store word as a key in dictionary
# Step 4) Store the word that comes after as a VALUE
# Step 5) If word that comes after already in nested dictionary increment by 1

def get_histogram(list_of_words):
    #Converts a list of words into a markov chain

    histogram = {}
    # Step 1
    for index, word in enumerate(list_of_words): # enumerate allows you to iterate through index AND value
        # index: 0
        # word: one

        # Step 2
        word_that_comes_after = list_of_words[index + 1] # fish

        # step 3
        if word_that_comes_after not in histogram[word]:

            # step 4
            histogram[word] = {word_that_comes_after: 1}

        else:
            # step 5
            histogram[word][word_that_comes_after] += 1

histogram[word] >> {'fish': 1}

histogram[word][word_that_comes_after] >> 1

'one': {'fish': 1}
'''
