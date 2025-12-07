#8. Interfaz interactiva

import customtkinter as ctk
import Estilos
import DataBase
import VentanaEmergente
import ReportePOO
from datetime import datetime, timedelta 



class OnlyFiado(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        #Mausqueherramienta misteriosa que usaremas mas tarde
        self.IdUsuario = None
        
        #Condfiguracion de la ventana
        self.title("OnlyFiado")
        self.geometry("1280x800")
        self.configure(fg_color=Estilos.Fondo) #Color de fondo
        
        #-------------------- Frames --------------------
        self.FrameInicio = ctk.CTkFrame(self, fg_color="transparent")   
        self.FrameRegistro = ctk.CTkFrame(self, fg_color="transparent")
        
        self.FramePaginaCompradores = ctk.CTkFrame(self, fg_color="transparent")
        self.FramePaginaVendedores = ctk.CTkFrame(self, fg_color="transparent")
        #-------------------- Paginas Existentes --------------------
        self.Inicio()
        self.Registro()
        
        self.PaginaCompradores()
        self.PaginaVendedores()
        
        #-------------------- Pagina principal --------------------
        self.FrameInicio.pack(fill="both", expand=True)
        
#----------------------------------------- Retornos ----------------------------------------
#┌( ͝° ͜ʖ͡°)=> Para poder realizar un retorno se tiene que mencionar el frame del que se viene
# junto a su extencion "pack_forget"
# seguido del frame al que se quiere ir y dado los valores "(fill="both", expand=True)"

    def VolverLogin(self):
        self.FrameRegistro.pack_forget()
        self.FramePaginaCompradores.pack_forget()
        self.FramePaginaVendedores.pack_forget()
        self.FrameInicio.pack(fill="both", expand=True)
        
    def VolverRegistro(self):
        self.FrameInicio.pack_forget()
        self.FrameRegistro.pack(fill="both", expand=True)
    def IrCompradores(self):
        self.FrameInicio.pack_forget()
        self.FramePaginaCompradores.pack(fill="both", expand=True)
        
        self.VerProductos()
        
    def IrVendedores(self):
        self.FrameInicio.pack_forget()
        self.FramePaginaVendedores.pack(fill="both", expand=True)
        
        self.MisProductos()
        
#---------------------------------------- Pagina Principal ----------------------------------------
    def Inicio(self,):
        #Tutulo
#┌( ͝° ͜ʖ͡°)=> Para poder agrgar cualquier witget despues de incorporar dendro de un frame
# es necesario especificar que esta desntro de ese frame
        self.Titulo = ctk.CTkLabel(self.FrameInicio, #aqui, junto al self
            text= "OnlyFiado",
            font= Estilos.Titulos,
            fg_color= Estilos.FondoTitulo,
            text_color= Estilos.ColorTitulo,
            justify= "center",
            height= Estilos.AltoTitulo, 
            width= Estilos.AnchoTitulo,
            ) 
        self.Titulo.pack_propagate(False)
        self.Titulo.pack()
        
#al final se le da su respectivo su respectivo cierre
# utilizando "self.", seguido del nombre puesto anteriormente"
#┌( ͝° ͜ʖ͡°)=> es este caso tambien se utiliza ".pack_propagate(False)" para que solo se expanda por
#las dimenciones dadas en "height" y "width"
    #Subtitulo
        self.Subtitulo = ctk.CTkLabel(self.FrameInicio,
            text="Bienvenido a OnlyFiado, Malvados y Asociados S.A. \nLa mejor tienda de fiados en todo el país.",
            font=Estilos.Subtitulos,
            text_color= Estilos.ColorSubtitulo, 
            justify= "center",
            height= Estilos.AltoSubtitulo,
            width= Estilos.AnchoSubtitulo,
            )
        self.Subtitulo.pack_propagate(False)
        self.Subtitulo.pack()

        #-------------------- Inicio de sesion --------------------
        self.ObtenerUsuario = ctk.CTkEntry(self.FrameInicio,
            placeholder_text="Usuario",
            font= Estilos.Texto,
            width= 400,
            height= 50,
            )
        self.ObtenerUsuario.pack(padx=50, pady=10) #Aca si se le pone
#┌( ͝° ͜ʖ͡°)=> "padx y pady" representan el espacio de los witget
# "padx" representa el eje x, mientras que "pady" representa el eje y
        
        self.ObtenerContraseña = ctk.CTkEntry(self.FrameInicio,
            placeholder_text="Contraseña",
            font= Estilos.Texto,
            width= 400,
            height= 50,
            show="*"
            )
        self.ObtenerContraseña.pack(padx=50, pady=10)
        
        self.BotonSecion  = ctk.CTkButton(self.FrameInicio,
            text="Iniciar Sesión",
            font= Estilos.Botones,
            fg_color= Estilos.ColorBoton,
            text_color= Estilos.ColorTextoBoton,
            height= Estilos.AltoBoton,
            width= Estilos.AnchoBoton,
            command= self.IniciarSesion
            )
        self.BotonSecion.pack(padx=50, pady=20)
        
        self.Pregunta = ctk.CTkLabel(self.FrameInicio,
            text="¿No tienes una cuenta?",
            font=Estilos.Texto,
            text_color= Estilos.ColorTitulo,
            justify= "center",
            height= Estilos.AltoPregunta,
            width= Estilos.AnchoPregunta,
            )
        self.Pregunta.pack_propagate(False)
        self.Pregunta.pack(side="top", pady=10)
        
        self.BotonRegistro  = ctk.CTkButton(self.FrameInicio,
            text="Pos a registrarse papi",
            font= Estilos.Botones,
            fg_color= Estilos.ColorBotonEspecial,
            text_color= Estilos.ColorTextoBoton,
            height= Estilos.AltoBoton,
            width= Estilos.AnchoBoton,
            command= self.VolverRegistro
            )
        self.BotonRegistro.pack_propagate(False)
        self.BotonRegistro.pack(side="top")
        
        
#---------------------------------------- Pagina de registro ----------------------------------------
    def Registro(self):
    
        self.Titulo = ctk.CTkLabel(self.FrameRegistro,
            text= "Registro",
            font= Estilos.Titulos,
            fg_color= Estilos.FondoTitulo,
            text_color= Estilos.ColorTitulo,
            justify= "center",
            height= Estilos.AltoTitulo, 
            width= Estilos.AnchoTitulo,
            ) 
        self.Titulo.pack_propagate(False)
        self.Titulo.pack()
    
        self.ParrafoRegistro = ctk.CTkLabel(self.FrameRegistro,
            text="Por favor cuentanos de ti",
            font=Estilos.Subtitulos,
            text_color= Estilos.ColorSubtitulo, 
            justify= "center",
            height= 50,
            width= Estilos.AnchoSubtitulo,
            )
        self.ParrafoRegistro.pack_propagate(False)
        self.ParrafoRegistro.pack()

        self.RegistrarNombre = ctk.CTkEntry(self.FrameRegistro,
            placeholder_text="Nombre",
            font= Estilos.Texto,
            width= 400,
            height= 50,
            )
        self.RegistrarNombre.pack(padx=10, pady=10)
    
        self.RegistrarUsuario = ctk.CTkEntry(self.FrameRegistro,
            placeholder_text="Usuario",
            font= Estilos.Texto,
            width= 400,
            height= 50,
            )
        self.RegistrarUsuario.pack(padx=50, pady=10)

        self.RegistrarContraseña = ctk.CTkEntry(self.FrameRegistro,
            placeholder_text="Contraseña",
            font= Estilos.Texto,
            width= 400,
            height= 50,
            show="*"
            )
        self.RegistrarContraseña.pack(padx=50, pady=10)
        

        self.RegistrarRol = ctk.CTkLabel(self.FrameRegistro,text="¿Pa' qué se quiere registrar?", text_color="white")
        self.RegistrarRol.pack()
        
        self.RegistrarRoles = ctk.StringVar(value="Comprador") # Por defecto Comprador
        
        
        self.RadioComprador = ctk.CTkRadioButton(self.FrameRegistro,text="Quiero Comprar", variable=self.RegistrarRoles, value="Comprador")
        self.RadioComprador.pack(pady=5)
        self.RadioVendedor = ctk.CTkRadioButton(self.FrameRegistro, text="Quiero Vender", variable=self.RegistrarRoles, value="Vendedor")
        self.RadioVendedor.pack(pady=5)
            
        self.BotonRegistro  = ctk.CTkButton(self.FrameRegistro,
            text="Registrame, pero YAAAA",
            font= Estilos.Botones,
            fg_color= Estilos.ColorBoton,
            text_color= Estilos.ColorTextoBoton,
            height= Estilos.AltoBoton,
            width= Estilos.AnchoBoton,
            command= self.Registrar
            )
        self.BotonRegistro.pack_propagate(False)
        self.BotonRegistro.pack(side="top")
        
        self.PreguntaRegistro = ctk.CTkLabel(self.FrameRegistro,
            text="¿Ya tienes una cuenta?",
            font=Estilos.Texto,
            text_color= Estilos.ColorTitulo,
            justify= "center",
            height= Estilos.AltoPregunta,
            width= Estilos.AnchoPregunta,
            )
        self.PreguntaRegistro.pack_propagate(False)
        self.PreguntaRegistro.pack(side="top", pady=10)
        
        self.BotonVolver  = ctk.CTkButton(self.FrameRegistro,
            text="Volver al inicio",
            font= Estilos.Botones,
            fg_color= Estilos.ColorBotonEspecial,
            text_color= Estilos.ColorTextoBoton,
            height= Estilos.AltoBoton,
            width= Estilos.AnchoBoton,
            command= self.VolverLogin
            )
        self.BotonVolver.pack_propagate(False)
        self.BotonVolver.pack(side="top")

#---------------------------------------- Pagina de compradores ----------------------------------------

    def PaginaCompradores(self):
        self.TituloCompradores = ctk.CTkLabel(self.FramePaginaCompradores,
            text= "OnlyFiado",
            font= Estilos.Titulos,
            fg_color= Estilos.FondoTitulo,
            text_color= Estilos.ColorTitulo,
            justify= "center",
            height= Estilos.AltoTitulo, 
            width= Estilos.AnchoTitulo,
            ) 
        self.TituloCompradores.pack_propagate(False)
        self.TituloCompradores.pack()

        self.ParrafoRegistro = ctk.CTkLabel(self.FramePaginaCompradores,
            text="¿Miras algo que te interese?",
            font=Estilos.Subtitulos,
            text_color= Estilos.ColorSubtitulo, 
            justify= "center",
            height= 50,
            width= Estilos.AnchoSubtitulo,
            )
        self.ParrafoRegistro.pack_propagate(False)
        self.ParrafoRegistro.pack()
        
        self.Catalogos = ctk.CTkScrollableFrame(
            master=self.FramePaginaCompradores,
            width=100,
            height=500 
            )
        self.Catalogos.pack(fill="both", expand=True)
        

#---------------------------------------- Pagina de vendedores ----------------------------------------
    def PaginaVendedores(self):
#┌( ͝° ͜ʖ͡°)=> se pueden separar las paginas en secciones, para esto nos apoyamos 
# de otro "CTkFrame",
        # Indicamos la primera columna (la de la izquierda)
        # Para el Catálogo y le damos más espacio por ser lo pricipal
        self.ColumnaIzquierda = ctk.CTkFrame(self.FramePaginaVendedores, fg_color="transparent")
        self.ColumnaIzquierda.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        
        # Creamos la columna de la derecha para los Botones
        self.ColumnaDerecha = ctk.CTkFrame(self.FramePaginaVendedores,fg_color="transparent")
        self.ColumnaDerecha.pack(side="right", fill="both", padx=10, pady=10)
        
#┌( ͝° ͜ʖ͡°)=> ahora solo tenemos que especificar en cada uno de los demas witgets 
# donde deberian de ir (izquierda o derecha)
        self.TituloVendedores = ctk.CTkLabel(self.ColumnaDerecha, # como aqui
            text= "OnlyFiado",
            font= Estilos.Titulos,
            fg_color= Estilos.FondoTitulo,
            text_color= Estilos.ColorTitulo,
            justify= "center",
            height= Estilos.AltoTitulo, 
            width= 150,
            ) 
        self.TituloVendedores.pack(pady=(0, 10))
        
        self.ParrafoRegistro = ctk.CTkLabel(self.ColumnaDerecha,
            text="Bienvenido a la edicion de sus Productos",
            font=Estilos.Subtitulos,
            text_color= Estilos.ColorSubtitulo, 
            justify= "center",
            height= 50,
            width= 150,
            )
        self.ParrafoRegistro.pack(pady=(0, 30))
        

        self.Catalogo = ctk.CTkScrollableFrame(
            master=self.ColumnaIzquierda,
            width=100,
            height=500 
            )
        self.Catalogo.pack(fill="both", expand=True)
        
        
        
        self.BotonAgregar  = ctk.CTkButton(self.ColumnaDerecha,
            text="Agregar producto",
            font= Estilos.BotonesVendedores,
            fg_color= Estilos.FondoTitulo,
            text_color= Estilos.ColorTextoBoton,
            height= Estilos.AltoBotonVendedores,
            width= Estilos.AnchoBotonVendedores,
            command= self.VentanaNuevoProducto
            )
        self.BotonAgregar.pack(pady=15, fill="x")
        
        self.BotonModificar  = ctk.CTkButton(self.ColumnaDerecha,
            text="Modificar Productos",
            font= Estilos.BotonesVendedores,
            fg_color= Estilos.FondoTitulo,
            text_color= Estilos.ColorTextoBoton,
            height= Estilos.AltoBotonVendedores,
            width= Estilos.AnchoBotonVendedores,
            command= self.VentanaModificarProductos
            )
        self.BotonModificar.pack(pady=20, fill="x")

        self.BotonSalir  = ctk.CTkButton(self.ColumnaDerecha,
            text="Cerrar seción",
            font= Estilos.BotonesVendedores,
            fg_color= Estilos.ColorBotonCerrar,
            text_color= Estilos.ColorTextoBoton,
            height= Estilos.AltoBotonVendedores,
            width= Estilos.AnchoBotonVendedores,
            command= self.VolverLogin
            )
        self.BotonSalir.pack(pady=20, fill="x")
        
        self.BotonReporte = ctk.CTkButton(self.ColumnaDerecha,
            text="Generar Reporte POO",
            font= Estilos.BotonesVendedores,
            fg_color= Estilos.ColorBotonEspecial,
            text_color="white",
            height= 50,
            command= self.GenerarReporteInteligente
            )
        self.BotonReporte.pack(pady=15, fill="x")

#---------------------------------------- Ventanas de apoyo para los compradores ----------------------------------------
#-------------------- Agregar producto nuevo --------------------
    def VentanaNuevoProducto(self):
        VentanaEmergente = ctk.CTkToplevel() 
        VentanaEmergente.title ("Agregar productos")
        VentanaEmergente.geometry("1280x720")
        VentanaEmergente.attributes("-topmost", True)
        VentanaEmergente.wait_visibility() # Pa que se espere
        VentanaEmergente.grab_set() 
        
        
        self.ParrafoNuevoProduto = ctk.CTkLabel(VentanaEmergente,
            text="Cuentanos Sobre tu producto",
            font=Estilos.Subtitulos,
            text_color= Estilos.ColorSubtitulo, 
            justify= "center",
            height= 50,
            width= 150,
            )
        self.ParrafoNuevoProduto.pack(pady=(0, 30))
    
        self.NombreProducto = ctk.CTkEntry(VentanaEmergente,
            placeholder_text="Nombre de su nuevo producto",
            font= Estilos.Texto,
            width= 400,
            height= 50,
            )
        self.NombreProducto.pack(padx=50, pady=10)
        
        self.ParrafoPregunta1Produto = ctk.CTkLabel(VentanaEmergente,
            text="¿Qué tipo de producto es?",
            font=Estilos.Parrafo,
            text_color= Estilos.ColorSubtitulo, 
            justify= "center",
            height= 50,
            width= 50,
            )
        self.ParrafoPregunta1Produto.pack(pady=(0, 0))
        
        CatalogoProductos = ["Alimentos", "Electronicos", "Limpieza"]
        
        self.TipoProducto = ctk.CTkOptionMenu(VentanaEmergente,
            values= CatalogoProductos,
            )
        self.TipoProducto.pack(padx=50, pady=10)
        
        self.CantidadProducto = ctk.CTkEntry(VentanaEmergente,
            placeholder_text="Cantidad",
            font= Estilos.Texto,
            width= 400,
            height= 50,
            )
        self.CantidadProducto.pack(padx=50, pady=10)
        
        self.PrecioProducto = ctk.CTkEntry(VentanaEmergente,
            placeholder_text="Precio $",
            font= Estilos.Texto,
            width= 400,
            height= 50,
            )
        self.PrecioProducto.pack(padx=50, pady=10)
        
        self.ParrafoPregunta1Produto = ctk.CTkLabel(VentanaEmergente,
            text="¿En que estado se encuentra?",
            font=Estilos.Parrafo,
            text_color= Estilos.ColorSubtitulo, 
            justify= "center",
            height= 50,
            width= 50,
            )
        self.ParrafoPregunta1Produto.pack(pady=(0, 0))
        
        EstadoProductos = ["Nuevo", "Seminuevo", "Fresco", "Caduco", "Radioactivo", "Dudoso"]
        
        self.CaducidadProducto = ctk.CTkOptionMenu(VentanaEmergente,
            values= EstadoProductos,
            )
        self.CaducidadProducto.pack(padx=50, pady=10)

        Boton = ctk.CTkButton(
            VentanaEmergente,
            text="Subir producto",
            font=Estilos.Botones,
            fg_color=Estilos.ColorBoton,
            text_color=Estilos.ColorTextoBoton,
            width=100,
            command=self.RegistrarPoductos
        )
        Boton.pack(pady=20)

#-------------------- Modificacion de Productos --------------------
    def VentanaModificarProductos(self):
        
        VentanaEmergente = ctk.CTkToplevel() 
        VentanaEmergente.title ("Agregar productos")
        VentanaEmergente.geometry("800x800")
        VentanaEmergente.attributes("-topmost", True)
        VentanaEmergente.wait_visibility() # Pa que se espere
        VentanaEmergente.grab_set() 
        
        
        self.ParrafoModificarProduto = ctk.CTkLabel(VentanaEmergente,
            text="Modificar Producto",
            font=Estilos.Subtitulos,
            text_color= Estilos.ColorSubtitulo, 
            justify= "center",
            height= 50,
            width= 150,
            )
        self.ParrafoModificarProduto.pack(pady=(0, 30))
    
        self.ParrafoEspecificarProduto = ctk.CTkLabel(VentanaEmergente,
            text="Porfavor especifica el producto que quiera editar",
            font=Estilos.Parrafo,
            text_color= Estilos.ColorSubtitulo, 
            justify= "center",
            height= 50,
            width= 50,
            )
        self.ParrafoEspecificarProduto.pack(pady=(0, 0))
    
        self.NumeroProdcto = ctk.CTkEntry(VentanaEmergente,
            placeholder_text="Numero de barras",
            font= Estilos.Texto,
            width= 400,
            height= 50,
            )
        self.NumeroProdcto.pack(padx=50, pady=10)
        
        self.ParrafoStockProduto = ctk.CTkLabel(VentanaEmergente,
            text="¿Modifique su stock?",
            font=Estilos.Parrafo,
            text_color= Estilos.ColorSubtitulo, 
            justify= "center",
            height= 50,
            width= 50,
            )
        self.ParrafoStockProduto.pack(pady=(0, 0))
        
        self.PrecioProducto = ctk.CTkEntry(VentanaEmergente,
            placeholder_text="Nuevo numero de Stock",
            font= Estilos.Texto,
            width= 400,
            height= 50,
            )
        self.PrecioProducto.pack(padx=50, pady=10)
        
        self.ParrafoPregunta1Produto = ctk.CTkLabel(VentanaEmergente,
            text="¿Desea eliminar?",
            font=Estilos.Parrafo,
            text_color= Estilos.ColorSubtitulo, 
            justify= "center",
            height= 50,
            width= 50,
            )
        self.ParrafoPregunta1Produto.pack(pady=(0, 0))
        
        # --- Boton Variable ---
        ctk.CTkLabel(VentanaEmergente, text="¿Qué quieres hacer?").pack(pady=10)
        
        # Variable exclusiva para esta ventana
        self.RadioELIMINAR = ctk.StringVar(value="Eliminar") 
        ctk.CTkRadioButton(VentanaEmergente, text="Actualizar Stock", variable=self.RadioELIMINAR, value="Conservar").pack(pady=5)
        ctk.CTkRadioButton(VentanaEmergente, text="ELIMINAR PRODUCTO", variable=self.RadioELIMINAR, value="Eliminar", fg_color="red").pack(pady=5)        
        
        Boton = ctk.CTkButton(VentanaEmergente,
            text="Cambiar producto",
            font=Estilos.Botones,
            fg_color=Estilos.ColorBotonEspecial,
            text_color=Estilos.ColorTextoBoton,
            width=100,
            command=self.ModificarProductos
        )
        Boton.pack(pady=20)   
    
        
#---------------------------------------- Conexion con la base de datos ----------------------------------------
#-------------------- inicio de secion y registro --------------------

#┌( ͝° ͜ʖ͡°)=> Primero debemos se conectarnos con el archivo "DataBase.py"
# para poder utilizarla de manera mas comoda
    def ConectarBD(self):
        DataBase.Conectar()
        
    def Registrar(self): 
#┌( ͝° ͜ʖ͡°)=> Para poder obtener los datos que el usuario dio debemos
# de gurdarlo en una variable seguido de un ".get()"
        Nombre = self.RegistrarNombre.get()
        Usuario = self.RegistrarUsuario.get()
        Contraseña = self.RegistrarContraseña.get()
        Rol = self.RegistrarRoles.get()
        
#┌( ͝° ͜ʖ͡°)=> Mandamos lo archivos al archivo BaseDatos.py 
# sin embargo, las bases de datos son bien lloronas, por lo que
# debemos de mandar exactamente los mismos datos a comparar para que empiece a llorar

        Exito = DataBase.Registrar(Nombre, Usuario, Contraseña, Rol)
        
#┌( ͝° ͜ʖ͡°)=> a partir de ello podemos hacer con ellas lo que querramos
# y se viene lo chido :), como ventanas emergentes o como ya vimos
# cambios completos en la interfaz

        if Exito:
            self.VolverLogin()
            if Rol == "Comprador":
                VentanaEmergente.Ventana(self, "¡Bárbaro!", "Inicia sesión para que te puedan fiar", ERROR=False)
            else:
                VentanaEmergente.Ventana(self, "¡Bárbaro!", "Inicia sesión para que puedas fiar JAJ", ERROR=False)
        else:
            VentanaEmergente.Ventana(self, "Ops...", "Error: Ese usuario ya existe.", ERROR=True)
        
    def IniciarSesion(self):
        Usuario = self.ObtenerUsuario.get()
        Contraseña = self.ObtenerContraseña.get()
        
        Resultado = DataBase.Iniciar(Usuario, Contraseña)
        
        if Resultado:
            self.IdUsuario = Resultado[0]
            Rol = Resultado[4]
            if Resultado[4] == "Comprador":
                self.IrCompradores()
            elif Resultado[4] == "Vendedor":
                self.IrVendedores()
        else:
            VentanaEmergente.Ventana(self, "Ops...", "No somos nosotros, eres tu \n Usuario o contraseña incorrectos, checalos bebuki", ERROR=True)


#-------------------- Compradores --------------------
    def VerProductos(self):
        for widget in self.Catalogos.winfo_children(): # Limpiar lista para acercarnos a un "recargar pagina"
            widget.destroy() #se destrutye para volver a aparecer

        Productos = DataBase.VerTodosLosProductos()
        
        if Productos:
            for Producto in Productos:

                IdProducto, Nombre, Tipo, Cantidad, Estado, Precio = Producto

                FrameProducto = ctk.CTkFrame(self.Catalogos,
                    fg_color= Estilos.Fondo)
                FrameProducto.pack(fill="x", padx=10, pady=5)
                
                if Estado == "Seminuevo":
                    AntiguoPrecio = Precio
                    Precio = Precio * 10 / 100
                    Oferta = f"Antiguo precio: ${AntiguoPrecio} Ahora: ${Precio}, 10 porciento de descueto!"
                elif Estado == "Caduco":
                    AntiguoPrecio = Precio
                    Precio = Precio * 50 / 100
                    Oferta = f"Antiguo precio: ${AntiguoPrecio} Ahora: ${Precio} 50 porciento de descueto!!"
                elif Estado == "Radioactivo":
                    AntiguoPrecio = Precio
                    Precio = Precio * 90 / 100
                    Oferta = f"Antiguo precio: ${AntiguoPrecio} Ahora: ${Precio} 90 porciento de descueto!!"
                elif Estado == "Dudoso":
                    AntiguoPrecio = Precio
                    Precio = Precio * 80 / 100
                    Oferta = f"Antiguo precio: ${AntiguoPrecio} Ahora: ${Precio} 80 porciento de descueto!!"
                else:
                    Oferta = f"Precio: ${Precio}"
                
                
                try:
                    Info = f"Categoria= {Tipo} \n Nombre: {Nombre} | Stock: {Cantidad} | Estado: {Estado} \n {Oferta}"
                    Label = ctk.CTkLabel(FrameProducto, text=Info, text_color="white", anchor="w")
                    Label.pack(side="left", padx=10, pady=10)
                    
                    BotonComprar = ctk.CTkButton(FrameProducto,
                        text="Comprar",
                        font=Estilos.Botones,
                        fg_color=Estilos.ColorBoton,
                        text_color=Estilos.ColorTextoBoton,
                        width=20,
                        command= lambda: self.Compras(IdProducto)
                        )
                    BotonComprar.pack(side="right", pady=40)
                    
                    BotonFiado = ctk.CTkButton(FrameProducto,
                        text="Fiar",
                        font=Estilos.Botones,
                        fg_color=Estilos.ColorBoton,
                        text_color=Estilos.ColorTextoBoton,
                        width=20,
                        command= lambda: self.Fiadote(IdProducto)
                        )
                    BotonFiado.pack(side="right", pady=40)
                    

                except:
                    Info = f"Que verguenza, pero no tenemos productos :("
                    Label = ctk.CTkLabel(FrameProducto, text=Info, text_color="white", anchor="w")
                    Label.pack(side="left", padx=10, pady=10)
                    
        else:
            Label = ctk.CTkLabel(self.Catalogos, text="No tienes productos aún", text_color="gray")
            Label.pack(pady=20)
            
# --- Acciones de compras ---
    def Compras(self, IdProducto):
        try:
            DataBase.Compra(IdProducto)
            self.VerProductos() #Actualizamos los datos
            VentanaEmergente.Ventana(self, "Viejo comprador", "Eso mamona, acabas de comprar un producto", ERROR=False)
                        
        except:
            VentanaEmergente.Ventana(self, "Ah cabron!", "Algo salio mal,no se que paso, pero no vuelvas a hacer eso", ERROR=True)
            
    def Fiadote(self, IdProducto):
        try:
            DataBase.Compra(IdProducto)
            self.VerProductos() #Actualizamos los datos
            VentanaEmergente.Ventana(self, "Fiado!", "Mijo, Algo bien, \n Algo gratis (por ahora) \n Te cobraremos en 1 semana :D", ERROR=False)
                        
        except:
            VentanaEmergente.Ventana(self, "Ah cabron!", "Algo salio mal,no se que paso, pero no vuelvas a hacer eso", ERROR=True)      
        
            
#-------------------- Vendedores --------------------
    def RegistrarPoductos(self):    
        try:    
            Nombre = self.NombreProducto.get()
            Tipo = self.TipoProducto.get()
            Estado = self.CaducidadProducto.get()
            
            if not Nombre or Tipo == "Selecciona Categoría":
                VentanaEmergente.Ventana(self, "¡Oye!", "Ponle nombre y categoría, no seas cabron", ERROR=True)
                return
            
            Cantidad = int(self.CantidadProducto.get())
            Precio = float(self.PrecioProducto.get())
            IdUsuario = self.IdUsuario
            
            FechaSQL = None
            
            if Tipo == "Alimentos":
                dias = -1 if Estado == "Caduco" else 30 # se caduco ayer JAJ
                FechaCalculada = datetime.now() + timedelta(days=dias)
                FechaSQL = FechaCalculada.strftime('%Y-%m-%d')

            Exito = DataBase.AgregarProducto(Nombre, Tipo, Cantidad, Precio, IdUsuario, FechaSQL, Estado)
            
            if Exito:
                VentanaEmergente.Ventana(self, "¡Éxito!", f"Se añadió {Nombre} al mercado.", ERROR=False)
                
                self.MisProductos() #Recarga la pagina

            else:
                VentanaEmergente.Ventana(self, "Error", "La base de datos rechazó el producto.", ERROR=True)

        except ValueError:
            VentanaEmergente.Ventana(self, "Matemáticas hijo...", "Cantidad y Precio deben ser números.", ERROR=True)
        
    def MisProductos(self):
        for widget in self.Catalogo.winfo_children(): # Limpiar lista
            widget.destroy()

        Productos = DataBase.VerMisProductos(self.IdUsuario)
    
        if Productos:
            for Producto in Productos:

                IdProducto, Nombre, Tipo, Cantidad, Precio, IdUsuario = Producto

                FrameProducto = ctk.CTkFrame(self.Catalogo,
                    fg_color= Estilos.Fondo)
                FrameProducto.pack(fill="x", padx=10, pady=5)
                
                Info = f"Codigo de barras: {IdProducto} \n  Nombre: {Nombre} | Tipo de Producto: ({Tipo}) | stock: {Cantidad} | Precio: ${Precio} |"
                Label = ctk.CTkLabel(FrameProducto, text=Info, text_color="white", anchor="w")
                Label.pack(side="left", padx=10, pady=10)
        else:
            Label = ctk.CTkLabel(self.Catalogo, text="No tienes productos aún", text_color="gray")
            Label.pack(pady=20)

    def ModificarProductos(self):
        try: 
            CodigoBarras= int(self.NumeroProdcto.get())
            Stock = int(self.PrecioProducto.get())
            Eliminar = self.RadioELIMINAR.get()
            
            if not CodigoBarras or Stock == "Selecciona Algo":
                VentanaEmergente.Ventana(self, "hmmmm", "Algo me dice que te falta algo", ERROR=True)
                return
            
            if Eliminar == "Eliminar":
                Exito = DataBase.EliminarProducto(CodigoBarras)
                VentanaEmergente.Ventana(self, "Eliminaste el artucilo", "Eliminaste el artucilo", ERROR=False)
                
            elif Eliminar != "Eliminar":
                Exito = DataBase.ModificarStock(CodigoBarras, Stock)
                self.MisProductos() #Recarga la pagina
                
            else:
                VentanaEmergente.Ventana(self, "Error", "La base de datos rechazó el producto.", ERROR=True)
        except ValueError:
            VentanaEmergente.Ventana(self, "Matemáticas hijo...", "Codigo de barras y Stock deben ser números.", ERROR=True)
                    
    def GenerarReporteInteligente(self):
        # Llamamos al módulo satélite
        exito = ReportePOO.GenerarReporteTxt()
        
        if exito:
            VentanaEmergente.Ventana(self, "Reporte Listo", 
                "Se generó 'reporte_inventario.txt' usando Polimorfismo y Herencia.", ERROR=False)
        else:
            VentanaEmergente.Ventana(self, "Error", "No se pudo generar el reporte.", ERROR=True)

if __name__ == "__main__":
    app = OnlyFiado()
    app.mainloop()
