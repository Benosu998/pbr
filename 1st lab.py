opt = {
    'op5': ['pbr', 'android', 'actn'],
    'op6': ['psihologie', 'CC', 'tiln', 'arms'],
    'op7': ['sca', '.net', 'rpa']
}
scor = {
    'pbr': 0,
    'android': 0,
    'actn': 0,
    'psihologie': 0,
    'CC': 0,
    'tiln': 0,
    'arms': 0,
    'sca': 0,
    'rpa': 0,
    '.net': 0
}
props = {
    'pbr': ['eclipse', 'fortran', 'reguli', 'c'],
    'android': ['android', 'mobile', 'java'],
    'actn': ['numere', 'ecuatii', 'python', 'fai'],
    'psihologie': ['oameni', 'relatii', 'profesional', 'comunicare'],
    'CC': ['retele', 'cloud', 'stocare', 'api', 'rest', 'nodejs', 'orice limbaj', 'python'],
    'tiln': ['parsare', 'limbaj', 'natura', 'python'],
    'arms': ['analiza', 'socializare', 'python', 'no-stress'],
    'rpa': ['retele', 'distribuite', 'sisteme'],
    'sca': ['fai', 'si', 'securitate', 'java', 'protocol'],
    '.net': ['.net', 'c#', 'proiect']
}
intrebari = [
    ('care din urmatoarele limbaje va place cel mai mult?', ['python', 'java', 'c', '.net']),
    ('Cum ati vrea sa fie evaluarea?', ['proiect', 'comunicare', 'fai']),
    ('Ce va intereseaza cel mai mult', ['securitate', 'retele', 'analiza', 'ecuatii', 'reguli', 'no-stress']),
    ('Ati vrea ca materia sa se asemene cu ... ', ['fai', 'si']),
    ('Limbajul forte al dvs  este...', ['python', 'c', 'java', 'c#']),
    ('Nu ati vrea sa scapati de...', ['sisteme', 'nodejs', 'eclipse', 'protocol']),

]
if __name__ == "__main__":
    for intrebare, raspunsuri in intrebari:
        r = input(intrebare + str(raspunsuri))
        for materie in props:
            if r in props[materie]:
                scor[materie] += 1
    print(scor)
    for op in opt:
        materie = opt[op]
        rz = max(materie, key=lambda x: int(scor[x]))
        print(rz)
