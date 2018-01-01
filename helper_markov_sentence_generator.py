import re

def get_clean_data_strt_end(raw_data):

    punctuation = """!"#$%&'()*+,-/:;<=>?@[\]^_`{|}~"""

    crowd_reaction_removed = re.sub('\(\w*\)', '', raw_data)

    crowd_reaction_removed = re.sub('\(\w*\s\w*\)', '', crowd_reaction_removed)

    numbers_removed = re.sub('\d\w*', '', crowd_reaction_removed)

    punctuationless_data = ''.join([char for char in numbers_removed
                                    if char not in punctuation and char != '\n'])  # Removes punctuation from data

    # Splits data based on whitespace
    # clean_data = re.split('\s*', punctuationless_data)[:-1]

    return punctuationless_data

def get_ending_token_histogram(raw_data):
    pass

def remove_empty_string(raw_data):
    '''
    raw_data: List
    Function removes empty sentences from raw data
    Returns none
    '''
    empty_sentences_index = []
    for ind, sentence in enumerate(raw_data):
        if len(sentence) < 1:
            empty_sentences_index.append(ind)

    for index in empty_sentences_index:
        raw_data.pop(index)

def get_first_token(sentence):
    for word in sentence.split(' '):
        if len(word) > 0 and ' ' not in word:
            return word

def get_last_token(sentence):
    sentence = sentence.split(' ')

    for index in range((len(sentence) - 1), -1, -1):
        if len(sentence[index]) > 0 and ' ' not in sentence[index]:
            return sentence[index]


if __name__ == '__main__':
    
    sentence = 'The world is a beautiful place'
    sentence2 = 'The world is a beautiful place '
    sentence3 = 'The world is a         '

    def test_get_last_token():
        assert get_last_token(sentence) == 'place'
        assert get_last_token(sentence2) != ' '
        assert get_last_token(sentence2) == 'place'
        assert get_last_token(sentence3) == 'a'
        print('Successful')
        
    test_get_last_token()