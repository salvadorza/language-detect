from customtkinter import *
from langdetect import detect

app = CTk()

app.geometry("600x400")

set_appearance_mode("dark")

# Establecemos una serie de idiomas con un diccionario para despues convertir la clave en un valor que será el idioma
nombres_idiomas = {
    'af': 'Afrikáans',
    'sq': 'Albanés',
    'am': 'Amárico',
    'ar': 'Árabe',
    'hy': 'Armenio',
    'az': 'Azerí',
    'eu': 'Euskera',
    'bn': 'Bengalí',
    'bs': 'Bosnio',
    'bg': 'Búlgaro',
    'ca': 'Catalán',
    'hr': 'Croata',
    'cs': 'Checo',
    'da': 'Danés',
    'nl': 'Holandés',
    'en': 'Inglés',
    'et': 'Estonio',
    'fi': 'Finlandés',
    'fr': 'Francés',
    'gl': 'Gallego',
    'de': 'Alemán',
    'el': 'Griego',
    'he': 'Hebreo',
    'hi': 'Hindi',
    'hu': 'Húngaro',
    'is': 'Islandés',
    'id': 'Indonesio',
    'ga': 'Irlandés',
    'it': 'Italiano',
    'ja': 'Japonés',
    'ko': 'Coreano',
    'lv': 'Letón',
    'lt': 'Lituano',
    'mk': 'Macedonio',
    'ms': 'Malayo',
    'mt': 'Maltés',
    'no': 'Noruego',
    'fa': 'Persa',
    'pl': 'Polaco',
    'pt': 'Portugués',
    'ro': 'Rumano',
    'ru': 'Ruso',
    'sr': 'Serbio',
    'sk': 'Eslovaco',
    'sl': 'Esloveno',
    'es': 'Español',
    'sw': 'Suajili',
    'sv': 'Sueco',
    'tl': 'Tagalo',
    'th': 'Tailandés',
    'tr': 'Turco',
    'uk': 'Ucraniano',
    'ur': 'Urdu',
    'vi': 'Vietnamita',
    'cy': 'Galés',
    'xh': 'Xhosa',
    'yi': 'Yidis',
    'zu': 'Zulú',
}

# Funcion para poder seleccionar todo el texto con control-a
def seleccionar_todo(seleccion):
    entrada.select_range(0, len(entrada.get())) 
    return "break"




# Funcion para detectar el idioma que el usuario introduzca 
def detectar_idioma():
    texto = entrada.get() 
    label2.configure(text="")
    # Si el usuario no ha introducido ninguna palabra se lo decimos
    if not texto.strip():
        label2.configure(text="Por favor, ingresa un texto.", text_color="#1fa23e")
        return

    try:
        # Con detect podemos saber el idioma que ha introducido el usuario con langdetect
        codigo_idioma = detect(texto)
        if len(texto) < 5:  # Si el texto que introduce tiene menos de 5 letras le decimos que no es valido
         label2.configure(text="Por favor, escribe una oración más larga para detectar el idioma.", text_color="#1fa23e")
         return
        if codigo_idioma in nombres_idiomas:
            idioma_nombre = nombres_idiomas[codigo_idioma]
        else:
            texto.set("Idioma no reconocido")

        # Si hemos encontrado un idioma lo mostramos
        label2.configure(text=f"Idioma detectado: {idioma_nombre}")

    except Exception as e:
        # Manejamos las posibles excepciones que puedan surjir
        label2.configure(text=f"Idioma no detectado. Error: {str(e)}", text_color="red")
    
# Boton para generar el texto que nos diga que idioma ha introducido el usuario
boton = CTkButton(master=app,text="Detectar Idioma",corner_radius=2.5,fg_color="transparent",hover_color="#0c5299",border_color="#1fa23e",
                  border_width=2,command=detectar_idioma)
boton.place(relx=0.5,rely=0.3,anchor="center")

# Titulo del programa
label = CTkLabel(master=app,text="Introduce un texto",font=("Arial",20,"bold"),text_color="#1fa23e")
label.place(relx=0.5,rely=0.05,anchor="center")

# Lugar donde el usuario escribe el texto
entrada = CTkEntry(master=app, placeholder_text="Escribe aquí...",width=400,text_color="#fffec5")
entrada.place(relx=0.5,rely=0.15,anchor="center")

# Sitio donde va a aparecer el idioma que ha introducido el usuario o los posibles errores
label2 = CTkLabel(master=app,text="",font=("arial",18,"bold"),text_color="#1fa23e")
label2.place(relx=0.5,rely=0.5,anchor="center")

entrada.bind("<Control-a>", seleccionar_todo) # Selecciona todo el texto con control-a
app.mainloop()