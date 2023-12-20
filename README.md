# Dispensador de Comida Automatico para Mascota
## Tabla de Contenido

- [Dispensador de Comida Automatico para Mascota](#dispensador-de-comida-automatico-para-mascota)
  - [Tabla de Contenido](#tabla-de-contenido)
  - [Idea y Concepto](#idea-y-concepto)
  - [Especificación Tecnica](#especificación-tecnica)
  - [Ordenamiento de Archivo](#ordenamiento-de-archivo)
  - [Variables](#variables)
  - [Utilización de la API](#utilización-de-la-api)

---
## Idea y Concepto
Clonar Repositorio:
~~~
git clone https://github.com/Tiago-Pujia/Dispensador-Comida
~~~

El proyecto trata sobre un alimentador de mascotas automatico y manual, donde dispensa X cantidad de comida todos los dias en una hora especifica. Este, puede controlarse desde un panel de control en forma de pagina web.

---
## Especificación Tecnica
**Componentes fisicos necesarios:**
- MicroControlador (que soporte WIFI como ESP32)
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
- JQuery (Libreria JS)

El microcontrolador creara una Web-Server HTTP donde el cliente hara todas las peticiones, este puede entregar el panel de control donde definimeros todas las acciones como crear, modificar o eliminar los horarios. Estos se guardaran en un archivo en formato JSON llamado "horarios.json", el microcontrolador se encargara de modificar este archivo.

El archivo JSON contrenda un array con una lista de objetos, estos tendran los atributos:
  - HORA (tiempo)
  - PORCIONES (cantidad de 1 a 9)
  - HABILITADO (1 habilitado)

Todos los archivos estaran almacenados en la memoria del microcontrolador

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
> 19 wifi_ssid = ""
> 20 wifi_password = ""
> ~~~

---
## Utilización de la API
El microcontrolador servira como una API como tal:

> ### Tipo GET
 
> ### Tipo POST

> ### Tipo PUT

> ### Tipo DELETE