import tkinter as tk
from automatapy import isValidSql
import re

MENSAJE_LABEL ='-La sentencia FROM es obligatoria\n'
MENSAJE_LABEL+='-No se contemplan SUBCONSULTAS\n'
MENSAJE_LABEL+='-No se contemplan RELACIONES AVANZADAS (JOIN)\n'
MENSAJE_LABEL+='-No se contemplan operaciones con PARÉNTESIS\n'
MENSAJE_LABEL+="-Los string se escriben con comillas simples (')\n"
MENSAJE_LABEL+="-No se permiten nombres de columna"

MENSAJE_EMPTY="INGRESE SU CONSULTA SQL"
MENSAJE_VALIDO="LA CONSULTA SQL ES VÁLIDA"
MENSAJE_INVALIDO="LA CONSULTA SQL NO ES VÁLIDA"

TITULO  = "VERIFICADOR DE \n"
TITULO +="CONSULTAS SQL"

FONT = "Impact Regular"
INPUT_FONT="Roman Regular"
FONT_TITULO = "Bell MT"

ICONOS1 = "Webdings"

class App(tk.Frame):
    def __init__(self, master):
        #widgets
        super().__init__(master)
        self.ContainerBtn = tk.Frame(self,relief='raised')
        self.lblInstruccion = tk.Label(text=TITULO,relief='flat',
                                       font=(FONT_TITULO,24,'bold '))
        self.lblMensaje = tk.Label(text=MENSAJE_LABEL,justify='left',
                                   font=(FONT,8,''),
                                   fg='gray')
        self.lblVerificar = tk.Label(self.ContainerBtn,
                                     text='COMPROBAR',justify='center',
                                   font=(FONT,8,'bold'),
                                   fg='gray')
        self.lblBorrar = tk.Label(self.ContainerBtn,
                                  text='BORRAR',justify='center',
                                   font=(FONT,8,'bold'),
                                   fg='gray')
        self.txtConsultaSQL = tk.Text(height=7,width=50,
                                      font=(INPUT_FONT,10,''),
                                      fg='black')
        self.btnComprobar = tk.Button(self.ContainerBtn,text="8",
                                      font=(ICONOS1,20,''),
                                      width=5,
                                      fg='white',
                                      background='#0BE462')
        self.btnBorrar = tk.Button(self.ContainerBtn,text="r",
                                      font=(ICONOS1,20,''),
                                      width=5,
                                      fg='white',
                                      background='#FF7373')
        self.lblResultado = tk.Label(text=MENSAJE_EMPTY,
                                     font=(FONT,12,'bold'),
                                     fg='gray')
        
        self.lblInstruccion.pack(pady=5)
        self.lblMensaje.pack(pady=5,fill='x')
        self.txtConsultaSQL.pack(padx=20,fill='both')
        self.ContainerBtn.pack(pady=10,fill='x')
        self.lblVerificar.grid(row=0,column=0)
        self.lblBorrar.grid(row=0,column=1)
        self.btnComprobar.grid(row=1, column=0, padx=20, sticky='e')
        self.btnBorrar.grid(row=1, column=1, padx=20, sticky='w')
        self.lblResultado.pack(pady=5)
        self.pack()

        #eventos
        self.btnComprobar.bind('<Button-1>',self.btnComprobarClic)
        self.btnBorrar.bind('<Button-1>',self.btnBorrarClic)
    
    #funciones
    def btnBorrarClic(self,event):
        self.txtConsultaSQL.delete("1.0","end")
        self.lblResultado.config(text=MENSAJE_EMPTY,
                                     font=(FONT,12,'bold'),
                                     fg='gray')

    def btnComprobarClic(self,event):
        cadena = self.txtConsultaSQL.get("1.0","end-1c").upper()
        isValid = isValidSql(cadena+" ")
        isEmpty = re.fullmatch('\s*',cadena+" ")
        
        if isValid:
            self.lblResultado.config(text=MENSAJE_VALIDO,
                                     fg='green')
        elif isEmpty:
            self.lblResultado.config(text=MENSAJE_EMPTY,
                                     fg='gray')
        else:
            self.lblResultado.config(text=MENSAJE_INVALIDO,
                                     fg='red')

                            
root = tk.Tk()
root.title('AUTOMATA-SELECT-SQL')
root.resizable(False,False)
myapp = App(root)
myapp.mainloop()

