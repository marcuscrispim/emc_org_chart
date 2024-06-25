document.addEventListener('DOMContentLoaded', function() {
    fetch('/disciplinas')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('semestres-container');

            data.semestres.forEach((semestre, index) => {
                const semestreDiv = document.createElement('div');
                semestreDiv.classList.add('semestre');
                const semestreTitle = document.createElement('h2');
                semestreTitle.textContent = `Semestre ${index + 1}`;
                semestreDiv.appendChild(semestreTitle);

                Object.keys(semestre).forEach(disciplina => {
                    const div = document.createElement('div');
                    div.classList.add('disciplina');
                    div.textContent = disciplina;
                    div.addEventListener('click', () => {
                        handleDisciplinaClick(div, disciplina, data.disciplinas);
                    });
                    semestreDiv.appendChild(div);
                });

                const marcarCompletadoBtn = document.createElement('button');
                marcarCompletadoBtn.classList.add('marcar-completado');
                marcarCompletadoBtn.textContent = 'Marcar Semestre Como Concluído';
                marcarCompletadoBtn.addEventListener('click', () => {
                    marcarSemestreComoConcluido(semestreDiv, data.disciplinas);
                });

                semestreDiv.appendChild(marcarCompletadoBtn);
                container.appendChild(semestreDiv);
            });

            createLegend();
            updateHabilitadas(data.disciplinas);
        });
});

function handleDisciplinaClick(div, disciplina, allDisciplinas) {
    if (!div.classList.contains('habilitada') && !div.classList.contains('pode-fazer') && !div.classList.contains('completada')) {
        return;
    }

    if (!div.classList.contains('completada')) {
        div.classList.add('completada');
    } else {
        div.classList.remove('completada');
    }

    updateHabilitadas(allDisciplinas);
}

function updateHabilitadas(allDisciplinas) {
    const completedDisciplinas = Array.from(document.querySelectorAll('.disciplina.completada'))
                                        .map(div => div.textContent);

    const allDivs = document.querySelectorAll('.disciplina');
    allDivs.forEach(d => {
        const disc = d.textContent;
        const requisitos = allDisciplinas[disc] || [];
        const podeFazer = requisitos.every(req => completedDisciplinas.includes(req));
        const preRequisitosFeitos = requisitos.filter(req => completedDisciplinas.includes(req)).length;
        
        d.classList.remove('habilitada', 'pre-requisito', 'selecionada', 'trancada-diretamente', 'trancada-indiretamente', 'pode-fazer');

        if (d.classList.contains('completada')) {
            d.classList.add('selecionada');
        } else if (podeFazer) {
            d.classList.add('pode-fazer');
        } else if (preRequisitosFeitos > 0) {
            d.classList.add('trancada-indiretamente');
        } else {
            d.classList.add('trancada-diretamente');
        }
    });

    const marcarCompletadoBtns = document.querySelectorAll('.marcar-completado');
    marcarCompletadoBtns.forEach(btn => {
        const disciplinasNoSemestre = btn.parentElement.querySelectorAll('.disciplina');
        const todasCompletadas = Array.from(disciplinasNoSemestre).every(div => div.classList.contains('completada'));
        btn.disabled = todasCompletadas;
    });
}

function marcarSemestreComoConcluido(semestreDiv, allDisciplinas) {
    const disciplinasNoSemestre = semestreDiv.querySelectorAll('.disciplina');
    disciplinasNoSemestre.forEach(div => {
        if (div.classList.contains('pode-fazer') || div.classList.contains('habilitada') || !div.classList.contains('completada')) {
            div.classList.add('completada');
        }
    });
    updateHabilitadas(allDisciplinas);
}

function createLegend() {
    const legend = document.createElement('div');
    legend.classList.add('legend');
    
    const legendItems = [
        { text: 'Pré-requisito', className: 'pre-requisito' },
        { text: 'Selecionada', className: 'selecionada' },
        { text: 'Trancada diretamente', className: 'trancada-diretamente' },
        { text: 'Trancada indiretamente', className: 'trancada-indiretamente' },
        { text: 'Pode fazer', className: 'pode-fazer' }
    ];
    
    legendItems.forEach(item => {
        const div = document.createElement('div');
        div.classList.add('legend-item');
        const colorBox = document.createElement('span');
        colorBox.classList.add('color-box', item.className);
        const text = document.createElement('span');
        text.textContent = item.text;
        div.appendChild(colorBox);
        div.appendChild(text);
        legend.appendChild(div);
    });

    document.body.insertBefore(legend, document.getElementById('semestres-container'));
}
