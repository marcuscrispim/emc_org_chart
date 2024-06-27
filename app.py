from flask import Flask, render_template, jsonify
from disciplinas import semestres

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/disciplinas')
def get_disciplinas():
    response = []
    for semestre in semestres:
        semestre_data = []
        for codigo, prereqs in semestre.items():
            semestre_data.append({
                "nome": codigo,
                "preRequisitos": prereqs
            })
        response.append(semestre_data)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
