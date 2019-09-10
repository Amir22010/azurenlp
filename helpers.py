import os, requests, uuid, json

# Don't forget to replace with your Cog Services subscription key!
subscription_key = 'a0ed5683ab204deeb4e7f5696e37a3ef'

# Our Flask route will supply four arguments: input_text, input_language,
# output_text, output_language.
# When the run sentiment analysis button is pressed in our Flask app,
# the Ajax request will grab these values from our web app, and use them
# in the request. See main.js for Ajax calls.
def get_languages(input_text, output_text):
    base_url = 'https://mytextservice.cognitiveservices.azure.com/text/analytics'
    path = '/v2.1/languages'
    constructed_url = base_url + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = {
        'documents': [
            {
                'id': '1',
                'text': input_text
            },
            {
                'id': '2',
                'text': output_text
            }
        ]
    }
    response = requests.post(constructed_url, headers=headers, json=body)
    return response.json()



def get_sentiment(input_text, input_language, output_text, output_language):
    base_url = 'https://mytextservice.cognitiveservices.azure.com/text/analytics'
    path = '/v2.1/sentiment'
    constructed_url = base_url + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = {
        'documents': [
            {
                'language': input_language,
                'id': '1',
                'text': input_text
            },
            {
                'language': output_language,
                'id': '2',
                'text': output_text
            }
        ]
    }
    response = requests.post(constructed_url, headers=headers, json=body)
    return response.json()

def get_entities(input_text, output_text):
    base_url = 'https://mytextservice.cognitiveservices.azure.com/text/analytics'
    path = '/v2.1/entities'
    constructed_url = base_url + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = {
        'documents': [
            {
                'id': '1',
                'text': input_text
            },
            {
                'id': '2',
                'text': output_text
            }
        ]
    }
    response = requests.post(constructed_url, headers=headers, json=body)
    return response.json()

def get_keyphrases(input_text, input_language, output_text, output_language):
    base_url = 'https://mytextservice.cognitiveservices.azure.com/text/analytics'
    path = '/v2.1/keyphrases'
    constructed_url = base_url + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = {
        'documents': [
            {
                'language': input_language,
                'id': '1',
                'text': input_text
            },
            {
                'language': output_language,
                'id': '2',
                'text': output_text
            }
        ]
    }
    response = requests.post(constructed_url, headers=headers, json=body)
    return response.json()




