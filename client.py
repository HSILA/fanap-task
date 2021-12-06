import requests

ENDPOINT = 'http://127.0.0.1:5000/'

def post_request(json):

    result = requests.post(ENDPOINT, json=json)
    if result.status_code == 200:
        print(result.json())

def get_request():
    result = requests.get(ENDPOINT)
    print(result.json())
    print(result.headers)

if __name__ == '__main__':
    ex1 = {
            "main": {"x": 0, "y": 0, "width": 10, "height": 20},
            "input": [
                    {"x": 2, "y": 18, "width": 5, "height": 4},
                    {"x": 12, "y": 18, "width": 5, "height": 4},
                    {"x": -1, "y": -1, "width": 5, "height": 4}
            ]
        }
    ex2 = {
            "main": {"x": 3, "y": 2, "width": 5, "height": 10},
            "input": [
                    {"x": 4, "y": -5, "width": 2, "height": 2},
                    {"x": 9, "y": 10, "width": 5, "height": 4}
            ]
        }
    post_request(ex2)
    get_request()