from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    # print(request.get_json())
    try:
        term_one = int(request.args.get('term_one'))
        term_two = int(request.args.get('term_two'))
    except Exception as exc:
        return {'error': str(exc)}, 400
    else:
        return {'result': term_one+term_two}, 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
