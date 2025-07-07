#Python y Django 

## Curso Python Flex

Comision: 78110

Profesor: Alan Exequiel Prestia

Linkedin:

## Alumno 

Nombre: Alejandro Martin Elordi

Linkedin: https://www.linkedin.com/in/alejandro-elordi-5323b444/

Github: https://github.com/AleElordi/TuPrimeraPagina-Elordi.git

 orden en el que se prueban las cosas y/o donde están las funcionalidades:

 1) Pantalla de inicio con template index heredando el nav y footer del llamado "padre", esto se repetira en el resto de templates.
 2) El proyecto contiene una seccion de productos donde se pueden ver todos los productos y repuestos ingresados a la BBDD
    a) Esta seccion tambien contiene al buscador por marca que relaciona este atributo tanto en articulos como en repuestos y los muestra en pantalla pisando el contenido original
    b) Esta seccion es dinamica y se nutre de los formularios especificados en el punto 3
3) En la seccion de articulos se encuentran 2 formularios que permiten grabar en la BBDD los datos necesarios para crear nuevos productos y repuestos
    a) En ambos formularios hay controles de datos, confirmacion de exito y mensaje de error
4) LA ultima seccion funcional es la de suscriptores que permite grabar en BBDD el mail, nombre y fecha de registro para "recibir novedades"
5) Por ultimo en el template "datos" deje la consigna del proyecto para que sea mas facil de controlar cada punto