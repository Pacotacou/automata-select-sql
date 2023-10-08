import tkinter as tk
from automatapy import isValidSql

MENSAJE_LABEL ='-La sentencia FROM es obligatoria\n'
MENSAJE_LABEL+='-No se contemplan SUBCONSULTAS\n'
MENSAJE_LABEL+='-No se contemplan RELACIONES AVANZADAS (JOIN)\n'
MENSAJE_LABEL+='-No se contemplan operaciones con PARÉNTESIS'

FONT = "Verdana"
INPUT_FONT="Roman Regular"
ICONOS1 = "Webdings"
ICONOS2 = "Wingdings 2"

class App(tk.Frame):
    def __init__(self, master):
        #widgets
        super().__init__(master)
        self.lblInstruccion = tk.Label(text="Ingrese su consulta SQL:",
                                       font=(FONT,12,'bold'))
        self.lblMensaje = tk.Label(text=MENSAJE_LABEL,justify='left',
                                   font=(FONT,8,''),
                                   fg='gray')
        self.txtConsultaSQL = tk.Text(height=7,width=50,
                                      font=(INPUT_FONT,10,'bold'),
                                      fg='black')
        self.ContainerBtn = tk.Frame(self)
        self.btnComprobar = tk.Button(self.ContainerBtn,text="8",
                                      font=(ICONOS1,20,''),
                                      width=5,
                                      fg='green')
        self.btnBorrar = tk.Button(self.ContainerBtn,text="r",
                                      font=(ICONOS1,20,''),
                                      width=5,
                                      fg='red')
        self.lblResultado = tk.Label(text="(resultado...)",
                                     font=(FONT,12,'bold'),
                                     fg='gray')
        
        self.lblInstruccion.pack(pady=5)
        self.lblMensaje.pack(pady=5,fill='x')
        self.txtConsultaSQL.pack(padx=20,fill='both')
        self.ContainerBtn.pack(pady=10,fill='x')
        self.btnComprobar.grid(row=0, column=0, padx=20, pady=10, sticky='e')
        self.btnBorrar.grid(row=0, column=1, padx=20, pady=10, sticky='w')
        self.lblResultado.pack(pady=5)
        self.pack()

        #eventos
        self.btnComprobar.bind('<Button-1>',self.btnComprobarClic)
        self.btnBorrar.bind('<Button-1>',self.btnBorrarClic)
    
    #funciones
    def btnBorrarClic(self,event):
        self.txtConsultaSQL.delete("1.0","end")
        self.lblResultado.config(text="(resultado...)",
                                     font=(FONT,12,'bold'),
                                     fg='gray')

    def btnComprobarClic(self,event):
        cadena = self.txtConsultaSQL.get("1.0","end-1c").upper()
        isValid = isValidSql(cadena+" ")
        self.lblResultado.config(text= 'La consulta SQL es válida' if isValid else 'La consulta SQL es inválida',
                                 fg= 'green' if isValid else 'red')
                            
root = tk.Tk()
root.title('AUTOMATA-SELECT-SQL')
root.resizable(False,False)
myapp = App(root)
myapp.mainloop()

