import tkinter as tk
from automatapy import isValidSql

MENSAJE_LABEL ='-La sentencia FROM es obligatoria\n'
MENSAJE_LABEL+='-No se contemplan SUBCONSULTAS, NI RELACIONES AVANZADAS (JOIN)\n'
MENSAJE_LABEL+='-NO se contemplan operaciones con PARÉNTESIS'

class App(tk.Frame):
    def __init__(self, master):
        #widgets
        super().__init__(master)
        self.lblInstruccion = tk.Label(text="Ingrese su consulta SQL:",
                                       font=('Consolas',12,'bold'))
        self.lblMensaje = tk.Label(text=MENSAJE_LABEL,justify='left',
                                   font=('Consolas',8,''),
                                   fg='gray')
        self.txtConsultaSQL = tk.Text(height=7,width=40,
                                      font=('Consolas',12,''))
        self.btnComprobar = tk.Button(text="VERIFICAR",
                                      font=('Consolas',16,'bold'))
        self.lblResultado = tk.Label(text="(resultado...)",
                                     font=('Consolas',12,'bold'))
        
        self.lblInstruccion.pack(pady=5)
        self.lblMensaje.pack(pady=5)
        self.txtConsultaSQL.pack(padx=20,fill='both')
        self.btnComprobar.pack(padx=10,pady=10,fill='x')
        self.lblResultado.pack()
        self.pack()

        #eventos
        self.btnComprobar.bind('<Button-1>',self.btnComprobarClic)
    
    #funciones
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

