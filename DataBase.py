#5. Persistencia y manejo de datos

import mysql.connector

#-------------------- Establecer conexion con base de datos --------------------
def Conectar():
    return mysql.connector.connect(
        host="localhost",
        user="Adriel",
        password="Brocoli007",
        database="OnlyFiado"
        )

#-------------------- tablas inicializadas para el funcionamiento de la base de datos --------------------
#┌( ͝° ͜ʖ͡°)=> para poder realizar una conexion con la base de datos
# se necesita inicar la conexion cada vez que se use
# junto a ello se debe de dar un "cursor()" para ejecutar comandos SQL
# un execute para mandar los comandos
# "commit()" que guarda los datos en la base
# y se debe de cerrar para que no ande de llorona la base de datos
# como "cursor.close()" para cerrar el cursor
# y la conexion "Conecion.close()"


def IniciarTablas():
    Conexion = Conectar() # se conecta a la base de datos
    Cursor = Conexion.cursor() # crea un cursor para ejecutar comandos SQL
    
    TablaUsuarios = """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre_completo VARCHAR(100),
        usuario VARCHAR(50) UNIQUE,
        contrasena VARCHAR(50),
        rol VARCHAR(20)
    )
    """
    Cursor.execute(TablaUsuarios)
    
    TablaProductos = """
    CREATE TABLE IF NOT EXISTS productos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100),
        tipo VARCHAR(50),
        cantidad INT,
        precio DECIMAL(10, 2),
        id_vendedor INT,
        fecha_caducidad DATE,
        estado VARCHAR(50),
        FOREIGN KEY (id_vendedor) REFERENCES usuarios(id)
    )
    """
    Cursor.execute(TablaProductos)
    Conexion.commit()
    Cursor.close()
    
    
#-------------------- Inicio de secion --------------------
def Iniciar(Usuario, Contraseña):
    Conexion = Conectar()
    Cursor = Conexion.cursor()
        
    Consulta = "SELECT * FROM usuarios WHERE usuario = %s AND contrasena = %s"
    Cursor.execute(Consulta, (Usuario, Contraseña))
        
    Resultado = Cursor.fetchone() # se obtiene un solo registro que coincida
    Cursor.close()
    Conexion.close()
    return Resultado
    
def VerTodosLosProductos():
    try:
        Conexion = Conectar()
        Cursor = Conexion.cursor()
        
        Consulta = "SELECT id, nombre, tipo, cantidad, estado, precio FROM productos"   
                 
        Cursor.execute(Consulta)
        Resultados = Cursor.fetchall()
        Cursor.close()
        Conexion.close()
        return Resultados if Resultados else []
        
    except Exception as e:
        print(f"Error al cargar productos: {e}")
        return []
    
def VerMisProductos(IdVendedor):
    try:
        Conexion = Conectar()
        Cursor = Conexion.cursor()
        
        Consulta = "SELECT id, nombre, tipo, cantidad, precio, id_vendedor FROM productos WHERE id_vendedor = %s"
            
        Cursor.execute(Consulta, (IdVendedor,))
     
        Productos = Cursor.fetchall()
        Cursor.close()
        Conexion.close()
            
        return Productos if Productos else []
    except Exception as e:
        print(f"Error al cargar productos: {e}")
        return []
    

def ModificarProducto(IdProducto, CantidadComprada):
    Conexion = Conectar()
    Cursor = Conexion.cursor()
        
    Actualizacion = "UPDATE productos SET cantidad = cantidad - %s WHERE id = %s"
    Cursor.execute(Actualizacion, (CantidadComprada, IdProducto))
        
    Conexion.commit()
    Cursor.close()
    Conexion.close()
        
def Registrar(nombre, usuario, contra, rol):
    try:
        Conexion = Conectar()
        Cursor = Conexion.cursor()
        
        Sentencia = "INSERT INTO usuarios (nombre_completo, usuario, contrasena, rol) VALUES (%s, %s, %s, %s)"
        Valores = (nombre, usuario, contra, rol)
        
        Cursor.execute(Sentencia, Valores)
        Conexion.commit()
        Cursor.close()
        Conexion.close()
        return True
    except:
        return False


def AgregarProducto(nombre, tipo, cantidad, precio, id_vendedor, fecha_caducidad, estado):
    try:
        Conexion = Conectar()
        Cursor = Conexion.cursor()
        
        sql = """
        INSERT INTO productos 
        (nombre, tipo, cantidad, precio, id_vendedor, fecha_caducidad, estado) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        valores = (nombre, tipo, cantidad, precio, id_vendedor, fecha_caducidad, estado)
        
        Cursor.execute(sql, valores)
        Conexion.commit()
        Cursor.close()
        Conexion.close()
        return True
    except Exception as e:
        print(f"Error SQL: {e}")
        return False
    
def ModificarStock(CodigoBarras, NuevaCantidad):
    try:
        Conexion = Conectar()
        Cursor = Conexion.cursor()
        
        sql = "UPDATE productos SET cantidad = %s WHERE id = %s"
        
        valores = (NuevaCantidad, CodigoBarras)
        
        Cursor.execute(sql, valores)
        Conexion.commit()
        Cursor.close()
        Conexion.close()
        return True
    except Exception as e:
        print(f"Error Update: {e}")
        return False

def EliminarProducto(CodigoBarras):
    try:
        Conexion = Conectar()
        Cursor = Conexion.cursor()
        
        sql = "DELETE FROM productos WHERE id = %s"
        
        Cursor.execute(sql, (CodigoBarras,)) # La coma es importante en tuplas de 1 elemento
        Conexion.commit()
        Cursor.close()
        Conexion.close()
        return True
    except Exception as e:
        print(f"Error Delete: {e}")
        return False


def Compra(CodigoBarras):
    try:
        Conexion = Conectar()
        Cursor = Conexion.cursor()
        
        sql = "UPDATE productos SET cantidad = cantidad - 1 WHERE id = %s"
        
        Cursor.execute(sql, (CodigoBarras,))
        Conexion.commit()
        Cursor.close()
        Conexion.close()
        return True
    except Exception as e:
        print(f"Error Update: {e}")
        return False
    
    
if __name__ == "__main__":
    IniciarTablas()