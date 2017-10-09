from flask import Flask, jsonify, render_template, request
# from flask.ext import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from LDA_similarities import Similar
# from web_application import model

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ihor:root@localhost/guitar_tips'

db = SQLAlchemy(app)

# texts =

@app.route("/songs/<id>/similar", methods=['GET', 'POST'])
def similar(id):
    return jsonify(Similar(int(id)).get_json())

if __name__ == '__main__':
    app.run()
