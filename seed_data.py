from primermvt.models import Familiar
from datetime import datetime

hoy = datetime.now()
fecha= hoy.date()

Familiar(nombre="Lionel", apellido= "Messi", edad="35", dni=123123, fecha_ingreso=fecha).save()
Familiar(nombre="Dibu", apellido= "Martinez", edad="30", dni=234234, fecha_ingreso=fecha).save()
Familiar(nombre="Nicolás", apellido= "Otamendi", edad="34", dni=345345, fecha_ingreso=fecha).save()
Familiar(nombre="Rodrigo", apellido= "De Paul", edad="28", dni=456456, fecha_ingreso=fecha).save()
print("Se cargo con éxito los usuarios de pruebas")