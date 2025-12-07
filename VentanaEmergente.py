import customtkinter as ctk
import Estilos

def Ventana(PAPA, Titulo, Mensaje, ERROR=True):
    #--- ajusted de ventana ---
    VentanaEmergente = ctk.CTkToplevel(PAPA) # PAPA es para que sea una ventana hija jaja
    VentanaEmergente.title(Titulo)
    VentanaEmergente.geometry("600x250")
    VentanaEmergente.attributes("-topmost", True)
    VentanaEmergente.wait_visibility() # Pa que se espere
    
    #--- personalizacion ---
    #se le da un color u otro dependiendo si la ariable ERROR es o no true
    ColorTextoMensaje = Estilos.ColorBotonEspecial if ERROR else Estilos.ColorBoton 
    
    lbl = ctk.CTkLabel(VentanaEmergente, text=Mensaje, font=("Arial", 16, "bold"), text_color=ColorTextoMensaje, wraplength=450, justify="center")
    lbl.pack(pady=30, padx=20)
    
    Mensajito = "Chale" if ERROR else "Fuga"
    
    #--- boton ---
    Boton = ctk.CTkButton(
        VentanaEmergente,
        text=Mensajito,
        font=Estilos.Botones,
        fg_color=Estilos.ColorBoton,
        text_color=Estilos.ColorTextoBoton,
        width=100,
        command=VentanaEmergente.destroy
    )
    Boton.pack(pady=20)
    

