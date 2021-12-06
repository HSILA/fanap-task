from flask import Flask, request, Response
from check_overlap import Overlap
import datetime
import pickle
import json

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        data = request.json
        time = datetime.datetime.now()
        Overlap(data, time)
        return {"message": "success"}
    else:
        with open('rectangles.pkl', 'rb') as f:
            rectangles = pickle.load(f)
        return Response(json.dumps(rectangles),  mimetype='application/json')

if __name__ == '__main__':
    app.run(host= '127.0.0.1', debug=True)