import DataBase

#┌( ͝° ͜ʖ͡°)=> Este archivo usa Programación Orientada a Objetos (POO) para generar reportes
# Utilizamos Herencia, Polimorfismo y Encapsulación para organizar los datos de manera elegante

#---------------------------------------- Clases Base ----------------------------------------
#-------------------- Clase padre --------------------
class ProductoGenerico:
#┌( ͝° ͜ʖ͡°)=> Esta es la clase padre, contiene los atributos generales 
# que todos los productos van a tener


    def __init__(self, Nombre, Cantidad, Precio):
        self.Nombre = Nombre
        self.Cantidad = Cantidad
        self.Precio = float(Precio)


#-------------------- Método Base para Polimorfismo --------------------
#┌( ͝° ͜ʖ͡°)=> Este método será sobrescrito por las clases hijas
# permitiéndose el comportamiento polimórfico
    def ObtenerInfoDetallada(self):
        return f"Generico: {self.Nombre} | Stock: {self.Cantidad}"

#-------------------- Sobrecarga de Operadores --------------------
#┌( ͝° ͜ʖ͡°)=> Aquí sobrecargamos el operador "+" para sumar precios
# esto es parte del Polimorfismo, permitiendo operaciones personalizadas
    def __add__(self, OtroProducto):
        return self.Precio + OtroProducto.Precio
class Alimento(ProductoGenerico):
#┌( ͝° ͜ʖ͡°)=> Aquí sobrescribimos el método ObtenerInfoDetallada
# esto es POLIMORFISMO, cada clase hijo tiene su propia versión del método
    def ObtenerInfoDetallada(self):
        # Polimorfismo: Cambiamos el comportamiento según el tipo
    
        return f"Alimentos: {self.Nombre} (Revisar caducidad diaria)"

class Electronico(ProductoGenerico):
#┌( ͝° ͜ʖ͡°)=> Otra clase hija con su propia versión del método
# demostrando cómo diferentes tipos pueden comportarse diferente
    def ObtenerInfoDetallada(self):
        # Polimorfismo: Comportamiento específico para electrónicos
        return f"Tecnologia: {self.Nombre} (Manejar con cuidado)"

def GenerarReporteTxt():
    print("Iniciando generación de reporte POO...")
    
    #┌( ͝° ͜ʖ͡°)=> Traemos los datos crudos de la base de datos
    # Estos vienen como tuplas (filas) que necesitamos convertir a objetos
    Datos = DataBase.VerTodosLosProductos() 
    
    ListaObjetos = []

    #┌( ͝° ͜ʖ͡°)=> Convertimos Tuplas SQL -> Objetos Python
    # Esto es parte de la encapsulación, cada tupla se convierte en un objeto
    # con su propio comportamiento según su tipo
    
    # Traemos los datos crudos de la base de datos
    Datos = DataBase.VerTodosLosProductos() 
    
    ListaObjetos = []

##┌( ͝° ͜ʖ͡°)=> Convertimos Tuplas SQL -> Objetos Python
    for Prod in Datos:
        # Desempaquetamos los datos de la tupla
        # El "_" ignora el ID porque no lo necesitamos
        # Orden que viene de la BD: id, nombre, tipo, cantidad, estado, precio
        
        _, Nombre, Tipo, Cantidad, Estado, Precio = Prod
        
        #┌( ͝° ͜ʖ͡°)=> Creamos instancias según el tipo de producto
        # Esto es un ejemplo de creación dinámica de objetos
        # El tipo determina cuál clase se instancia
        if Tipo == "Alimentos":
            Objeto = Alimento(Nombre, Cantidad, Precio)
        elif Tipo == "Electronicos":
            Objeto = Electronico(Nombre, Cantidad, Precio)
        else:
            Objeto = ProductoGenerico(Nombre, Cantidad, Precio)
            
        ListaObjetos.append(Objeto)

    #┌( ͝° ͜ʖ͡°)=> Ahora redactamos el contenido que irá en el archivo
    # Todo esto se logra gracias a la organización POO
    try:
        with open("ReporteInventario.txt", "w", encoding="utf-8") as Archivo:
            # Escribimos el encabezado del reporte
            Archivo.write("=== REPORTE DE INVENTARIO (SISTEMA ONLYFIADO) ===\n")
            Archivo.write("Generado con Módulo de Objetos Polimórficos\n\n")
            
            ValorTotalInventario = 0
            
            #┌( ͝° ͜ʖ͡°)=> Iteramos sobre cada objeto y aplicamos POLIMORFISMO
            # Cada objeto responde diferente a ObtenerInfoDetallada()
            # según su clase (Alimento, Electronico, o Genérico)
            for Objeto in ListaObjetos:
                
                # Aquí ocurre la magia del Polimorfismo :)
                # El método ObtenerInfoDetallada() cambia según el tipo de objeto
                Linea = Objeto.ObtenerInfoDetallada()
                
                Archivo.write(Linea + "\n")
                Archivo.write(f"   Valor unitario: ${Objeto.Precio}\n")
                Archivo.write("-" * 30 + "\n")
                
                #Sumamos precios para obtener el total del inventario
                ValorTotalInventario += Objeto.Precio

            # Finalizamos el reporte con el valor total
            Archivo.write(f"\nVALOR TOTAL EN BODEGA: ${ValorTotalInventario:.2f}")
            
        return True
    except Exception as E:
        print(f"Error generando reporte: {E}")