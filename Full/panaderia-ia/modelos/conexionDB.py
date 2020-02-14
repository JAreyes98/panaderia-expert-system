import pymysql
import pymysql.cursors

class Conexion():

    def __init__(self):
        self.conexionIsOpened = False
        self.coneccion = None
        self.datosConexion = ()


    def conctar(self, datosConexion):
        self.datosConexion = datosConexion
        if(not self.conexionIsOpened):
            self.coneccion = pymysql.connect(host=datosConexion[0],
                      port=datosConexion[1],
                      db=datosConexion[2],
                      user=datosConexion[3],
                      password=datosConexion[4],
                      cursorclass=pymysql.cursors.DictCursor)
            
            self.conexionIsOpened = True

        return self.coneccion

    def conectarDefault(self):
        return self.conctar(('localhost',33060,'pastelería','root','Arigrande_98'))
    
    def cursor(self):
        if(len(self.datosConexion) == 0):
            return self.conectarDefault().cursor()
        return self.conctar(self.datosConexion).cursor()

    def cerrarConexion(self):
        if(self.conexionIsOpened):
            self.coneccion.close()
            self.conexionIsOpened = False

    # Otro metodo

    def conexion(self):
        coneccion = pymysql.connect(
            user='root',
            password='Arigrande_98',
            db='pastelería',
            charset='utf8mb4',
            port=33060
        )

        if coneccion.open == True:
            return coneccion
        else:
            print('Error')

    def cursor3(self):

        if self.conexion().open == True:
            cursor = self.conexion().cursor()
            return cursor
        else:
            print('Error')

    def cerrar_conexion(self):
        if(self.conexion().open == True):
            self.conexion().close()


        