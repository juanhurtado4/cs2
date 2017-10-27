import re
import string

# TODO: Finish clean data function
# TODO: Finish logic for histogram function
# TODO: Finish unique_words function
# TODO: Finish frequency function

def histogram(source_text):
    '''
    Source_text: String
    Function analyses the frequency of words in Source_text
    Returns key value pair. Key: String, Value: Int
    '''
    pass

def unique_words(histogram):
    '''
    Histogram: Key value pair. Key: String, Value: Int
    Function counts the total unique words in the histogram
    Returns Int
    '''
    pass

def frequency(word, histogram):
    '''
    Word: String
    Histogram: Key value pair. Key: String, Value: Int
    Function computes the number of times that word appears in histogram
    Returns Int
    '''
    pass

def clean_data(raw_data):

    punctuationless_data = ''.join([char for char in raw_data
                                    if char not in string.punctuation])# Removes punctuation from data

    clean_data = re.split('\s*', punctuationless_data)[:-1]  # Splits data based on whitespace
    pass

def main():
    with open('source_text.txt') as file:

        raw_data = file.read()

        clean_data(raw_data)

if __name__=='__main__':
    main()
