from logging import exception
from flask import Flask, request, abort

import spacy
import json

app = Flask(__name__)

@app.errorhandler(Exception)
def handle_exception(e):
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

@app.route("/entities", methods=["POST"])
def post_payload():
    data = json.loads(request.get_data())
    lang = data['lang']
    input = data['input']
    entities = {}
    module_name = ''

    if lang == 'en':
        module_name = 'en_core_web_sm'
    elif lang == 'de':
        module_name = 'de_core_news_sm'
    else:
        abort(422)

    nlp = spacy.load(module_name)
    doc = nlp(input)
    
    for entity in doc.ents:
        key = entity.text
        value = entity.label_
        entities.update({key:value})
    return entities

if __name__ == "__main__":
    app.run()
