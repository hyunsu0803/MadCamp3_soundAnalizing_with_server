import os
from flask_cors import CORS
from flask import Flask, jsonify, request
from flask_restx import Resource, Api, reqparse
import main
from madmom.features import *

app = Flask(__name__)
api = Api(app)
app.config['DEBUG'] = True
CORS(app)


@app.route('/ddd')
def index():
    return 'Hello world'


@app.route('/express_to_flask', methods=['POST'])
def express_to_flask():
    parsed_request = request.files.get('file')
    fileName = request.form.get('fileName')

    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = dir_path + "\data"
    saved_file_path = os.path.join(dir_path, fileName)
    parsed_request.save(saved_file_path)

    notes = main.post_notes(saved_file_path)

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
    # return jsonify({"a":"b"})


@api.route('/test')
class testAPI(Resource):

    # 데이터 그냥 주는 함수
    def get(self):

        notes = main.get_notes()
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

    # 데이터를 request.json.get으로 받고 나도 return으로 주는 함수
    def post(self):

        parsed_request = request.files.get('file')
        notes = main.post_notes(parsed_request)
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
