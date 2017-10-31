from histogram import get_clean_data, get_histogram, get_total_unique_words, get_frequency
import pytest

with open('source_text.txt') as file:

    raw_data = file.read().lower()

def test_get_clean_data():
    assert '25' not in get_clean_data(raw_data)
    assert '\n' not in get_clean_data(raw_data)
    assert '(CROWD CHEERS)' not in get_clean_data(raw_data)
    assert 'CROWD CHEERS' not in get_clean_data(raw_data)
    assert '(APPLAUSE)' not in get_clean_data(raw_data)
    assert 'APPLAUSE' not in get_clean_data(raw_data)
    assert '\t' not in get_clean_data(raw_data)
    assert '' not in get_clean_data(raw_data)
    assert '.' not in get_clean_data(raw_data)
    assert ',' not in get_clean_data(raw_data)
    assert '!' not in get_clean_data(raw_data)

def test_get_histogram():
    clean_data = get_clean_data(raw_data)
    histogram = get_histogram(clean_data)
    dictionary_types = [True if type(key) == str and type(num) == int else False for key, num in histogram.items()]
    assert False not in dictionary_types ## Checks if keys and values are the correct type
    assert len(histogram) == len(dictionary_types)

def test_get_total_unique_words():
    clean_data = get_clean_data(raw_data)
    histogram = get_histogram(clean_data)
    assert type(get_total_unique_words(histogram)) == int
