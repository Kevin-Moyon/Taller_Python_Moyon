import psutil
import socket

def obtener_informacion_remota(ip):
    try:
        # Conectar al servicio en la máquina remota
        with socket.create_connection((ip, 5000), timeout=1) as sock:
            # Obtener la cantidad de memoria disponible
            memoria_disponible = psutil.virtual_memory().available / (1024 * 1024)

            # Obtener el porcentaje de uso de la memoria
            memoria_usada = psutil.virtual_memory().percent

            # Obtener el rendimiento de la red
            rendimiento_red = psutil.net_io_counters().bytes_sent / (1024 * 1024)

            # Obtener la temperatura del CPU (puede no estar disponible en todas las plataformas)
            try:
                temperatura_cpu = psutil.sensors_temperatures()['coretemp'][0].current
            except (AttributeError, KeyError, IndexError):
                temperatura_cpu = "No disponible en esta plataforma"

            # Devolver los datos recopilados
            return memoria_disponible, memoria_usada, rendimiento_red, temperatura_cpu
    except Exception as e:
        return f"No se pudo conectar a {ip}: {e}"

# Direcciones IP de las máquinas remotas
ip_remota_1 = '10.3.21.191'
ip_remota_2 = '10.3.21.193'

# Obtener la información remota para la primera máquina
resultado_1 = obtener_informacion_remota(ip_remota_1)

# Imprimir los resultados para la primera máquina
print(f"Información para {ip_remota_1}:")
if isinstance(resultado_1, tuple):
    memoria_disponible, memoria_usada, rendimiento_red, temperatura_cpu = resultado_1
    print(f"Memoria disponible: {memoria_disponible:.2f} MB")
    print(f"Porcentaje de uso de la memoria: {memoria_usada:.2f}%")
    print(f"Rendimiento de la red: {rendimiento_red:.2f} MB")
    print(f"Temperatura del CPU: {temperatura_cpu}")
else:
    print(resultado_1)

# Obtener la información remota para la segunda máquina
resultado_2 = obtener_informacion_remota(ip_remota_2)

# Imprimir los resultados para la segunda máquina
print(f"\nInformación para {ip_remota_2}:")
if isinstance(resultado_2, tuple):
    memoria_disponible, memoria_usada, rendimiento_red, temperatura_cpu = resultado_2
    print(f"Memoria disponible: {memoria_disponible:.2f} MB")
    print(f"Porcentaje de uso de la memoria: {memoria_usada:.2f}%")
    print(f"Rendimiento de la red: {rendimiento_red:.2f} MB")
    print(f"Temperatura del CPU: {temperatura_cpu}")
else:
    print(resultado_2)
