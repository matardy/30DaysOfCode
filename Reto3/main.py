from __future__ import annotations
import math


class Point:
    """
        Definimos a un punto como un objeto que tiene asociado su ubicacion (location),
        tiempo (time), nombre(name) y si dicho punto ha sido visitado por el trabajador.

    """
    def __init__(self, location:list, time:list, name:str, visited:bool = False):
        self.location = location 
        self.time = time 
        self.name = name
        self.visited = visited

    def set_visited(self):
        self.visited = True

    def is_visited(self): # Por defecto todos los puntos no estan visitados
        return self.visited

    def get_time(self): # pasamos el tiempo a minutos
        return self.time[0]*60 + self.time[1]
    
    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def get_distance(self, work_place:Point):
        # (x2 - x1 / y1 - y2)
        x_2 = work_place.get_location()[0]
        x_1 = self.get_location()[0]
        y_2 = work_place.get_location()[1]
        y_1 = self.get_location()[1]

        return math.sqrt(math.pow(x_2 - x_1,2) + math.pow(y_2 - y_1,2))

    def compare_to(self, work_place:Point): # compara si un objeto es igual a otro por su nombre
        return self.get_name() == work_place.get_name()


   

def calculate_path(points:list[Point], first_point:Point)->list(Point):
    tmp = [] # lista temporal que guarda las comparaciones de punto a punto
    sorted_list = [first_point] # lista final, siempre inicia con el punto elegido por el usuario
    work_point = first_point # Punto incial, este es un pivote e ira cambiando segun escoja la ruta

    # Contador
    j=0

    while j<len(points): # La cantidad de comparaciones sera igual a la cantidad de puntos

        # work_point empieza siendo el punto elegido por el usuario
        # luego work_point pasa a ser el punto tenga la ruta mas corta al punto inicial.
        # Es por esto que work_point siempre será un punto visitado

        # Marco a work_point como un punto visitado
        for i in points:
            if i.compare_to(work_point):
                i.set_visited()

        # Guarda las rutas de work_point con respecto a los puntos no visitados en tmp
        for i in points:
            if not i.is_visited():
                tmp.append([i, work_point.get_distance(i)])

        # Verifico si tengo rutas para comparar
        if len(tmp) != 0 :
            # De la lista de rutas, escojo la minima
            min_distance = min(tmp, key=lambda x:x[1])[0]
            # La minima ruta pasa a ser mi pivote, mi nuevo work_point
            work_point = min_distance
            # Guardo los puntos en la lista final
            sorted_list.append(work_point)
            # Reinicio la lista de rutas
            tmp = []

        # aumento el contador
        j = j+1

    return sorted_list


def calculate_path_bytime(points:list(Point))->list(Point):
    # El tiempo de cada punto esta encalsulado en el objeto Punto, utilizo sorted para ordenar la lista
    return sorted(points, key =lambda x:x.get_time(), reverse = True)


def main():
    D = Point([-4,4], [0,45], "D")
    A = Point([-1,1], [2,30], "A")
    C = Point([2,7], [2,50], "C")
    B = Point([4,5], [1,0], "B")
    points = [D,A,C,B]

    print("Ruta tomando el cuenta el camino: ")
    for i in calculate_path(points, A):
        print(i.get_name())
    
    print("Ruta tomando el cuenta el tiempo: ")
    for i in calculate_path_bytime(points):
        print(i.get_name())


if __name__ == '__main__':
    main()