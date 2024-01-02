# El Sudoku es un popular pasatiempo que tenéis definido en https://es.wikipedia.org/wiki/Sudoku

# Te pedimos que realices una función que reciba un array bidimensional con un Sudoku de 9x9 resuelto

# y devuelva true si el Sudoku es correcto, false en caso contrario.

def esSudokuCorrecto(miSudoku):
    # Verificar filas
    for fila in miSudoku:
        if len(set(fila)) != 9 or sum(fila) != 45:
            return False

    # Verificar columnas
    for columna in range(9):
        if len(set(miSudoku[fila][columna] for fila in range(9))) != 9 or sum(miSudoku[fila][columna] for fila in range(9)) != 45:
            return False

    # Verificar subgrids 3x3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [miSudoku[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if len(set(subgrid)) != 9 or sum(subgrid) != 45:
                return False

    return True
