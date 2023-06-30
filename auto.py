class Vehiculo:
    def __init__(self, tipo, patente, marca, precio, multas, fecha_registro, dueno):
        self.tipo = tipo
        self.patente = patente
        self.marca = marca
        self.precio = precio
        self.multas = multas
        self.fecha_registro = fecha_registro
        self.dueno = dueno


def grabar_vehiculo(vehiculos):
    tipo = input("Tipo de vehículo: ")
    patente = input("Patente: ")
    marca = input("Marca: ")
    precio = float(input("Precio: "))
    multas = []
    fecha_registro = input("Fecha de registro: ")
    dueno = input("Nombre del dueño: ")

    if len(marca) < 2 or len(marca) > 15:
        print("La marca debe tener entre 2 y 15 caracteres.")
        return

    if precio <= 5000000:
        print("El precio debe ser mayor a $5.000.000.")
        return

    vehiculo = Vehiculo(tipo, patente, marca, precio, multas, fecha_registro, dueno)
    vehiculos.append(vehiculo)
    print("Vehículo registrado correctamente.")


def buscar_vehiculo(vehiculos):
    patente = input("Ingrese la patente del vehículo: ")

    for vehiculo in vehiculos:
        if vehiculo.patente == patente:
            print("Información del vehículo:")
            print("Tipo:", vehiculo.tipo)
            print("Patente:", vehiculo.patente)
            print("Marca:", vehiculo.marca)
            print("Precio:", vehiculo.precio)
            print("Multas:", vehiculo.multas)
            print("Fecha de registro:", vehiculo.fecha_registro)
            print("Dueño:", vehiculo.dueno)
            return

    print("No se encontró ningún vehículo con la patente proporcionada.")


def imprimir_certificados(vehiculos):
    for vehiculo in vehiculos:
        print("Certificado de Emisión de contaminantes")
        print("Patente:", vehiculo.patente)
        print("Dueño:", vehiculo.dueno)
        print()

        print("Certificado de Anotaciones vigentes")
        print("Patente:", vehiculo.patente)
        print("Dueño:", vehiculo.dueno)
        print()

        print("Certificado de Multas")
        print("Patente:", vehiculo.patente)
        print("Dueño:", vehiculo.dueno)
        print()


def mostrar_menu():
    print("=== Auto Seguro - Registro de Vehículos ===")
    print("1. Grabar vehículo")
    print("2. Buscar vehículo")
    print("3. Imprimir certificados")
    print("4. Salir")


def main():
    vehiculos = []

    while True:
        mostrar_menu()
        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            grabar_vehiculo(vehiculos)
        elif opcion == "2":
            buscar_vehiculo(vehiculos)
        elif opcion == "3":
            imprimir_certificados(vehiculos)
        elif opcion == "4":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


if __name__ == "__main__":
    main()