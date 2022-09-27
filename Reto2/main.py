# Author: Gutemberg S. Mendoza

def main():
    string = "4$$E&95KPfjT$%TJ7#6T2%tcnS#3$^"
    print('Cantidad de letras: ', count_letters(string))
    print('Cantidad de numeros: ', count_numbers(string))
    char = input("Ingresa un caracter: ")
    print(f'{char} se encuentra ' , count_this(string,char), "veces en la cadena.") 

def count_letters(string:str)->int:
    """Esta funcion recibe un string y retorna cuantas letras existen dentro 
       de dicho string

    Args:
        string (str): cadena de caracteres

    Returns:
        int: numero de letras dentro de la cadena
    """
    # Hacemos uso del metodo built-in para los objetores 'str'
    # en python: isalpha()
    # Esta funcion me dice si el caracter pertenece o no al alfabeto.

    # Con la ayuda de una Comprehension List, generamos una lista solo con
    # las letras de la cadena y finalmente calculamos la longitud de dicha lista

    return len([i for i in string if i.isalpha()])

def count_numbers(string:str)->int:
    """Esta funcion recibe un string y retorna cuantos numeros existen dentro 
       de dicho string

    Args:
        string (str): cadena de caracteres

    Returns:
        int: Cantidad de numeros dentro de la cadena
    """

    # La logica es la misma usada en la funcion count_letters, variando
    # el metodo isalpha() por isnumeric()

    return len([i for i in string if i.isnumeric()])

def find_char(char:str, match:str)->bool:
    if char == match:
        return True 
    return False

def count_this(string:str, matching_char:str)->int:
    """Esta funcion recibe un caracter y cuenta cuantos existen en una cadena

    Args:
        matching_char (str): caracter a ser contado en la cadena

    Returns:
        int: numero de matching_char en la cadena
    """

    # Esta funcion utiliza la misma logica de las funciones anteriores
    # en vez de usar isalpha o isnumeric utiliza find_char
    return len([i for i in string if find_char(i,matching_char)])

if __name__ == '__main__':
    main()
    
    
    