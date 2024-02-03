from tkinter import *

ventana1=Tk()
ventana1.geometry("225x380")
ventana1.title("CALCUXX")
ventana1.resizable(False,False)

texto= " "
var_texto = StringVar()

def botones(num_o_sig):
    global texto
    texto= texto + str(num_o_sig)
    var_texto.set(texto)

def igual():
    global texto
    try:
        total=str(eval(texto))
        var_texto.set(total)
    except SyntaxError:
        var_texto.set("Error de calculo")

def borrar_total():
    global texto
    texto= " "
    var_texto.set(texto)

label=Label(ventana1,width=5,borderwidth=10,height=5,relief="sunken",bg="darkgrey",textvar=var_texto)
label.pack(fill="x")

ventana2=Frame(ventana1,width=5,borderwidth=5,relief="sunken",bg="grey")
ventana2.pack(fill="both",expand=True)

boton7=Button(ventana2,text=7,bg="black",fg="white",command= lambda: botones(7)).place(x=0,y=0,width=50,height=50)
boton8=Button(ventana2,text=8,bg="black",fg="white",command=lambda: botones(8)).place(x=55,y=0,width=50,height=50)
boton9=Button(ventana2,text=9,bg="black",fg="white",command=lambda: botones(9)).place(x=110,y=0,width=50,height=50)
boton4=Button(ventana2,text=4,bg="black",fg="white",command=lambda: botones(4)).place(x=0,y=55,width=50,height=50)
boton5=Button(ventana2,text=5,bg="black",fg="white",command=lambda: botones(5)).place(x=55,y=55,width=50,height=50)
boton6=Button(ventana2,text=6,bg="black",fg="white",command=lambda: botones(6)).place(x=110,y=55,width=50,height=50)
boton1=Button(ventana2,text=1,bg="black",fg="white",command=lambda: botones(1)).place(x=0,y=110,width=50,height=50)
boton2=Button(ventana2,text=2,bg="black",fg="white",command=lambda: botones(2)).place(x=55,y=110,width=50,height=50)
boton3=Button(ventana2,text=3,bg="black",fg="white",command=lambda: botones(3)).place(x=110,y=110,width=50,height=50)
boton0=Button(ventana2,text=0,bg="black",fg="white",command=lambda: botones(0)).place(x=0,y=165,width=105,height=50)

borrador=Button(ventana2,text="CE",bg="red",fg="white",command=lambda: borrar_total()).place(x=165,y=0,width=50,height=50)
suma=Button(ventana2,text="+",bg="black",fg="white",command= lambda: botones("+")).place(x=165,y=55,width=50,height=50)
resta=Button(ventana2,text="-",bg="black",fg="white",command= lambda: botones("-")).place(x=165,y=110,width=50,height=50)
multy=Button(ventana2,text="*",bg="black",fg="white",command= lambda: botones("*")).place(x=165,y=165,width=50,height=50)
divi=Button(ventana2,text="/",bg="black",fg="white",command= lambda: botones("/")).place(x=110,y=165,width=50,height=50)
decimal=Button(ventana2,text=".",bg="black",fg="white",command= lambda: botones(".")).place(x=165,y=220,width=50,height=50)
igual_a=Button(ventana2,text="=",bg="orange",fg="white",command=lambda: igual()).place(x=0,y=220,width=160,height=50)


mainloop()