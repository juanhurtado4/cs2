import random, sys

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

def get_word(raw_text):
    '''
    Histogram: Key Value pair. Key: String, Value: Int
    Returns a single word at random
    '''
    # list_of_keys = list(raw_text.keys()) # Turns dictionary into list of keys

    rand_index = random.randrange(0, len(raw_text))

    # return  list_of_keys[rand_index]
    return  raw_text[rand_index]

# print(get_word(parameters))

def main():
    file_name = sys.argv[1]

    try:
        with open(file_name) as file:

            raw_data = file.read().lower()

    except:
        print('Please enter a valid file name')

if __name__=='__main__':
    main()
