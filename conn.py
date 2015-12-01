__author__ = 'aferreiradominguez'
import sqlite3 as dbapi

#version api
print(dbapi.apilevel)
#0-3 nivel seguridade do modulo para usar fios
print(dbapi.threadsafety)
#Indica sintaxe para a insercion de param
print(dbapi.paramstyle)
try:
    bbdd=dbapi.connect("basedatos.dat")
except (InterfaceError,dbapi.DatabaseError):
    print("Error de connexion")
else:
    print("conn success")
finally:
    print("progreso de conn BD finalizado")

print(bbdd)

cursor=bbdd.cursor()

#cursor.execute("""create table empleados (dni text primary key, nome text ,departamento text,sueldo integer)""")

#cursor.execute("""insert into empleados values('111111111-Z','paco','informatico',1500)""")

#cursor.execute("""insert into empleados values('111111112-Z','lolololo','celtista',3000)""")


#bbdd.commit()

cursor.execute("""select * from empleados""")
for result in cursor:
    print("Dni: "+result[0]+"nome: "+result[1]+"profesion: "+result[2]+"sueldo: "+str(result[3]))
bbdd.close()