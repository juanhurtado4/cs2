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
    assert
