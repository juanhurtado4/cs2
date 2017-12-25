from helper_markov_sentence_generator import remove_empty_string, get_first_token, get_clean_data_strt_end
import random
import sys
import re
import string

# TODO: Get all starting tokens
# TODO: Get all ending tokens


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

    rand_num = random.random()

    cummulitive_wght = 0

    for key, value in histogram.items():

        word_probability = value / sum(histogram.values())

        cummulitive_wght += word_probability

        if rand_num <= cummulitive_wght:
            random_word = key
            break



    return random_word

def sentence_generator(num_words_in_sentence, histogram):
    '''
    Num_words_in_sentence: Int
    Histogram: Key Value pair. Key: String | Value: Int
    Function generates a sentence from a markov_chain
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

def get_starting_token_histogram(raw_data):
    split_data = raw_data.split('.')
    remove_empty_string(split_data)
    # import pdb; pdb.set_trace()
    starting_tokens = [get_first_token(sentence) for sentence in split_data]
    return set(starting_tokens)


def get_histogram(word_list):
    # result = {}
    # for index, word in enumerate(word_list):
    #     try:
    #         next_word = word_list[index + 1]
    #     except:
    #         break

    #     if word not in result:

    #         result[word] = {next_word: 1}

    #     else:

    #         if next_word not in result[word]:

    #             result[word].update({next_word: 1})

    #         else:
    #              result[word][next_word] += 1
    # return result

    # def get_histogram(word_list):
    
    # Second order markov chain implemented below
    result = {}
    for index, word in enumerate(word_list):
        try:
            next_word = word_list[index + 1]
            after_next = word_list[index + 2]
            next_state = next_word + ' ' + after_next
        except:
            break

        if word not in result:

            result[word] = {next_state: 1}  # Implement as tuple or string

        else:

            if next_state not in result[word]:

                result[word].update({next_state: 1})

            else:
                 result[word][next_state] += 1
    print(result)
    return result

def test_frequency():
    '''
    Function test sentence generator
    '''
    from dictionary_histogram import get_histogram as test

    markov_chain = {'one': {'fish': 1}, 'fish': {'two': 1, 'red': 1, 'blue': 2}, 'two': {'fish': 1}, 'red': {'fish': 1}, 'blue': {'fish': 1}}

    # list_of_words = get_clean_data(sentence_generator(1000, markov_chain))
    list_of_words = sentence_generator(1000, markov_chain).lower().split(' ')

    histogram = test(list_of_words)

    return histogram

if __name__=='__main__':
    with open('second_order_testing/short_version_obama_speech.txt') as file:
    # with open('one_fish_text.txt') as file:

        raw_data = file.read().lower()


    clean_data = get_clean_data_strt_end(raw_data)
    starting_tokens = get_starting_token_histogram(clean_data)
    print(starting_tokens)

    # uncomment when finish debugging
    # clean_data = get_clean_data(raw_data)
    # histogram = get_histogram(clean_data)
    # print(histogram)
    # print(sentence_generator(10, histogram))

    # print(test_frequency())
