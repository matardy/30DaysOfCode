# DÍA 2
## Strings, Strings y más Strings
### Descripción del problema :kissing:
**Resuelto por:** [Gutemberg S. Mendoza](linkedin.com/in/gutembergsmendoza)

Dada una cadena de caracteres, por ejemplo: `4$$E&95KPfjT$%TJ7#6T2%tcnS#3$^`, en donde tenemos caracteres especiales, letras y numeros. 

Necesitamos hacer lo siguiente: 

1. 🧑‍💻 Programa un bloque o función que retorne la cantidad de letras que existe en la cadena.
2. 👩‍💻 Programa un bloque o función que retorne la cantidad de dígitos que existe en la cadena.
3. 🧑‍💻 Dado un caracter ingresado por el usuario, el algoritmo debe contar cuantas veces se repite este caracter.


---

### Descripción de la solución :smiling_imp:
Para resolver este problema hemos creado 3 funciones diferentes que se encuentran documentadas en el codigo.

| Función <div style="width:250px"></div> | Descripción |
| --- | :--- |
|`count_letters(string:str)->int`| Recibe una cadena de caracteres y retorna el numero de letras en dicha cadena. Basicamente genera una lista de letras apartir de una list comprehensions validando los valores con el metodo `isalpha(): Valida si un caracter pertenece o no al alfabeto`| 
|`count_numbers(string:str)->int`|Recibe una cadena de caracteres y retorna la cantidad de numeros en la cadena, valida los caracteres con el metodo `isnumeric()`|
|`count_this(string:str, matching_char:str)->int`|Recibe un caracter y una cadena de caracteres, luego valida cuantos caracteres hay que hacen match con el caracter ingresado por el usuario, valida los caracteres con la función  `find_char`|
|`count_numbers(string:str)->int`|Recibe una cadena de caracteres y retorna la cantidad de numeros en la cadena, valida los caracteres con el metodo `isnumeric()`|
|`find_char(char:str, match:str)->bool`|Valida si un caracter es igual a otro|





---
### No te queda completamente claro? :confounded:
**Revisa este video de TikTok donde te lo explico mejor :** 
*Efectivamente aquí explico list comprehension* :flushed:




[<img src="https://res.cloudinary.com/marcomontalbano/image/upload/v1664299328/video_to_markdown/images/tiktok--7148110640102624517-c05b58ac6eb4c4700831b2b3070cd403.jpg" width = "250" height = "440">](https://www.tiktok.com/@steveeeeess/video/7148110640102624517?is_copy_url=1&is_from_webapp=v1)







Puedes encontrar a la AEIS en redes sociales como: [```@aeis_epn```](https://www.instagram.com/aeis_epn/)



`#30DaysOfCode #30DaysOfCodeByAEIS #30DoCodeAEIS #30DaysAEIS`

<a href="https://www.linkedin.com/in/gutembergsmendoza/">
    <img align="left" alt="Gutemberg S. Mendoza | LinkedIn " width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />
  </a>


