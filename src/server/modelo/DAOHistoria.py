from modelo.Historia import Historia
from modelo.InterfaceDAO import InterfaceDAO
from modelo.Singleton import Singleton

import MySQLdb

@Singleton
class DAOHistoria(InterfaceDAO):

    def __init__(self):
        self.preparar_ddbb()

    def preparar_ddbb(self):
        query = "DROP TABLE IF EXISTS Historias"
        self.ejecutar_query( query )

        query = """ CREATE TABLE Historias (
                    id                    INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                    nombre_historia       CHAR(30) NOT NULL,
                    latitud_historia      DECIMAL(10, 8)  NOT NULL,
                    longitud_historia     DECIMAL(10, 8)  NOT NULL,
                    zoom                  INT(6)  NOT NULL,
                    descripcion_historia  CHAR(300) NOT NULL) """
        self.ejecutar_query( query )


        query = """INSERT INTO Historias(nombre_historia, latitud_historia, longitud_historia, zoom, descripcion_historia)
                   VALUES('Historia 1', 37.198366, -3.624976, 15, 'Soy la descripcion')"""
        self.execute_query( query )

    def ejecutar_query(self, query):
        db = MySQLdb.connect(host='us-cdbr-gcp-east-01.cleardb.net',
                             user='b761ae150766d3',
                             passwd='4bcf3d10',
                             db='gcp_ca2ad2566039a3f0f01c',
                             port=3306)

        cursor = db.cursor()

        try:
            cursor.execute(query)
        except Exception as error:
            cursor.close()
            db.close()
            raise error

        db.commit()
        result = cursor.fetchall()
        cursor.close()
        db.close()

        return result
