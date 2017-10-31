import re
import string

# TODO: Finish clean data function
# TODO: Finish logic for histogram function
# TODO: Finish unique_words function
# TODO: Finish frequency function

def get_histogram(source_text):
    '''
    Source_text: String
    Function analyses the frequency of words in Source_text
    Returns key value pair. Key: String, Value: Int
    '''
    histogram = {}

    for word in source_text:
        if word not in histogram:
            histogram[word] = 1
            continue
        histogram[word] += 1
    return histogram

def get_unique_words(histogram):
    '''
    Histogram: Key value pair. Key: String, Value: Int
    Function counts the total unique words in the histogram
    Returns Int
    '''
    pass

def get_frequency(word, histogram):
    '''
    Word: String
    Histogram: Key value pair. Key: String, Value: Int
    Function computes the number of times that word appears in histogram
    Returns Int
    '''
    pass

def get_clean_data(raw_data):

    nonspoken_content_removed = re.sub('\(\w*\)', '', raw_data)

    nonspoken_content_removed = re.sub('\(\w*\s\w*\)', '', nonspoken_content_removed)

    numbers_removed = re.sub('\d\w*', '', nonspoken_content_removed)

    punctuationless_data = ''.join([char for char in numbers_removed
                                    if char not in string.punctuation])# Removes punctuation from data

    clean_data = re.split('\s*', punctuationless_data)[:-1]  # Splits data based on whitespace

    return clean_data

def main():
    with open('source_text.txt') as file:

        raw_data = file.read().lower()

        clean_data = get_clean_data(raw_data)

if __name__=='__main__':
    main()
