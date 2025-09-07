from  datetime import datetime, date, time, timedelta
import random

# 1. Crea una variable con la fecha y hora actual.
current_time = datetime.now()
print(current_time)
print()

# 2. Imprime solo el año, mes y día de la fecha actual.
print(current_time.date())
print(current_time.year)
print(current_time.month)
print(current_time.day)
print()

# 3. Crea una fecha específica: 25 de diciembre de 2025 y muéstrala.
my_date = date(2025, 12, 25)
print(my_date)
print()

# 4. Muestra solo la hora, los minutos y los segundos de un objeto time.
print(current_time.strftime("%H:%M:%S"))
print(current_time.time().replace(microsecond=0))
print()

hour = time(13,18,23)
print(hour)
print(hour.hour)
print(hour.minute)
print(hour.second)
print()

# 5. Calcula cuántos días faltan para el 1 de enero del año siguiente.
today = datetime.now().date()
next_year = today.year + 1
first_day_of_new_year = date(next_year, 1, 1)
print(f"Faltan {(first_day_of_new_year - today).days} dias para el año {next_year}")
print()

# 6. Crea una función que reciba una fecha y devuelva su timestamp.
def get_timestamp(date: datetime):
    return date.timestamp() # Número de segundos que han transcurrido desde la ëpoca Unix (1/1/1970)

print(get_timestamp(datetime.now()))
print()

# 7. Suma 30 días a la fecha actual usando timedelta.
today = date.today()
new_date = today + timedelta(days=30)
print(f"Hoy: {today}")
print(f"Dentro de 30 días: {new_date}")
print()

# 8. Crea una fecha y añade 1 mes (consejo: hazlo sumando 30 días como simplificación).
first_date = date(2028,2,23)
new_date = first_date + timedelta(days=30)
print(f"Primera fecha: {first_date} - Un mes después: {new_date}")
print()

# 9. Compara dos fechas y muestra cuál es anterior.
first_date = date(2022,2,23)
second_date = date(2022,2,22)
print(first_date) if first_date < second_date else print(second_date)
print()


# 10. Crea una lista con varias fechas y ordénalas cronológicamente.
dates = []
start = date(1985,2,23)
end = date.today()

days_range = (end - start).days

for _ in range(10):
    random_days = random.randint(0, days_range)
    dates.append(start + timedelta(days=random_days))

sorted_dates = sorted(dates)
for element in sorted_dates:
    print(element)



