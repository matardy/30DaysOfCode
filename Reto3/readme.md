# DÍA 3
## Geoemtría, Ordenamiento y más
### Descripción del problema :kissing:
**Resuelto por:** [Gutemberg S. Mendoza](linkedin.com/in/gutembergsmendoza)

Vamos a imaginar que Lucho Almeida, un humilde trabajador del campo tiene que pintar ciertas casas. Lucho ha armado un mapa con las cordenadas de las casas a donde tiene que ir. 

Además también ha anotado cuanto tiempo le tarda cada trabajo. 

Lucho nos ha entregado un mapa 2D como vemos en la figura de abajo y él se encuentra interesado en que creemos un algoritmo que: 
1. Calcule la ruta de acuerdo a la distancia de dos puntos teniendo en cuenta que: 
    - Lucho puede elegir iniciar en cualquier punto aleatoriamente. 
    - La siguiente casa a la que irá lucho será la más cercana a la que se encuentra. 
    - A Lucho no le gusta el trabajo doble, es por eso que no visitará la misma casa dos veces.
2. Calcula en que orden debe visitar las casas Lucho si quiere empezar en la que le toma más tiempo a la que le toma menos tiempo 

<p align="center">
<img src="https://github.com/matardy/30DaysOfCode/blob/main/Reto3/image.png">
</p>
---

### Descripción de la solución :smiling_imp:
Este problema no es realmente complejo, pero puede ser un reto la crear un codigo de calidad para este reto. 

Por lo que vamos a tratar de abstraer el problema al mundo real y hacer nuestro codigo lo más entendible posible. 

Primero, notemos que un Punto en el mapa tiene varias cosas asociadas: 

    - Una ubicación 
    - Un tiempo
    - Un Nombre 
    - Si un punto ha sido visitado o no por Lucho (Por defecto todos el False)
    
Además, tengo operaciones entre puntos como calcular su distancia y comparar sus tiempos etc. 

Lo más eficiente en este caso es crear una clase Point.

Dicha clase va a tener como atributos sus caracteristicas asociadas y metodos de clase entre Objetos Point. 

Finalmente cuando instancie un objeto de la clase Point se verá así: 
```
D = Point([-4,4], [0,45], "D")
    A = Point([-1,1], [2,30], "A")
    C = Point([2,7], [2,50], "C")
    B = Point([4,5], [1,0], "B")
```

En donde en su constructor tenemos las cordenadas, el tiempo, el nombre y por defecto todos los puntos se encuentra en `visited = False` 

Aunque parezca mentira, crear esta clase nos ha ahorrado muchisimo trabajo y ha hecho que los algoritmos sobre un objeto Point se puedan entender mejor. 

---

**El codigo se encuentra correctamente documento, sin embargo aquí te pongo el algoritmo para calcular la ruta (el de tiempo es bastante trivial):** 
1. El algoritmo recibe una lista de Objetos `Point` y un Objeto `Point` inicial y se inicializa un contador `j=0`
2. En una variable `work_point` guarda el `Point` inicial
3. Todos los objetos `Point` que sean `work_point` serán marcados como visitados. 
4. Guarda las rutas entre `work_point` y los demas `Point` en donde `visited=False` 
5. Con la funcion `min()` se obtiene el objeto `Point` que tenga la ruta minima con `work_point`.
6. El objeto `Point` que tenga la ruta minima con el anterior `work_point`, este sera el nuevo `work_point` y ademas se guardara en la lista final de la ruta. 
7. Se repite hasta que j = len(lista de objetos `Point`)





---
### No te queda completamente claro? :confounded:
**Revisa este video de TikTok donde te lo explico mejor :** 
*Efectivamente aquí explico programación orientada a objetos* :flushed:




[<img src="https://res.cloudinary.com/marcomontalbano/image/upload/v1664299328/video_to_markdown/images/tiktok--7148110640102624517-c05b58ac6eb4c4700831b2b3070cd403.jpg" width = "250" height = "440">](https://www.tiktok.com/@steveeeeess/video/7148110640102624517?is_copy_url=1&is_from_webapp=v1)







Puedes encontrar a la AEIS en redes sociales como: [```@aeis_epn```](https://www.instagram.com/aeis_epn/)



`#30DaysOfCode #30DaysOfCodeByAEIS #30DoCodeAEIS #30DaysAEIS`

<a href="https://www.linkedin.com/in/gutembergsmendoza/">
    <img align="left" alt="Gutemberg S. Mendoza | LinkedIn " width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />
  </a>
