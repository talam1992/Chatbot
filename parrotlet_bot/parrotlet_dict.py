__author__ = 'Timothy Lam'

from PyDictionary import PyDictionary
from googletrans import Translator
from nltk.corpus import wordnet
import config

dictionary=PyDictionary()


def selector(msg):
    try:
        if msg[:len("dictionary definition")] == "dictionary definition":
            msg = msg[len("dictionary definition") + 1:].strip()
            return find_definition(msg)

        #elif msg[:len("dictionary definition for")] == "dictionary definition for":
        #    msg = msg[len("dictionary definition for") + 1:].strip()
        #    return find_meaning(msg)
        elif msg[:len("dictionary synonym for")] == "dictionary synonym for":
            msg = msg[len("dictionary synonym for") + 1:].strip()
            return find_syn(msg)
        elif msg[:len("dictionary antonym for")] == "dictionary antonym for":
            msg = msg[len("dictionary antonym for") + 1:].strip()
            return find_ant(msg)
        elif msg[:len("dictionary translate")] == "dictionary translate":
            msg = msg[len("dictionary translate") + 1:].strip().split(' to ')
            return translate_sentence(msg[0], msg[1])
        else:
            return "I am sorry, the dictionary part of my brain is not working at the moment"
    except Exception as e:
        return f"error in dictionary selector: {e}"


def find_meaning(query):
    try:
        response = dictionary.meaning(query)
        if config.lang_code == 'en':
            reply = "<table id='t01'>\
                          <tr>\
                            <th>Word Type</th>\
                            <th>Definition</th>\
                          </tr>\
                        "
            for i in response:
                definition = ''
                if len(response[i]) > 1:
                    for j in response[i]:
                        definition += f"<p>{j.replace(';', ',')}."
                else:
                    definition = response[i][0]
                reply += f"<tr>\
                                    <td>{i}</td>\
                                    <td>{definition}</td>\
                                  </tr>"
            reply_ = {'display': reply, 'say': f'find below the definition of {query}'}
        else:
            reply = f"<table id='t01'>\
                                  <tr>\
                                    <th>{translate_sentence_code(query='Word Type', lang=config.lang_code)['display']}</th>\
                                    <th>{translate_sentence_code(query='Definition', lang=config.lang_code)['display']}</th>\
                                  </tr>\
                                "
            for i in response:
                definition = ''
                if len(response[i]) > 1:
                    for j in response[i]:
                        value = translate_sentence_code(query=j.replace(';', ','), lang=config.lang_code)['display']
                        definition += f"<p>{value}."
                else:
                    definition = translate_sentence_code(query=response[i][0], lang=config.lang_code)['display']
                word = translate_sentence_code(query=i, lang=config.lang_code)['display']
                reply += f"<tr>\
                                            <td>{word}</td>\
                                            <td>{definition}</td>\
                                          </tr>"
            say = translate_sentence_code(query=f'find below the definition of {query}', lang=config.lang_code)['say']
            reply_ = {'display': reply, 'say': say}
            config.lang_code = 'en'

        return reply_
    except Exception as e:
        return f"Error in find_meaning: {e}"


