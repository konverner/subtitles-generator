from spellchecker import SpellChecker

from src.utils import text_likelihood


def test_text_likelihood_empty():
    empty_string = ''
    dictionary = SpellChecker(language='en')
    likelihood_score = text_likelihood(empty_string, dictionary)
    assert likelihood_score == 0.0, 'incorrect likelihood score'


def test_text_likelihood_normal():
    text = 'a cat runs after a dog'
    dictionary = SpellChecker(language='en')
    likelihood_score = text_likelihood(text, dictionary)
    assert likelihood_score == 1.0, 'incorrect likelihood score'


def test_text_likelihood_wrong():
    text = 'dslfkds dsfklsdkfl'
    dictionary = SpellChecker(language='de')
    likelihood_score = text_likelihood(text, dictionary)
    assert likelihood_score == 0.0, 'incorrect likelihood score'
 
