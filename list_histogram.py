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

def get_histogram(source_text):
    '''
    Source_text: List
    Function counts the frequency of words in Source_text
    Returns 2d list
    '''
    histogram = []

    for word in source_text:
        if len(word) < 2:
            continue
        word_count = source_text.count(word)
        if [word, word_count] not in histogram:
            histogram.append([word, word_count])
    return histogram

def get_total_unique_words(histogram):
    '''
    Histogram: Key value pair. Key: String, Value: Int
    Function counts the total unique words in the histogram
    Returns Int
    '''
    return len(histogram)

def get_frequency(word, histogram):
    '''
    Word: String
    Histogram: Key value pair. Key: String, Value: Int
    Function computes the number of times that word appears in histogram
    Returns Int
    '''
    for index, value in enumerate(histogram):
        if word in value:
            word_index = index
            break

    return histogram[word_index][1]

def main():
    with open('source_text.txt') as file:

        raw_data = file.read().lower()

        clean_data = get_clean_data(raw_data)

        histogram = get_histogram(clean_data)

        histogram_words_count = get_total_unique_words(histogram)

if __name__=='__main__':
    main()
