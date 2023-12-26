# Dispensador de Comida Automatico para Mascota
## Tabla de Contenido

- [Dispensador de Comida Automatico para Mascota](#dispensador-de-comida-automatico-para-mascota)
  - [Tabla de Contenido](#tabla-de-contenido)
  - [Idea y Concepto](#idea-y-concepto)
  - [Especificación Tecnica](#especificación-tecnica)
  - [Ordenamiento de Archivo](#ordenamiento-de-archivo)
  - [Variables](#variables)
  - [Utilización de la API](#utilización-de-la-api)
    - [Metodo GET](#metodo-get)
    - [Metodo POST](#metodo-post)
    - [Metodo DELETE](#metodo-delete)
    - [Metodo PUT](#metodo-put)

---
## Idea y Concepto
Clonar Repositorio:
~~~
git clone https://github.com/Tiago-Pujia/Dispensador-Comida
~~~

El proyecto trata sobre un alimentador de mascotas automatico y manual, donde dispensa X cantidad de comida todos los dias en una hora especifica. Este, puede controlarse desde un panel de control en forma de pagina web. Podemos crear, modificar y eliminar horarios e incluso dispensar alimento de forma remota.

![Interfaz Grafica](/imgs/muestra.jpg)

---
## Especificación Tecnica
**Componentes fisicos necesarios:**
- MicroControlador (que soporte WIFI y Web Server como ESP32)
- Servo 180°
- 1 Boton
- Cables
  
**Softwares necesarios:**
- MicroPython (MicroControlador)
- HTML (web)
- CSS (web)
- JSON (formato en red)
- JavaScript (web)
- Bootstrap (FrameWork CSS)

El microcontrolador creara una Web-Server HTTP donde el cliente hara todas las peticiones, este puede entregar el panel de control donde definimeros todas las acciones como crear, modificar o eliminar los horarios. Estos se guardaran en un archivo en formato JSON llamado "horarios.json", el microcontrolador se encargara de modificar este archivo.

El archivo JSON contrenda un array con una lista de objetos, estos tendran los atributos:
  - HORA (tiempo) (string)
  - PORCIONES (cantidad de 1 a 9) (number)
  - HABILITADO (1 habilitado y 0 deshabilitado) (number)

Todos los archivos estaran almacenados en la memoria ROM del microcontrolador excepto el framework Bootstrap que estara en la nube

---
## Ordenamiento de Archivo
~~~
index.html 	  -> Panel de Control.
index.py      -> Archivo principal del microcontrolador
horarios.json -> Lista de horarios
~~~
---
## Variables
Estas son variables que deben de cambiarse en los siguientes archivos, segun la adaptación del proyecto a un area:
> ### index.py
> 
> Wifi
> ~~~
> 15 wifi_ssid = ""
> 16 wifi_password = ""
> ~~~

---
## Utilización de la API
El microcontrolador servira como una API como tal:

### Metodo GET
> **/** 
> 
> Obtenemos el archivo principal "index.html"

> **/horarios** 
> 
> Obtenemos los horarios "horarios.json"
 
### Metodo POST
> **/**
> 
> Creamos un nuevo horario. Especificamos:
> - HORA
> - PORCIONES

> **/dispensar**
>
> Dispensamos alimento de manera remota. Especificamos:
> - PORCIONES

### Metodo DELETE
> /
>
> Eliminamos un horario. Especificamos:
> - HORA

### Metodo PUT
> /
>
> Modificamos un horario. Especificamos:
> - HORA
> - HORA_NUEVA (opcional)
> - PORCIONES_NUEVA (opcional)
> - HABILITAR_NUEVA (opcional)