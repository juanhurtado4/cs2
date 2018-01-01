import random

def join_strings_together(prev_sentence, token_to_add):
    '''
    Prev_sentence: String
    Token_to_add: String
    Returns a new sentence comprised of a new token being appended to the old sentence
    '''
    return prev_sentence + token_to_add + ' '
    
def get_next_token(rand_token):
    '''
    rand_token: String
    Returns the next token in markov chain
    '''
    return rand_token.split(' ')[-1]

# TESTING NEW SENTENCE GENERATOR THAT INCLUDES STARTING AND ENDING TOKENS
# Test 1: Randomly choose starting word, enter while loop, then randomly choose ending word


def get_random_word(histogram):
    '''
    DELETE FUNCTION AFTER TESTING IS DONE
    '''

    rand_num = random.random()

    cummulitive_wght = 0
    # import pdb; pdb.set_trace() # Debugging
    for key, value in histogram.items():

        word_likelyhood_percent = value / sum(histogram.values())

        cummulitive_wght += word_likelyhood_percent

        if rand_num <= cummulitive_wght:
            random_word = key
            break

    return random_word

def sentence_generator(num_tokens_in_sentence, histogram, starting_histo, ending_histo):
    '''
    Num_words_in_sentence: Int
    Histogram: Key Value pair. Key: String | Value: Int
    Function generates a sentence from a source text
    Returns a string
    '''

    # TODO: change logic in while loop conditional to 1 less than the num_words_in_sentence
    # TODO: Before while loop prepend sentence with starting word, then proceed as normal
    # TODO: once while loop breaks choose one of the ending words
    # TODO: Add function that checks if the last word is in ending tokens histogram. If so, break out of while loop. If not, get next word. If all words are exhausted force break to ending histogram

    counter = 0

    list_of_tokens = list(histogram)
    list_of_starting_tokens = list(starting_histo)
    list_of_ending_tokens = list(ending_histo)

    starting_word = random.choice(list_of_starting_tokens)
    sentence = join_strings_together('', starting_word)
    next_token = random.choice(list_of_tokens)
    # import pdb; pdb.set_trace()

    while counter < num_tokens_in_sentence:

        rand_word = get_random_word(histogram[next_token])

        sentence = join_strings_together(sentence, rand_word)

        next_token = get_next_token(rand_word)

        counter += 1
    
    last_token = random.choice(list_of_ending_tokens)
    sentence = join_strings_together(sentence, last_token)

    return sentence.strip().capitalize()
