from datetime import date, time, datetime, timedelta

# 1. Crea una variable con la fecha y hora actual.

now = datetime.now()
print(now)

# 2. Imprime solo el año, mes y día de la fecha actual.

print(now.year)
print(now.month)
print(now.day)

# 3. Crea una fecha específica: 25 de diciembre de 2025 y muéstrala.

christmas = datetime(2025, 12, 25)
print(christmas)

# 4. Muestra solo la hora, los minutos y los segundos de un objeto time.

hour = time(14, 30, 15)
print(hour.hour)
print(hour.minute)
print(hour.second)

# 5. Calcula cuántos días faltan para el 1 de enero del año siguiente.

today = date.today()
year_init = date(today.year + 1, 1, 1)
diff = year_init - today
print(diff.days)

# 6. Crea una función que reciba una fecha y devuelva su timestamp.


def get_timestamp(date):
    return date.timestamp()


print(get_timestamp(datetime.now()))

# 7. Suma 30 días a la fecha actual usando timedelta.

future_date = datetime.now() + timedelta(days=30)
print(future_date)

# 8. Crea una fecha y añade 1 mes (consejo: hazlo sumando 30 días como simplificación).

init_date = datetime(2024, 3, 15)
new_date = init_date + timedelta(days=30)
print(new_date)

# 9. Compara dos fechas y muestra cuál es anterior.

date1 = datetime(2023, 6, 1)
date2 = datetime(2024, 1, 1)

if date1 < date2:
    print("date1 es anterior")
else:
    print("date2 es anterior")

# 10. Crea una lista con varias fechas y ordénalas cronológicamente.

dates = [
    datetime(2022, 5, 1),
    datetime(2020, 1, 15),
    datetime(2023, 12, 31),
]

sorted_dates = sorted(dates)

for f in sorted_dates:
    print(f)
