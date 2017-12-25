def add_to_sentence(prev_sentence, token_to_add):
    '''
    token_to_add: String
    Returns a new sentence comprised of a new token being appended to the old sentence
    '''
    return prev_sentence + token_to_add + ' '
    
def get_next_token(rand_token):
    '''
    rand_token: String
    Returns the next token in markov chain
    '''
    return rand_token.split(' ')[-1]
