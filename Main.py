import tkinter
from tkinter import *
from tkinter import ttk
from tokenize import String
from BBDDhelper import insertar_militante, consultar_edad, consultar_id

##
#  Programa principal++
##

# Preparación de ventana y frame

raiz = Tk()
raiz.title("Gestión de militantes")
raiz.resizable(False, False)
# raiz.iconbitmap("logo.ico")
raiz.geometry("520x360")
raiz.config(bg="white")

nombre = StringVar()
edad = StringVar()
IDs = StringVar()

miFrame = Frame()
miFrame.pack()
miFrame.config(width=500, height=340, bg="grey")

labelFrame = Label(raiz, text="Gestión de militantes")
labelFrame.pack()

# Declaración de funciones

def meterMilitante():
    insertar_militante(entryNombre.get(), entryEdad.get(), comboPago.get())
    entryNombre.delete(0, END)
    entryEdad.delete(0, END)


def buscarMilitante():
    resultado.delete("1.0", "end")  # Se borran los datos de la búsqueda anterior

    texto = consultar_edad(int(comboEdad.get()))
    texto2: String = ""

    for militante in texto:
        texto2 = texto2 + str((militante[1] + ", con ID: " + str(militante[0]) + "\n"))

    resultado.insert(tkinter.INSERT, texto2)

def busquedaPorID():
    resultado.delete("1.0", "end")  # Se borran los datos de la búsqueda anterior
    resultado.insert(tkinter.INSERT, consultar_id(int(entryID.get())))


# Parte de inclusión de nuevos militantes

labelSeccion1 = Label(miFrame, text="Inscripción de militantes", background="grey", fg="white", font="12")
labelSeccion1.place(x=45, y=30)
labelSeccion2 = Label(miFrame, text="Consulta de militantes", background="grey", fg="white", font="12")
labelSeccion2.place(x=300, y=30)

labelNombre = Label(miFrame, text="Nombre", background="grey", fg="white")
labelNombre.place(x=20, y=70)
entryNombre = Entry(miFrame, textvariable=nombre)
entryNombre.place(x=80, y=70)
labelEdad = Label(miFrame, text="Edad", background="grey", fg="white")
labelEdad.place(x=20, y=100)
entryEdad = Entry(miFrame, width=10, textvariable=edad)
entryEdad.place(x=80, y=100)
labelPago = Label(miFrame, text="Pago", background="grey", fg="white")
labelPago.place(x=20, y=130)
comboPago = ttk.Combobox(miFrame, state="readonly", values=("SÍ", "NO"))
comboPago.place(x=80, y=130, width=50)

botonAgregar = Button(raiz, text="Inscribir", command=meterMilitante)
botonAgregar.place(x="130", y="170")

# Parte de consulta de militantes

labelBuscarEdad = Label(miFrame, text="Edad", background="grey", fg="white")
labelBuscarEdad.place(x=290, y=70)
comboEdad = ttk.Combobox(miFrame, state="readonly", values=list(range(12, 112)))
comboEdad.place(x=330, y=70, width=50)

labelBuscarID = Label(miFrame, text="ID", background="grey", fg="white")
labelBuscarID.place(x=290, y=100)
entryID = Entry(miFrame, textvariable=IDs)
entryID.place(x=330, y=100, width=50)

botonConsultar = Button(raiz, text="Consultar por ID", command=busquedaPorID)
botonConsultar.place(x="290", y="140")

botonConsultar = Button(raiz, text="Consultar por edad", command=buscarMilitante)
botonConsultar.place(x="390", y="140")

resultado = Text(miFrame, background="white", fg="black", state="normal")
resultado.place(x=290, y=180, width=170, height=140)
scrollResultado = Scrollbar(miFrame, command=resultado.yview)
scrollResultado.place(x=470, y=180, height=140)
resultado.config(yscrollcommand=scrollResultado.set)  # Ajusta el scroll al Text

raiz.mainloop()
