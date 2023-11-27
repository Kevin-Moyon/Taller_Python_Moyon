import psutil

# Obtener la cantidad de memoria disponible
memoria_disponible = psutil.virtual_memory().available / (1024 * 1024)

# Obtener el porcentaje de uso de la memoria
memoria_usada = psutil.virtual_memory().percent

# Obtener el rendimiento de la red
rendimiento_red = psutil.net_io_counters().bytes_sent / (1024 * 1024)

# Obtener la temperatura del CPU (solo disponible en algunas plataformas)
try:
    temperatura_cpu = psutil.sensors_temperatures()['coretemp'][0].current
except AttributeError:
    temperatura_cpu = "No disponible en esta plataforma"

# Imprimir la cantidad de memoria disponible, el porcentaje de uso de la memoria, el rendimiento de la red y la temperatura del CPU
print(f"Memoria disponible: {memoria_disponible:.2f} MB")
print(f"Porcentaje de uso de la memoria: {memoria_usada:.2f}%")
print(f"Rendimiento de la red: {rendimiento_red:.2f} MB")
print(f"Temperatura del CPU: {temperatura_cpu}")