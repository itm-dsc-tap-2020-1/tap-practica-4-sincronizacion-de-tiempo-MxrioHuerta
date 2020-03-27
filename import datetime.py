import datetime
from time import ctime
import ntplib
import os

servidor_tiempo = "time-e-g.nist.gov"
cliente_ntp = ntplib.NTPClient()

t1 = datetime.datetime.now()
print("Tiempo de inicio de la peticion: " + str(t1))
respuesta = cliente_ntp.request(servidor_tiempo)
t2 = datetime.datetime.now()
print("Tiempo de llegada de la peticion: " + str(t2))

hora_servidor = datetime.datetime.strptime(
    ctime(respuesta.tx_time), "%a %b %d %H:%M:%S %Y")
Ajuste = (t2-t1)/2
Reloj = hora_servidor + Ajuste

print("Tiempo que se recibió del servidor: " + str(hora_servidor))
print("Ajuste: " + str(Ajuste))
print("Hora cambiada: " + str(Reloj))
os.system(f"date --set '{Reloj}'")
