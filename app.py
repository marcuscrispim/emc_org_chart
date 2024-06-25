from flask import Flask, jsonify, render_template
from disciplinas import semestres, disciplinas

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/disciplinas')
def get_disciplinas():
    return jsonify({'semestres': semestres, 'disciplinas': disciplinas})

if __name__ == '__main__':
    app.run(debug=True)