CONSTATE_G = 6.67e-11

def fuerza_gravitatoria(m1, m2, radio):
    return CONSTATE_G * m1 * m2 / (radio ** 2)

def fuerza_a_traves_de_campo(campo, m):
    return campo * m

def campo(m, radio):
    return CONSTATE_G * m / (radio ** 2)
