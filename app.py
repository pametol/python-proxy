from flask import Flask, request, Response
import requests


PROXY_SITE = 'http://httpbin.org/'
app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET'])
def proxy(path):
    if request.method == 'GET':
        resp = requests.get(f'{PROXY_SITE}{path}')
        headers = [(name, value) for name, value in resp.headers.items()]
        print(headers)
        response = Response(resp.content, resp.status_code, headers)

        return response

if __name__ == '__main__':
    app.run()
