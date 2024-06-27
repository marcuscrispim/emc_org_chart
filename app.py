from flask import Flask, render_template, jsonify
from disciplinas import disciplinas

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/disciplinas')
def get_disciplinas():
    semestres = [list(disciplinas.keys())[i:i + 6] for i in range(0, len(disciplinas), 6)]
    response = []
    for semestre in semestres:
        semestre_data = []
        for codigo in semestre:
            semestre_data.append({
                "nome": codigo,
                "preRequisitos": disciplinas[codigo]
            })
        response.append(semestre_data)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
