#crea una clase llamada Producto
#nombre, unidades y precio
#creas un producto camisa, 10, 9.95 de precio
#muestra el nombre de producto por consola

#crea un método de infoProducto. Muestra el nombre, unidades, precio y inventario valorado (uxp)

#práctica de sobreescritura.
#crea una clase llamada Servicio
#tiene un método llamado consultarDetalle que muestra. el servicio es básico.
#la empresa tiene dos servicios. estándar y premium. Son dos clases que derivan de Servicio
#la clase Estandar y Premium tienen un método llamado consultarDetalle y explican que son
#servicio estándar y premium respectivamente.
#pide por consola un servicio. Elegimos premium y te muestra el resultado de consultarDetalle

class Producto():
    def __init__(self,nombre,unidades,precio):
        self.nombre=nombre
        self.unidades=unidades
        self.precio=precio


    def infoProducto(self):
        print(f'Del producto {self.nombre} nos quedan {self.unidades} prendas con un precio de {self.precio} y un inventario valorado en {self.unidades * self.precio}')

producto1=Producto('Camisa', 10, 9.95)
producto1.infoProducto()



class Servicio:
    def consultarDetalle(self):
        print('El servicio es básico.')

class Estandar(Servicio):
    def consultarDetalle(self):
        print('Servicio Estándar')

class Premium(Servicio):
    def consultarDetalle(self):
        print('Servicio Premium')


tipoServicio=int(input('¿Que clase de servivio tiene Estandar(1) o Premium(2)? '))

match tipoServicio:

    case 1:
        estandar1=Estandar()
        estandar1.consultarDetalle()

    case 2:
        premium1=Premium()
        premium1.consultarDetalle()





