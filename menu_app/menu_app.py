#PRUEBA N°2 PROGRAMACIÓN WEB
#DILAN GATICA

def agregar_compra(producto, precio):
    producto.append(precio)
    print(f"Producto agregado correctamente!")

def mostrar_compras(producto):
    if len(producto):
        print("Todavía no has agregado ningún producto.")
    else:
        print("REGISTRO DE COMPRAS:")
        for i, producto in enumerate(producto):
            print(f"Compra {i}: ${producto:.2f}")


def mostrar_total(compras):
    total = sum(compras)
    print(f"Total gastado: ${total:.2f}")

def main():
    compras = []
    total_gastado = 0

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1),(2),(3),(4): ")

        if opcion == "1":
            valor = float(input("Ingrese el monto: $"))
            agregar_compra(compras, valor)
            total_gastado += valor
        elif opcion == "2":
            mostrar_compras(compras)
        elif opcion == "3":
            mostrar_total(compras)
        elif opcion == "4":
            print("Hasta pronto.")
            break
        else:
            print("Error. Seleccione una opción válida")

def mostrar_menu():
    print("Menú:")
    print("1. Agregar compra")
    print("2. Mostrar compras")
    print("3. Mostrar total gastado")
    print("4. Salir")

if __name__ == "__main":
    main()