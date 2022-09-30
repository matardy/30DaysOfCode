# DÍA 4
## Fechas
### Descripción del problema :kissing:
**Resuelto por:** [Gutemberg S. Mendoza](linkedin.com/in/gutembergsmendoza)
📅 Supongamos que tenemos dos fechas Fecha 1: 04/04/2022 y Fecha 2: 23/04/2022, fechas de inicio y fin, respectivamente. Y quiero distribuir un numero n de horas en este rango de fechas.

Por ejemplo, quiero distribuir 120 horas, en las fechas indicadas anteriormente, sin considerar los fines de semana, el programa me debería de mostrar: 08:00:00.


### Descripción de la solución :smiling_imp:
En este caso utilizaremos librerias en Python que están diseñadas para trabajar con fechas. 

El reto en este ejercicios es calcular los días laborables, es un problema conocido como `business_days`. En este reto encontraras `solution.py` solución simple utilizando libreria `datetime`. 

Y en `main.py` encontraras un acercamiento a una solución desde cero. 

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
