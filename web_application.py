from flask import Flask, jsonify
from LDA_similarities import Similar

app = Flask(__name__)


@app.route("/songs/<id>/similar", methods=['GET', 'POST'])
def similar(id):
    return jsonify(Similar(int(id)).get_json())
# TODO: test response

if __name__ == '__main__':
    app.run()
