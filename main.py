import tkinter as tk
from automatapy import isValidSql

class App(tk.Frame):
    def __init__(self, master):
        #widgets
        super().__init__(master)
        self.lblUrl = tk.Label(text="Ingrese consulta SQL:")
        self.txtUrl = tk.Text(height=7,width=40)
        self.btnComprobar = tk.Button(text="Comprobar")
        self.lblResultado = tk.Label(text="")
        self.lblUrl.pack(side='top',padx=20,pady=20)
        self.txtUrl.pack(padx=20,fill='x')
        self.btnComprobar.pack(padx=20,pady=20)
        self.lblResultado.pack()
        self.config(padx=400,pady=400)
        self.pack()

        #eventos
        self.btnComprobar.bind('<Button-1>',self.btnComprobarClic)
    
    #funciones
    def btnComprobarClic(self,event):
        cadena = self.txtUrl.get("1.0","end-1c").upper()
        isValid = isValidSql(cadena+" ")
        self.lblResultado.config(text= 'La consulta SQL es válida' if isValid else 'La consulta SQL es inválida',
                                 fg= 'green' if isValid else 'red')
                            
root = tk.Tk()
root.title('AUTOMATA-SELECT-SQL')
myapp = App(root)
myapp.mainloop()

