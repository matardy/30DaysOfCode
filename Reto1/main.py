def main():
    n = int(input("Ingrese un numero n y la función retornará: "))
    print("El termino ", n, " de la serie de fibonacci es: ", fibonacci(n))
    m = int(input("Ingrese un numero m y la función retornara m terminos de la serie de Fibonacci y su suma: "))
    elements = fibonacci_until(m)
    for i in elements:
        print(i)
    print("Su suma es: ", fib_sum_until(m))

def fibonacci(n:int)->int:
    """Funcion principal que retorne el n-esimo termino
       de una serie de fibonacci.

    Args:
        n (int): entero que indica n-esimo termino a retornar

    Returns:
        int: n-esimo termino
    """
    if(n<=1):
        return n 
    else: 
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_until(m:int)->list:
    """Funcion que devuelve una serie de fibonacci en una lista
       de m terminos de fibonacci

    Args:
        m (int): numero de terminos de una series de fibonacci

    Returns:
        list: Serie de fibonacci de m terminos
    """
    fib_elements = []
    for i in range(1,m+1):
        fib_elements.append(fibonacci(i))
    return fib_elements
        
def fib_sum_until(m:int)->int:
    """ Funcion que retorna la suma de m terminos
        de una serie de fibonacci

    Args:
        m (int): numero de terminos de una serie de fibonacci

    Returns:
        int: suma de m terminos de fibonacci
    """
    sum = 0
    for i in range(1,m+1):
        sum += fibonacci(i)
    return sum

if __name__ == '__main__':
    main() # Test de las funciones requeridas