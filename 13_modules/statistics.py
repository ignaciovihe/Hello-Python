# 8. Crea un módulo llamado "statistics" que tenga funciones para calcular la media y la mediana de una lista de números. Usa este módulo para calcular estos valores en una lista dada.

def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):

    sorted_numbers = sorted(numbers)

    if len(sorted_numbers) % 2 != 0:
        return sorted_numbers[len(sorted_numbers) // 2]
    else:
        middle1 = sorted_numbers[len(sorted_numbers)// 2 - 1]
        middle2 = sorted_numbers[len(sorted_numbers) // 2]
        return mean([middle1, middle2])

