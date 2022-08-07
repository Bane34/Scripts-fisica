CONSTATE_G = 6.67e-11

def fuerza_gravitatoria(m1, m2, radio):
    return CONSTATE_G * m1 * m2 / (radio ** 2)

def fuerza_gravitatoria(campo, m):
    return campo * m

def campo(m, radio):
    return CONSTATE_G * m / (radio ** 2)

if __name__ == '__main__':
    print(campo(5.98e24, 6.37e6))