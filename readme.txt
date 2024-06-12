La base de datos de herramientas sera lo siguiente 

admin
user = "admin"
contraseña = "admin"

empleados
cedula = int
nombre = string
cargo = string
telefono = int


herramientas
id_h = int(autoincrementable)
codigo = string("H001") // recuerda que tiene que tener el codigo de esta forma o que no se repita ese codigo para otros no se debe repetir
nombre_h = string("Martillo") // No se puede repetir el nombre tiene que ser distinto o con una variante
stock = int //Cantidad que se debe colocar siempre va hacer uno no olvidar eso 
comentario = string ("tiene que colocar alguna caracteristica que tenga la herramienta ")
imagen = string ("tiene que tener el enlace para la imagen") // tiene que no ser obligatorio la imagen 


prestamo
id_p = int(autoincrementable)
empleado_p = string(nombre)
cedula_p = int(cedula)
codigo_p = string(codigo)
nombreh_p =  string(nombre_h)
stock_p = (stock)
fecha_p = string ("tiene que colocarse la hora tambien")
fecha_pf = string("tiene que colocarse la hora en la que entrega")//tiene que estar en blanco antes de enviarse a reporte
estado = string //"Prestado o Devuelto"
comentario = string // colocar cualquier cosa que hizo el empleado para llevar un control de el o dejarlo vacio 


reporte
empleado_p = string(nombre)
cedula_p = int(cedula)
codigo_p = string(codigo)
nombreh_p  =  string(nombre_h)
stock_p = (stock)
fecha_p = string ("tiene que colocarse la hora tambien")
fecha_pf= string("tiene que colocarse la hora en la que entrega")
estado = string //"Prestado o Devuelto"
comentario = string // colocar cualquie cosa que hizo el empleado para llevar un control de el