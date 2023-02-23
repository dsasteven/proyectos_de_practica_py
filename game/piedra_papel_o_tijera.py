import random

def escoje_casillas():

    opciones = ('piedra', 'papel', 'tijeras')

    jugador_opcion = input('escoje ==> ')
    jugador_elijio = jugador_opcion.lower()

    computador_elijio = random.choice(opciones)

    if not jugador_elijio in opciones:
        print('esa opcion no existe escoje otra')
        return None, None

    return jugador_elijio, computador_elijio


def lojica_del_juego(jugador_elijio, computador_elijio, puntos_jugador, puntos_computador):

    if jugador_elijio == computador_elijio:
        print('empate')

    if jugador_elijio == 'piedra':
        if computador_elijio == 'tijeras':
            print('piedra gana a tiejera')
            print('gana jugador')
            puntos_jugador += 1

        else:
            print('papel gana a pierda')
            print('gana computador')
            puntos_computador += 1
    
    if jugador_elijio == 'papel':
        if computador_elijio == 'piedra':
            print('papel gana a pierda')
            print('gana jugador')
            puntos_jugador += 1

        else:
            print('tijera gana a pape')
            print('gana computador')
            puntos_computador += 1

    if jugador_elijio == 'tijera':
        if computador_elijio == 'papel':
            print('tijeras ganan a papel')
            print('gana jugador')
            puntos_jugador += 1

        else:
            print('piedra gtanan a papel')
            print('gana computador')
            puntos_computador += 1
            
    return puntos_jugador, puntos_computador

def quien_gana( puntos_jugador, puntos_computador):

    if puntos_jugador == 3:
        print('jugador cano la partida')
        return 1

    if puntos_computador == 3:
        print('computador gano la partida')
        return 1  


def run():


    rondas = 0
    puntos_jugador = 0
    puntos_computador = 0

    while True:

        rondas += 1
        print('.')
        print('.')
        print('.')
        print('.')
        print(f'puntos del jugador {puntos_jugador}' )

        print(f'puntos del computador {puntos_computador}' )
        print(f'rondas {rondas}')
        print('juego piedra, papel o tijeras ')


        jugador_elijio, computador_elijio = escoje_casillas()

        puntos_jugador, puntos_computador = lojica_del_juego(jugador_elijio, computador_elijio, puntos_jugador, puntos_computador)

        hay_ganador = quien_gana(puntos_jugador, puntos_computador)
        if hay_ganador == 1:
            break


run()