def find_definition(query):
    word_type = {'n': 'NOUN', 'v': 'VERB', 'a': 'ADJECTIVE', 's': 'ADJECTIVE SATELLITE', 'r': 'ADVERB'}
    try:
        response = wordnet.synsets(query)
        if config.lang_code == 'en':
            reply = "<table id='t01'>\
                          <tr>\
                            <th>Word Type</th>\
                            <th>Definition</th>\
                            <th>Example</th>\
                          </tr>\
                        "
            for i in response:
                w_type = word_type[i.pos()] if i.pos() in word_type else i.pos()
                definition = i.definition().replace(';', ',')
                example = f'{query}' if len(i.examples()) == 0 else i.examples()[0].replace(';', ',')
                reply += f"<tr>\
                                    <td>{w_type}</td>\
                                    <td>{definition}</td>\
                                    <td>{example}</td>\
                                  </tr>"
            reply_ = {'display': reply, 'say': f'find below the definition of {query}'}
        else:
            reply = f"<table id='t01'>\
                                  <tr>\
                                    <th>{translate_sentence_code(query='Word Type', lang=config.lang_code)['display']}</th>\
                                    <th>{translate_sentence_code(query='Definition', lang=config.lang_code)['display']}</th>\
                                    <th>{translate_sentence_code(query='Example', lang=config.lang_code)['display']}</th>\
                                  </tr>\
                                "
            for i in response:
                w_type = word_type[i.pos()] if i.pos() in word_type else i.pos()
                definition = i.definition().replace(';', ',')
                example = f'{query}' if len(i.examples()) == 0 else i.examples()[0].replace(';', ',')
                reply += f"<tr>\
                                    <td>{translate_sentence_code(query=w_type, lang=config.lang_code)['display']}</td>\
                                    <td>{translate_sentence_code(query=definition, lang=config.lang_code)['display']}</td>\
                                    <td>{translate_sentence_code(query=example, lang=config.lang_code)['display']}</td>\
                                  </tr>"
            say = translate_sentence_code(query=f'find below the definition of {query}', lang=config.lang_code)['say']
            reply_ = {'display': reply, 'say': say}
            config.lang_code = 'en'

        return reply_
    except Exception as e:
        return f"Error in find_definition: {e}"


def defin(query):
    word_type = {'n': 'NOUN', 'v': 'VERB', 'a': 'ADJECTIVE', 's': 'ADJECTIVE SATELLITE', 'r': 'ADVERB'}
    response = wordnet.synsets(query)
    if config.lang_code == 'en':
        reply = "<table id='t01'>\
                              <tr>\
                                <th>Word Type</th>\
                                <th>Definition</th>\
                                <th>Example</th>\
                              </tr>\
                            "
        for i in response:
            w_type = word_type[i.pos()] if i.pos() in word_type else i.pos()
            definition = i.definition()
            example = f'{query}' if len(i.examples()) == 0 else i.examples()[0]
            reply += f"<tr>\
                                        <td>{w_type}</td>\
                                        <td>{definition}</td>\
                                        <td>{example}</td>\
                                      </tr>"
        reply_ = {'display': reply, 'say': f'find below the definition of {query}'}
    else:
        reply = f"<table id='t01'>\
                                      <tr>\
                                        <th>{translate_sentence_code(query='Word Type', lang=config.lang_code)['display']}</th>\
                                        <th>{translate_sentence_code(query='Definition', lang=config.lang_code)['display']}</th>\
                                        <th>{translate_sentence_code(query='Example', lang=config.lang_code)['display']}</th>\
                                      </tr>\
                                    "
        for i in response:
            w_type = word_type[i.pos()] if i.pos() in word_type else i.pos()
            definition = i.definition()
            example = f'{query}' if len(i.examples()) == 0 else i.examples()[0]
            reply += f"<tr>\
                                        <td>{translate_sentence_code(query=w_type, lang=config.lang_code)['display']}</td>\
                                        <td>{translate_sentence_code(query=definition, lang=config.lang_code)['display']}</td>\
                                        <td>{translate_sentence_code(query=example, lang=config.lang_code)['display']}</td>\
                                      </tr>"
        say = translate_sentence_code(query=f'find below the definition of {query}', lang=config.lang_code)['say']
        reply_ = {'display': reply, 'say': say}
        config.lang_code = 'en'

    return reply_


def find_synonym(query):
    try:
        response = dictionary.synonym(query)

    except Exception as e:
        return f"Error in find_synonym: {e}"

    return response


def find_syn(query):
    synonyms = []
    for syn in wordnet.synsets(query):
        for l in syn.lemmas():
            synonyms.append(l.name())
    if len(synonyms) > 0:
        return f"synonyms for {query}: " + ', '.join(set(synonyms)).replace('_', '-')
    else:
        return f"There is no synonyms for {query}"


