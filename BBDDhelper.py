from tokenize import String

import pymysql

# Declaración de clases de acceso a datos

conexion = pymysql.connect(host="localhost", port=3306, user="root",
                           passwd="xxxx", db="dam1")
cursor = conexion.cursor()


def insertar_militante(nombre: String, edad: String, pago: String):
    militante = (nombre, edad, pago)

    try:
        cursor.execute("INSERT INTO militante VALUES (NULL, %s, %s, %s)", militante)
        conexion.commit()
        # print("La información ha sido almacenada correctamente.")
    except:
        print("No se ha podido almacenar la información introducida.")

    # conexion.close()


def consultar_edad(edad: int):
    try:
        cursor.execute("Select id, nombre FROM militante where edad =" + str(edad))
        return cursor.fetchall()

    except:
        print("No se halló gran cosa.")


def consultar_id(iden: int):
    try:
        cursor.execute("SELECT id, nombre, edad, pago FROM militante where id =" + str(iden))
        militante = cursor.fetchone()

        return "El militante con id " + str(militante[0]) + " es " + \
               str(militante[1]) + ", tiene " + str(militante[2]) + " años y " + str(militante[3] +
                                                                                     " está al corriente de pago")

    except:
        print("No se halló nada.")
