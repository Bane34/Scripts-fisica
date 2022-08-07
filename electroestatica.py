CONSTANTE_K = 9e9

def fuerza_electroestatica(q1, q2, radio):
    return CONSTANTE_K * abs(q1) * abs(q2) / (radio ** 2)