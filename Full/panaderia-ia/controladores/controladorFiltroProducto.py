from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from modelos.conexionDB import Conexion

Ui_Form, QBase = uic.loadUiType('./vistas/filtroProducto.ui')

class ControladorFiltroProducto(QtWidgets.QMainWindow, Ui_Form):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_Form.__init__(self)
        super().setupUi(self)
        self.productos()
        self.mostar_all()
        self.cbxproducto.currentIndexChanged.connect(self.filtrar_producto)
        self.btntodos.clicked.connect(self.mostar_all)

    def mostar_all(self):

        row = 0
        fila = 0
        conexion = Conexion()
        cursor = conexion.cursor3()

        if True == True:

            sql = """SELECT p.codigo, p.nombre, WEEK(f.fecha_transacción), sum(dtt.cantidad)
                    FROM detalle_factura dtt INNER JOIN factura f
                    ON dtt.idfactura = f.idfactura
                    INNER JOIN producto p
                    on dtt.idproducto = p.idproducto
                    group by p.nombre, p.codigo, WEEK(f.fecha_transacción)
                    order by WEEK(f.fecha_transacción) asc;
                    """

            cursor.execute(sql)
            users = cursor.fetchall()  # Ya que retorna más de un registro
            conexion.cerrar_conexion()

            self.tablaproducto.setColumnCount(4)
            self.tablaproducto.setHorizontalHeaderLabels(['Codigo', 'Producto', 'Semana', 'Cantidad'])

            for use in users:
                fila = fila + 1

            self.tablaproducto.setRowCount(fila)

            for use in users:

                codigo = QtWidgets.QTableWidgetItem(str(use[0]))
                producto = QtWidgets.QTableWidgetItem(str(use[1]))
                semana = QtWidgets.QTableWidgetItem(str(use[2]))
                cantidad = QtWidgets.QTableWidgetItem(str(use[3]))

                self.tablaproducto.setItem(row, 0, codigo)
                self.tablaproducto.setItem(row, 1, producto)
                self.tablaproducto.setItem(row, 2, semana)
                self.tablaproducto.setItem(row, 3, cantidad)

                row = row + 1

        self.tablaproducto.verticalHeader().setVisible(False)
        self.tablaproducto.setGeometry(QtCore.QRect(75, 150, 524, 280))

    def productos(self):
        conexion = Conexion()
        cursor = conexion.cursor3()

        if True == True:

            sql = """SELECT DISTINCT(nombre) FROM producto ORDER BY nombre asc;"""

            cursor.execute(sql)
            product = cursor.fetchall()  # Ya que retorna más de un registro
            conexion.cerrar_conexion()

            for lista in product:
                self.cbxproducto.addItems(lista)            

    def filtrar_producto(self):

        row = 0
        fila = 0

        conexion = Conexion()
        cursor = conexion.cursor3()

        if True == True:

            sql = """SELECT WEEK(f.fecha_transacción), sum(dtt.cantidad)
                        FROM detalle_factura dtt INNER JOIN factura f
                        ON dtt.idfactura = f.idfactura
                        INNER JOIN producto p
                        on dtt.idproducto = p.idproducto
                        WHERE p.nombre = '{}'
                        group by WEEK(f.fecha_transacción)
                        order by WEEK(f.fecha_transacción);
                    """.format(self.cbxproducto.currentText())

            cursor.execute(sql)
            users = cursor.fetchall()  # Ya que retorna más de un registro
            conexion.cerrar_conexion()
            
            self.tablaproducto.setColumnCount(2)
            self.tablaproducto.setHorizontalHeaderLabels(['Semana', 'Cantidad'])

            for use in users:
                fila = fila + 1

            self.tablaproducto.setRowCount(fila)

            for use in users:

                semana = QtWidgets.QTableWidgetItem(str(use[0]))
                cantidad = QtWidgets.QTableWidgetItem(str(use[1]))

                self.tablaproducto.setItem(row, 0, semana)
                self.tablaproducto.setItem(row, 1, cantidad)

                row = row + 1
                
            self.tablaproducto.verticalHeader().setVisible(False)
            self.tablaproducto.setGeometry(QtCore.QRect(190, 150, 273, 290))
