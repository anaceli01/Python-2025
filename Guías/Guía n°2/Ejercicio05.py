"""Camilo y Karla"""

#Paso 1 (Dict Tablero)
Piezas = {
    # Piezas blancas (1)
    "a1": "TorreB", "b1": "CaballoB", "c1": "AlfilB", "d1": "ReinaB",
    "e1": "ReyB", "f1": "AlfilB", "g1": "CaballoB", "h1": "TorreB",
    # Peones blancos (2)
    "a2": "PeonB", "b2": "PeonB", "c2": "PeonB", "d2": "PeonB",
    "e2": "PeonB", "f2": "PeonB", "g2": "PeonB", "h2": "PeonB",
    # Filas vacías (3 a 6)
    "a3": "", "b3": "", "c3": "", "d3": "", "e3": "", "f3": "", "g3": "", "h3": "",
    "a4": "", "b4": "", "c4": "", "d4": "", "e4": "", "f4": "", "g4": "", "h4": "",
    "a5": "", "b5": "", "c5": "", "d5": "", "e5": "", "f5": "", "g5": "", "h5": "",
    "a6": "", "b6": "", "c6": "", "d6": "", "e6": "", "f6": "", "g6": "", "h6": "",
    # Peones negros (7)
    "a7": "PeonN", "b7": "PeonN", "c7": "PeonN", "d7": "PeonN",
    "e7": "PeonN", "f7": "PeonN", "g7": "PeonN", "h7": "PeonN",
    # Piezas negras (8)
    "a8": "TorreN", "b8": "CaballoN", "c8": "AlfilN", "d8": "ReinaN",
    "e8": "ReyN", "f8": "AlfilN", "g8": "CaballoN", "h8": "TorreN"
}

#Paso 2 (Codigos ASCII)
simbolos = dict (
    TorreB = "R",
    TorreN = "r", 
    CaballoB = "N",
    CaballoN = "n",
    AlfilB = "B",
    AlfilN = "b",  
    ReinaB = "Q",
    ReinaN = "q", 
    ReyB = "K",
    ReyN = "k", 
    PeonB = "P",
    PeonN = "p"
)

print("Ajedrez En Una Terminal (Python)\n")

#Control de turnos
blancas = True

#Paso 4 (Pieza Capturadas e interacciones)
Capturas = []

while True:
    # Imprimir tablero
    print("  a b c d e f g h")
    for fila in range(8, 0, -1):
        linea = str(fila) + " "
        for columna in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            casilla = columna + str(fila)
            pieza = Piezas.get(casilla, "")
            simbolo = simbolos.get(pieza, ".")
            linea += simbolo + " " 
        print(linea + str(fila))
    
    # Mostrar turno actual
    jugador_actual = "Blancas" if blancas else "Negras"
    print(f"\nTurno de las {jugador_actual}")
    
    # Validar casilla de origen
    origen = ""
    while True:
        origen = input("Casilla de origen (ej: a2): ").lower()
        if origen not in Piezas:
            print("Casilla inválida. Intenta de nuevo.")
            continue
        pieza_origen = Piezas[origen]
        if not pieza_origen:
            print("La casilla está vacía. Intenta de nuevo.")
            continue
        # Validar color de la pieza
        color_pieza = pieza_origen[-1]  # 'B' o 'N' al final del nombre
        if (blancas and color_pieza != 'B') or (not blancas and color_pieza != 'N'):
            print(f"No es tu turno o la pieza no es de tu color ({jugador_actual}). Intenta de nuevo.")
            continue
        break
    
    # Validar casilla de destino
    destino = ""
    while True:
        destino = input("Casilla de destino (ej: a4): ").lower()
        if destino not in Piezas:
            print("Casilla inválida. Intenta de nuevo.")
            continue
        if destino == origen:
            print("El destino no puede ser igual al origen. Intenta de nuevo.")
            continue
        break
    
    # Mover pieza y registrar capturas
    P_Origen = Piezas[origen]
    P_Destino = Piezas[destino]
    
    if P_Destino:
        Capturas.append(simbolos[P_Destino])
        print(f"¡capturaste una pieza: {P_Destino}!,en la posicion {destino}")
    
    Piezas[destino] = P_Origen 
    Piezas[origen] = ""
    
    # Cambiar turno
    blancas = not blancas
    
    # Mostrar piezas capturadas
    if Capturas:
        print("Total de Piezas capturadas:", ", ".join(Capturas))