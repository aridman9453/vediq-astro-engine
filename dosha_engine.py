def detect_doshas(planets):

    doshas = []

    if planets["Mars"]["house"] in [1, 2, 4, 7, 8, 12]:
        doshas.append("Manglik Dosha")

    if planets["Rahu"]["house"] == 1:
        doshas.append("Rahu Influence")

    if planets["Ketu"]["house"] == 1:
        doshas.append("Ketu Influence")

    return doshas
