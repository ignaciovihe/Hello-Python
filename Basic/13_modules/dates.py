# 10 Crea un módulo llamado "dates" que contenga funciones para obtener la fecha actual y calcular la diferencia entre dos fechas. Usa este módulo en un programa para mostrar la fecha actual y la diferencia entre dos fechas específicas.

from datetime import datetime, date

def get_date():
    return datetime.now().date()

def difference_of_dates(my_date1, my_date2):
    date1 = date(*my_date1)
    date2 = date(*my_date2)
    return abs((date1 - date2).days)

"""
    OTRA SOLUCIÓN:(Cuando se pasan las fechas en formato YYYY-MM-DD)
    def date_difference(date1, date2):
    d1 = datetime.strptime(date1, "%d-%m-%Y")
    d2 = datetime.strptime(date2, "%d-%m-%Y")
    return abs((d2 - d1).days)"""