import os
from rich.console import Console
from rich.table import Table


class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def reducir_stock(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            return True
        return False
    
    def cambiar_precio(self,precio_nuevo):
        self.precio = precio_nuevo

class Carrito:
    def __init__(self):
        self.items = []

    def agregar_producto(self, producto, cantidad):
        if producto.reducir_stock(cantidad):
            self.items.append({"producto": producto, "cantidad": cantidad})
            print(f"{cantidad} unidades de {producto.nombre} añadidas al carrito.")
        else:
            print("No hay suficiente stock.")

    def mostrar_carrito(self):
        if not self.items:
            print("\nEl carrito está vacío.")
        else:
            #print("\nCarrito de compras:")
            console = Console()
            # Crear una tabla
            table = Table(title="Carrito de compras")

            table.add_column("Producto", style="cyan")
            table.add_column("Precio", justify="right", style="green")
            table.add_column("Cantidad", justify="right", style="magenta")
            table.add_column("precio", justify="right", style="magenta")

            total = 0
            for item in self.items:
                #print(f"{item['producto'].nombre} - ${item['producto'].precio} x {item['cantidad']}")
                table.add_row(str(item['producto'].nombre), str(item['producto'].precio), str(item['cantidad']), str(item['cantidad']* item['producto'].precio))
                total += item['cantidad']* item['producto'].precio
            table.add_row("Total", "","", str(total))
            console.print(table)

    def calcular_total(self):
        total = sum(item['producto'].precio * item['cantidad'] for item in self.items)
        return total

    def vaciar_carrito(self):
        self.items.clear()

class Tienda:
    def __init__(self):
        self.productos = [
            Producto("Anillo de Oro", 500, 10),
            Producto("Collar de Plata", 200, 5),
            Producto("Reloj de Lujo", 1000, 3),
            Producto("Pendientes de Diamante", 1500, 2)
        ]
        self.carrito = Carrito()

    def mostrar_productos(self):
        console = Console()
        print("\nProductos disponibles:")
        # Crear una tabla
        table = Table(title="Productos")

        table.add_column("id", justify="right",style="white")
        table.add_column("Nombre", style="cyan")
        table.add_column("Precio", justify="right", style="green")
        table.add_column("Stock", justify="right", style="magenta")

        # Agregar datos
        for i, producto in enumerate(self.productos):
            table.add_row(str(i+1),str(producto.nombre), str(producto.precio), str(producto.cantidad))
            #print(f"{i + 1}. {producto.nombre} - ${producto.precio} (Stock: {producto.cantidad})")
        console.print(table)

    def seleccionar_producto(self):
        self.mostrar_productos()
        try:
            seleccion = int(input("\nSelecciona el número del producto que deseas comprar: ")) - 1
            if seleccion < 0 or seleccion >= len(self.productos):
                print("Producto no válido.")
                return None
            return self.productos[seleccion]
        except ValueError:
            print("Entrada no válida.")
            return None

    def agregar_al_carrito(self):
        producto = self.seleccionar_producto()
        if producto:
            try:
                cantidad = int(input(f"¿Cuántas unidades de {producto.nombre} deseas comprar?: "))
                self.carrito.agregar_producto(producto, cantidad)
            except ValueError:
                print("Entrada no válida.")

    def finalizar_compra(self):
        if not self.carrito.items:
            print("\nEl carrito está vacío. No se puede finalizar la compra.")
            return

        self.carrito.mostrar_carrito()
        total = self.carrito.calcular_total()
        print(f"\nEl total a pagar es: ${total}")
        confirmacion = input("¿Deseas finalizar la compra? (s/n): ").lower()

        if confirmacion == 's':
            self.carrito.vaciar_carrito()
            print("\nCompra finalizada. ¡Gracias por tu compra!")
        else:
            print("\nCompra cancelada.")

    def mostrar_menu(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Mostrar productos")
            print("2. Agregar producto al carrito")
            print("3. Mostrar carrito")
            print("4. Finalizar compra")
            print("5. Salir")

            opcion = input("\nSelecciona una opción: ")

            if opcion == '1':
                os.system("cls")
                self.mostrar_productos()
            elif opcion == '2':
                os.system("cls")
                self.agregar_al_carrito()
            elif opcion == '3':
                os.system("cls")
                self.carrito.mostrar_carrito()
            elif opcion == '4':
                os.system("cls")
                self.finalizar_compra()
            elif opcion == '5':
                print("Gracias por usar el sistema de ventas. ¡Hasta luego!")
                break
            else:
                print("Opción no válida, por favor selecciona una opción correcta.")

# Ejecutar el programa
if __name__ == "__main__":
    tienda = Tienda()
    tienda.mostrar_menu()
