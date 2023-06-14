from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    print(f"[*]- Program Executed Successfully by {request.host}")
    return {
        "response": "success"
    }


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)
