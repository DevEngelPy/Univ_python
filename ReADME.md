**parametros de windgets PACK:

*ejemplo:

- nombre:object = ttk.Label(aplicacion, text='Luis', font=('Helvetica',30),bootstyle='primary').pack(side=ttk.TOP,fill=ttk.BOTH, expand=True, ipadx=80, ipady=80)
- apellido:object = ttk.Label(aplicacion, text='Moreno', font=('Helvetica',30), bootstyle='inverse-danger').pack(side=ttk.TOP,fill=ttk.BOTH, expand=False)

- SIDE:Lado en que se posicionara el windget (top, left, bootom, righ).

- FILL: rellenar El relleno determina si un widget ocupará el espacio disponible. Acepta los siguientes valores: 'x', 'y', 'ambos' y 'ninguno'. De forma predeterminada, 
        el relleno es 'none'.
        llenar	    Efecto
        'Ninguno'	El widget no se expandirá para llenar ningún espacio adicional. Solo ocupa el espacio que se ajusta al contenido.
        'x'	        El widget se expandirá horizontalmente para llenar cualquier espacio adicional a lo largo del eje x.
        'y'	        El widget se expandirá verticalmente para llenar cualquier espacio adicional a lo largo del eje Y.
        'Ambas'	    El widget se expandirá tanto horizontal como verticalmente para llenar cualquier espacio adicional en ambas direcciones.

- EXPAND:La expansión determina si el widget debe expandirse para ocupar los espacios adicionales asignados al contenedor.
        Si la expansión se establece en Verdadero, el widget se expandirá, y si se establece en Falso, no lo hará. El valor predeterminado del parámetro expand es False.
        El parámetro expand depende en gran medida del parámetro side.
        La siguiente tabla ilustra las dependencias entre los parámetros side y expand cuando se trata del espacio del widget.
            
- ipdy y ipdx: son rellenado internos.
- padx y pady: son rellenado externo

-ANCHOR: El parámetro le permite anclar el widget al borde del espacio asignado. Acepta uno de los siguientes valores:anchor.
        Pegajoso	Descripción
            'n'  	Norte o Centro Superior
            's' 	Sur o centro inferior
            'e' 	Este o Centro Derecha
            'w' 	Oeste o Centro Izquierdo
            'NO'	Noroeste o arriba a la izquierda
            'ne'	Noreste o arriba a la derecha
            'se'	Sureste o abajo a la derecha
            'SW'	Suroeste o abajo a la izquierda
        'Centro'	Centro
