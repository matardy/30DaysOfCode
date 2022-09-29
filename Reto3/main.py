from __future__ import annotations
import math


class Point:
    def __init__(self, location:list, time:list, name:str):
        self.location = location 
        self.time = time 
        self.name = name

    def get_time(self):
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

   

def main():
    D = Point([-4,4], [0,45], "D")
    A = Point([-1,1], [2,30], "A")
    C = Point([2,7], [2,50], "C")
    B = Point([4,5], [1,0], "B")
    points = [D,A,C,B]

    print("Ruta por distancia: ")
    for i in calculate_path(points, A):
        print(i.get_name())

    print("Ruta por tiempo: ")
    for i in calculate_path_bytime(points):
        print(i.get_name())

def calculate_path(points:list, first_point:Point)->list(Point):
    # [D,A,C,B]
    i = 0
    tmp = []
    sorted_list = [first_point]
    work_point = first_point # Punto inicial, escogido por el usuario

    # Todos los puntos menos el primero, por eso len(points - 1)
    while i < len(points)-1 :

        # Compara la distancia con los puntos restantes
        for j in range(i, len(points)):
            if work_point.get_distance(points[j])!= 0: # Compara con todos los puntos, menos consigo mismo
                # Guarda los puntos con la distancia hacia work_point
                # Crea una lista temporal con los nombres de los puntos 
                # y su distancia a work_point [punto, distancia_a_workpoint]
                tmp.append([points[j], work_point.get_distance(points[j])])

        # Verifica si ya no hay mas puntos para comprar
        if len(tmp)!=0:
            # toma la lista y obtiene la distancia minima [punto, minima_distancia]
            min_distance = min(tmp, key=lambda x:x[1])[0]

        # actualiza el work_point con la distancia minima
        work_point = min_distance
        # completa la lista con el orden de distancia
        sorted_list.append(work_point)
        # avanza
        i = i+1
        # limpia la lista temporal
        tmp = []

    return sorted_list
    
def calculate_path_bytime(points:list(Point))->list(Point):
    return sorted(points, key =lambda x:x.get_time(), reverse = True)


if __name__ == '__main__':
    main()