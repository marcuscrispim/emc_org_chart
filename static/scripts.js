document.addEventListener("DOMContentLoaded", function () {
    const disciplinasContainer = document.getElementById("disciplinas-container");

    fetch("disciplinas.json")
        .then(response => response.json())
        .then(data => {
            const semestres = data;
            semestres.forEach((semestre, i) => {
                const semestreDiv = document.createElement("div");
                semestreDiv.classList.add("semestre");

                const semestreTitle = document.createElement("h3");
                semestreTitle.textContent = `Semestre ${i + 1}`;
                semestreDiv.appendChild(semestreTitle);

                const concluirButton = document.createElement("button");
                concluirButton.textContent = "Marcar Semestre como Concluído";
                concluirButton.addEventListener("click", () => {
                    const disciplinasSemestre = semestreDiv.querySelectorAll(".disciplina");
                    disciplinasSemestre.forEach(disciplina => {
                        if (disciplina.classList.contains("pode-fazer") || disciplina.classList.contains("nao-pode-fazer")) {
                            disciplina.classList.add("concluida");
                            disciplina.classList.remove("pode-fazer", "nao-pode-fazer");
                        }
                    });
                    updateDisciplinasStatus();
                });
                semestreDiv.appendChild(concluirButton);

                semestre.forEach(disciplina => {
                    const disciplinaDiv = document.createElement("div");
                    disciplinaDiv.classList.add("disciplina");
                    disciplinaDiv.textContent = disciplina.nome;
                    disciplinaDiv.dataset.nome = disciplina.nome;
                    disciplinaDiv.dataset.preRequisitos = JSON.stringify(disciplina.preRequisitos);

                    disciplinaDiv.addEventListener("click", () => {
                        if (disciplinaDiv.classList.contains("pode-fazer") || disciplinaDiv.classList.contains("concluida")) {
                            disciplinaDiv.classList.toggle("concluida");
                            if (disciplinaDiv.classList.contains("concluida")) {
                                disciplinaDiv.classList.remove("pode-fazer");
                            }
                            updateDisciplinasStatus();
                        }
                    });

                    semestreDiv.appendChild(disciplinaDiv);
                });

                disciplinasContainer.appendChild(semestreDiv);
            });

            updateDisciplinasStatus();
        });

    function updateDisciplinasStatus() {
        const allDisciplinas = document.querySelectorAll(".disciplina");

        allDisciplinas.forEach(disciplina => {
            const preRequisitos = JSON.parse(disciplina.dataset.preRequisitos);
            if (preRequisitos.length === 0) {
                disciplina.classList.add("pode-fazer");
            } else {
                const allConcluidas = preRequisitos.every(pr => {
                    const prElement = document.querySelector(`[data-nome='${pr}']`);
                    return prElement && prElement.classList.contains("concluida");
                });

                if (allConcluidas) {
                    disciplina.classList.add("pode-fazer");
                } else {
                    disciplina.classList.add("nao-pode-fazer");
                }
            }
        });

        allDisciplinas.forEach(disciplina => {
            if (disciplina.classList.contains("concluida")) {
                disciplina.classList.add("concluida");
                disciplina.classList.remove("pode-fazer", "nao-pode-fazer");
            } else {
                const preRequisitos = JSON.parse(disciplina.dataset.preRequisitos);
                const allConcluidas = preRequisitos.every(pr => {
                    const prElement = document.querySelector(`[data-nome='${pr}']`);
                    return prElement && prElement.classList.contains("concluida");
                });

                if (allConcluidas) {
                    disciplina.classList.remove("nao-pode-fazer");
                    disciplina.classList.add("pode-fazer");
                } else {
                    disciplina.classList.remove("pode-fazer");
                    disciplina.classList.add("nao-pode-fazer");
                }
            }
        });
    }
});