def find_ant(query):
    antonyms = []
    for syn in wordnet.synsets(query):
        for l in syn.lemmas():
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    if len(antonyms) > 0:
        return f"Antonyms for {query}: " + ', '.join(set(antonyms)).replace('_', '-')
    else:
        return f"There is no antonyms for {query}"


def find_antonym(query):
    try:
        response = dictionary.antonym(query)
    except Exception as e:
        return f"Error in find_antonym: {e}"

    return response


def ant_syn(query):
    words = []
    for syn in wordnet.synsets(query):
        for l in syn.lemmas():
            words.append(l.name())
            if l.antonyms():
                words.append(l.antonyms()[0].name())

    if len(words) > 0:
        return f"synonyms for {query}: " + ', '.join(set(words)).replace('_', '-')
    else:
        return f"There is no synonyms for {query}"


def translate_(query, lang):
    try:
        response = dictionary.translate(query,config.trans_code[lang.capitalize()])
    except Exception as e:
        return f"Error in find_translate_: {e}"
    return response


def translate_sentence(query, lang):
    try:
        translator = Translator()
        dest = config.trans_code[lang.capitalize()]
        obj = translator.translate(query, dest=dest)
        response = obj.text
        if is_alpha(obj.text):
            pronunciation = obj.text
        else:
            try:
                pronunciation = obj.extra_data['translation'][1][-1]
            except Exception as e:
                pronunciation = obj.text
        #pronunciation = obj.pronunciation
        reply = {'display': response, 'say': pronunciation}
    except Exception as e:
        return f"Error in translate_sentence: {e} \n request: {query} \n l: {lang}"
    return reply

def aball(query,lang):
    translator = Translator()
    #dest = config.trans_code[lang.capitalize()]
    obj = translator.translate(query, dest=lang)
    response = obj.text
    if is_alpha(obj.text):
        pronunciation = obj.text
    else:
        pronunciation = obj.extra_data['translation'][1][-1]
    # pronunciation = obj.pronunciation
    reply = {'display': response, 'say': pronunciation}
    return reply


def translate_sentence_code(query, lang):
    try:
        translator = Translator()
        obj = translator.translate(str(query), dest=lang)
        response = obj.text
        if is_alpha(obj.text):
            pronunciation = obj.text
        else:
            try:
                pronunciation = obj.extra_data['translation'][1][-1]
            except Exception as e:
                pronunciation = obj.text
        #pronunciation = obj.pronunciation
        reply = {'display': response, 'say': pronunciation}

    except Exception as e:
        print(f"Error in translate_sentence_code: {e} \n request: {query} \n l: {lang}")
        return {'display': "ask me a question",
                'say': f"Error in translate_sentence_code: {e} \n request: {query} \n l: {lang}"}
    return reply


def translate_list(query, lang):
    try:
        translator = Translator()
        obj = translator.translate(query, dest=lang)
        response = obj.text
        if is_alpha(obj.text):
            pronunciation = obj.text
        else:
            try:
                pronunciation = obj.extra_data['translation'][1][-1]
            except Exception as e:
                pronunciation = obj.text
        #pronunciation = obj.pronunciation
        reply = {'display': response, 'say': pronunciation}

    except Exception as e:
        print(f"Error in translate_sentence_code: {e} \n request: {query} \n l: {lang}")
        return {'display': "ask me a question",
                'say': f"Error in translate_sentence_code: {e} \n request: {query} \n l: {lang}"}
    return reply


def is_alpha(word):
    try:
        return word[:1].encode('ascii').isalpha()
    except:
        return False


def detect_lang(query):
    try:
        translator = Translator()
        return translator.detect(query).lang

    except Exception as e:
        return f"detect_lang error: {e}"

#print(translate_('hello', 'igbo'))
#print(selector("dictionary translate smart cities to japanese"))

#a = translate_sentence_code(query='hello', lang='ja')
#print(aball(query='jugar drake va mal', lang='en'))
#print(is_alpha("j"))
#print(defin('query'))
#print(find_ant('active'))