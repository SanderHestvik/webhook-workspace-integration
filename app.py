from crypt import methods
from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/', methods=['POST'])
def health_check():
    # TODO should compute and verify HMAC
    response = {"operationalState": "operational",
                "tokensState": "valid"}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
