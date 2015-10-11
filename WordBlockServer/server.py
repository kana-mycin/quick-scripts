from flask import Flask, request
import json
from wordBlock import main
app = Flask(__name__)

@app.route('/', methods=['GET'])
def find_synonyms():
    topic = request.args['topic']
    word = request.args['word']
    return json.dumps(main(topic, word))

if __name__ == '__main__':
    app.debug=True
    app.run()