from histogram import get_clean_data, get_histogram
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
    values_type = [True for num in histogram.values() if type(num) == int]
    assert False not in values_type ## Checks if all values are integers
