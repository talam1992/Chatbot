__author__ = 'Timothy Lam'

from spellchecker import SpellChecker

spell = SpellChecker()
spell.word_frequency.load_words(['microsoft', 'apple', 'google', 'tfl',
                                 'rihanna', 'chatbot', 'skype', 'facebook', 'amazon'])


def auto_correct(sentence):
    words = sentence.split()
    # find those words that may be misspelled
    misspelled = spell.unknown(words)
    #print(misspelled)
    if misspelled:
        for word in misspelled:
            # Get the one `most likely` answer
            correct = spell.correction(word)
            sentence = sentence.replace(word, correct)

    return sentence

#print(auto_correct("sned email"))
#print(auto_correct("amazon least price for external hard drive  2 terabyte"))