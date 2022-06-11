def getOffset(texto):
    minusculas = "abcdefghijklmnñopqrstuvwxyz"

    if not texto[0].islower():
        return 0
    else:
        return minusculas.index(texto[0]) + 1

def toMayusculas(texto):
    newString = ""

    for i in range(len(texto)):
        if i == 0:
            newString += texto[i].lower()
        else:
            newString += texto[i].upper()
          
    return newString

def codificar(texto, offset):
    mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZABCDEFGHIJKLMNÑOPQRSTUVWXYZABCDEFGHIJKLMNÑOPQRSTUVWXYZABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    textoCodificado = texto[0]

    for i in range(1,len(texto)):
        if texto[i] in mayusculas:
            textoCodificado += mayusculas[mayusculas.index(texto[i]) + offset]
        else:
            textoCodificado += texto[i]
    
    return textoCodificado
        


def decodificar(texto, offset):
    mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZABCDEFGHIJKLMNÑOPQRSTUVWXYZABCDEFGHIJKLMNÑOPQRSTUVWXYZABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    textoDecodificado = texto[0]

    for i in range(1,len(texto)):
        if texto[i] in mayusculas:
            textoDecodificado += mayusculas[mayusculas.index(texto[i]) - offset]
        else:
            textoDecodificado += texto[i]
    
    return textoDecodificado

def main():
    texto = input("Introduce el texto con el que deseas utilizar el programa: ")
    choice = input("Si deseas codificar el texto introduce 'c', si deseas decodificarlo pulsa enter.")

    offset = getOffset(texto)
    toMayus = toMayusculas(texto)


    if choice == "c":
        print(codificar(toMayus, offset))
    else:
        print(decodificar(toMayus, offset))



while True:
    main()

    