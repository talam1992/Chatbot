from googletrans import Translator


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


def is_alpha(word):
    try:
        return word[:1].encode('ascii').isalpha()
    except:
        return False