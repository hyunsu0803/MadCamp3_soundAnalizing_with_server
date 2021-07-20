import os
from flask_cors import CORS
from flask import Flask, jsonify, request
import main


app = Flask(__name__)
app.config['DEBUG'] = True
CORS(app)


@app.route('/react_to_flask', methods=['POST'])
def react_to_flask():
    parsed_request = request.files.get('file')
    fileName = request.form.get('fileName')

    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = dir_path + "\data"
    saved_file_path = os.path.join(dir_path, fileName)
    parsed_request.save(saved_file_path)

    notes = main.audio_to_MIDI_notes(saved_file_path)

    data = {}
    i = 0
    for n in notes:
        tmp = {
            'second': n[0],
            'code': n[1]
        }
        data['note' + str(i)] = tmp
        i = i + 1

    data = jsonify(data)
    return data


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000",  debug=True)
