from flask import Flask, render_template, url_for, jsonify, request
import translatetext, helpers, synthesizetext, synthesizespeech
import os
import json

TEMPLATE_DIR = os.path.abspath('templates')
STATIC_DIR = os.path.abspath('static')

app = Flask(__name__,template_folder=TEMPLATE_DIR,static_folder=STATIC_DIR)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate-text', methods=['POST'])
def translate_text():
    data = request.get_json()
    text_input = data['text']
    translation_output = data['to']
    response = translatetext.get_translation(text_input, translation_output)
    return jsonify(response)

@app.route('/text-analysis', methods=['POST'])
def sentiment_analysis():
    data = request.get_json()
    input_text = data['inputText']
    input_lang = data['inputLanguage']
    output_text = data['outputText']
    output_lang =  data['outputLanguage']
    result = {}
    language_response_list = []
    sentiment_response_list = []
    entity_response_list = []
    key_response_list = []
    try:
        language_response = helpers.get_languages(input_text,output_text)
        print(language_response)
        for document in language_response['documents']:
            language_response_list.append({"Document Id": document['id'], "Language":document['detectedLanguages'][0]['name']})
        print(language_response_list)
        result['Language'] = language_response_list
        sentiment_response = helpers.get_sentiment(input_text, input_lang, output_text, output_lang)
        for document in sentiment_response['documents']:
            sentiment_response_list.append({"Document Id": document['id'], "Sentiment Score": "{:.2f}".format(document['score'])})
        result['Sentiment'] = sentiment_response_list
        entity_response = helpers.get_entities(input_text,output_text)
        for document in entity_response['documents']:
            for entity in document['entities']:
                entity_response_list.append({"Document Id": document['id'], "NAME":entity['name'], "Type":entity['type']})
        result['Entity'] = entity_response_list
        key_response = helpers.get_keyphrases(input_text, input_lang, output_text, output_lang)
        for document in key_response['documents']:
            for phrase in document['keyPhrases']:
                key_response_list.append({"Document Id":document['id'], "Key Phrases":phrase})
        result['Key Phrases'] = key_response_list
    except Exception as err:
        print("Encountered exception. {}".format(err))
    return json.dumps(result)

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    data = request.get_json()
    text_input = data['text']
    voice_font = data['voice']
    tts = synthesizetext.TextToSpeech(text_input, voice_font)
    tts.get_token()
    audio_response = tts.save_audio()
    return audio_response

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    text_response = synthesizespeech.speech_to_text_service()
    return jsonify(text_response)


if __name__ == "__main__":
    app.run(debug=True)