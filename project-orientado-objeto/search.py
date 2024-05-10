import tkinter as tk

def tecla_precionada( event ):
  text = f'Tecla { repr( event.char ) } presionada.'
  label[ 'text' ] = text
  
def tecla_liberada( event ):
  text = f'Tecla { repr( event.char ) } liberada.'
  label[ 'text'] = text

root = tk.Tk()
root.title( string='Janela Principal')

# tamanho da janela
width = round( number=root.winfo_screenwidth() / 2 )
height = round( number=root.winfo_screenheight() / 2 )

# tamanho da janela
root.geometry( newGeometry=f'{width}x{height}') 
root.minsize( width=width, height=height)

# chamando as funcões
root.bind( sequence="key", func=tecla_precionada)
root.bind( sequence="keyRelease", func=tecla_precionada)

# frame
frame = tk.Frame( master=root  )
frame.pack( expand=True, fill=tk.BOTH, padx=50, pady=50 )

label = tk.Label( master=root, text="Precione qualquer tecla")
label.pack( expand=True, fill=tk.BOTH )

root.mainloop()