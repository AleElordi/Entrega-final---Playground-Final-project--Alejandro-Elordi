#Python y Django 

Entrega Final

## Curso Python Flex

Comision: 78110

Profesor: Alan Exequiel Prestia

## Alumno 

Nombre: Alejandro Martin Elordi

Linkedin: https://www.linkedin.com/in/alejandro-elordi-5323b444/

Github: https://github.com/AleElordi/TuPrimeraPagina-Elordi.git

Video demo de la aplicación: 

 orden en el que se prueban las cosas y/o donde están las funcionalidades:

 1) Pantalla de inicio con template index heredando el nav y footer del llamado "padre", esto se repetira en el resto de templates, es una pantalla estatica diseñada en html con contenido fijo tipo "landing page" 
    a) Si el usuario no esta registrado y logueado solo vera 5 links: inicio, productos, datos y loguin
    b) Si el usuario no es admin podra agregar, ver y editar todos los articulos pero no los usuarios, se le habilitarán  los links "ver productos y repuestos" y "Agregar Articulos"
    c) Al usuario admin se le sumara el link "Administrar Usuarios" donde podra editarlos y eliminarlos
    d) Al loguerse los usuarios aparece el avatar que hayan subido 
    e) El boton login cambia por el de logout
    f) Se creo un template con un control aparte para el cambio de contraseñas 

 2) El proyecto contiene una seccion "Productos" donde se pueden ver todos los productos y repuestos ingresados a la BBDD
    a) Esta seccion tambien contiene al buscador por marca que relaciona este atributo tanto en productos como en repuestos y los muestra en pantalla pisando el contenido original
    b) Esta seccion es dinamica y se nutre del formulario "Agregar articulos" que se habilita solo si el usuario esta logueado
    c) A diferencia del proyecto anterior ahora esta todo unificado en la entidad "articulo" y se divide por su atributo "tipo" en: "productos" y "repuestos"
    d) En este caso la aplicacion arranca con un solo producto para demostrar en el video demo como se pueden ingresar cualquiera de los dos tipos de articulos y en tiempo real tanto este filtro como el buscador levantan de la BBDD los nuevos registros.
    f) Cada artículo cargado, sea producto o repuesto posee un boton para "ver mas" donde se individualiza el artículo en pantalla, una vez ingresado a el exite un boton "volver" para regresar al listado de articulos

3) En la sección "datos" se encuetran mis datos y la consigna de la pauta 

4) Las secciones "Ver productos y repuestos" y "Administrar usuarios" poseen un modelo CRUD donde dependiendo el tipo de usuario podra verlos de manera individual boton "ver", editarlos y eliminarlos con botones homónimos a esa acción.   

5) Si el usuario se encuentra logueado tambien tendra una seccion "Mis datos" para poder editar sus datos personles, aqui el cambio de contraseña tambien se redirige a un template aparte con un control del tipo de contraseña que se ingresa. 