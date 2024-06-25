# disciplinas.py

semestres = [
    {
        "EGR5213": [],
        "EMC5004": [],
        "EQA5116": [],
        "FSC5101": [],
        "INE5201": [],
        "MTM3110": []
    },
    {
        "EGR5214": ["EGR5213"],
        "EMC5132": ["FSC5101", "MTM3110"],
        "FSC5002": ["FSC5101", "MTM3110"],
        "FSC5122": [],
        "MTM3120": ["MTM3110"],
        "MTM3121": []
    },
    {
        "EMC5128": ["MTM3121"],
        "EMC5201": ["EQA5116"],
        "EMC5223": ["MTM3110"],
        "EMC5405": ["FSC5002", "MTM3120"],
        "INE5202": ["INE5201"],
        "MTM3103": ["MTM3120"]
    },
    {
        "MTM3131": ["MTM3120", "MTM3121"],
        "EMC5138": ["EMC5128"],
        "EMC5142": ["EMC5128"],
        "EMC5302": ["EGR5214", "EMC5004"],
        "EMC5361": ["FSC5101", "MTM3120"],
        "EMC5407": ["EMC5405", "EMC5132"]
    },
    {
        "EMC5418": ["EMC5405"],
        "MTM3104": ["MTM3131"],
        "EMC5110": ["EMC5138", "EMC5201"],
        "EMC5123": ["EMC5361"],
        "EMC5202": ["EMC5201"],
        "EMC5203": ["EMC5201", "EMC5223"]
    },
    {
        "EMC5410": ["EMC5405"],
        "EMC5417": ["EMC5405", "INE5202"],
        "EMC5419": ["EMC5407", "MTM3104"],
        "FSC5113": ["MTM3110"],
        "EEL5113": ["FSC5113"],
        "EMC5005": ["EMC5302", "INE5202"]
    },
    {
        "EMC5210": ["EMC5202", "EMC5203", "EMC5223", "EMC5302"],
        "EMC5335": ["EMC5123", "EMC5138"],
        "EMC5336": ["MTM3104"],
        "EMC5404": ["EMC5407", "EMC5417"],
        "EMC5003": [],
        "EMC5006": ["EEL5113"]
    },
    {
        "EMC5140": ["EMC5138", "EMC5361", "MTM3104"],
        "EMC5143": ["EMC5138"],
        "EMC5204": ["EEL5113", "EMC5201"],
        "ENS5146": [],
        "EPS5229": []
    }
]

disciplinas = {disciplina: prereqs for semestre in semestres for disciplina, prereqs in semestre.items()}