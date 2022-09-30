from calendar import month
from datetime import date
import math

# Codigo de cada dia
DAYS = {
    1:'Lunes',
    2:'Martes',
    3:'Miercoles',
    4:'Jueves',
    5:'Viernes',
    6:'Sabado',
    7:'Domingo',
    0:'Domingo'
}

# Codigo de cada mes segun: https://cs.uwaterloo.ca/~alopez-o/math-faq/node73.html
MONTHS_CODE = ['non', ['Enero', 0], ['Febrero',3], ['Marzo',3], 
              ['Abril',6], ['Mayo',1], ['Junio',4],['Julio',6], 
              ['Agosto',2], ['Septiembre',5], ['Octubre',0], 
              ['Noviembre',3],['Diciembre',5]]
# From scratch
def get_day_week(date:str):
    date_array = date.split("/")

    # Separa los digitos
    year_digits = date_array[2][2:]
    month_digit = int(date_array[1])
    day_digit = int(date_array[0])

    # Verifica si es Enero o febrero y si es bisiesto
    leap_year_constant = 0
    if(int(date_array[2])%4 == 0) and (month_digit!= 1 or month_digit!=2):
        leap_year_constant = 1
    
    # Calcula year_code, month_code y century_code
    x = float(year_digits) * (25/100)
    x = int(x) - leap_year_constant
    day = (x + int(year_digits)) % 7 
    year_code = day
    month_code = MONTHS_CODE[month_digit][1]
    century_code = 6

    final_day_code = (year_code + month_code + century_code + day_digit - leap_year_constant) % 7

    # Devuelve el día de la semana que es
    return(DAYS[final_day_code])
