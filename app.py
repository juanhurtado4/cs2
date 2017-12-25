from markov_sentence_generator import get_histogram, get_clean_data
from flask import Flask, request, render_template, redirect
from app_helper import get_next_token add_to_sentence
import random
import sys
import re
import string
import pdb

app = Flask(__name__)
app.config['DEBUG'] = True

def get_random_word(histogram):
    '''
    Histogram: Key Value pair. Key: String, Value: Int
    Returns a single word at random
    '''

    rand_num = random.random()

    cummulitive_wght = 0
    import pdb; pdb.set_trace() # Debugging
    for key, value in histogram.items():

        word_likelyhood_percent = value / sum(histogram.values())

        cummulitive_wght += word_likelyhood_percent

        if rand_num <= cummulitive_wght:
            random_word = key
            break



    return random_word


def test_get_random_word(repetitions, histogram):
    '''
    Repetitions: Int
    Histogram: Key Value pair. Key: String | Value: Int
    Function returns histogram of random words returned by (get_random_word) function
    '''
    list_of_words = []

    for _ in range(repetitions):

        rand_word = get_random_word(histogram)

        list_of_words.append(rand_word)

    histogram = get_histogram(list_of_words)

    return histogram

def sentence_generator(num_words_in_sentence, histogram):
    '''
    Num_words_in_sentence: Int
    Histogram: Key Value pair. Key: String | Value: Int
    Function generates a sentence from a source text
    Returns a string
    '''

    counter = 0

    list_of_words = list(histogram)

    starting_word = random.choice(list_of_words)
    sentence = starting_word + ' '
    # import pdb; pdb.set_trace()

    while counter != num_words_in_sentence:

        rand_word = get_random_word(histogram[next_word])

        sentence = add_to_sentence(sentence, rand_word)

        next_word = get_next_word(rand_word)

        counter += 1

    return sentence.strip().capitalize()

@app.route('/', methods=['GET', 'POST'])
def main():
    ''' Runs testing of get_random function based on command line arguments passed'''
    try:

        with open('obama_speech.txt') as file:

            raw_data = file.read().lower() # Makes sure file name is correct

    except:
        print('Please enter a valid file name')
        return

    if request.method == 'POST':

        clean_data = get_clean_data(raw_data)

        histogram = get_histogram(clean_data)

        sentence_length = int(request.form['sentence_length'])

        # test_result = test_get_random_word(sentence_length, histogram)

    # Turns dictionary into string so that it can be displayed in the browser
        rand_sentence = sentence_generator(sentence_length, histogram)

        return render_template('display_sentence.html',
                                rand_sentence=rand_sentence)
    else:
        return render_template('show_form.html')

if __name__=='__main__':
    app.run()
