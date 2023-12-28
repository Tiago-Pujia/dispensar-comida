# Dispensador de Comida Automático para Mascotas
## Tabla de Contenido

- [Dispensador de Comida Automático para Mascotas](#dispensador-de-comida-automático-para-mascotas)
  - [Tabla de Contenido](#tabla-de-contenido)
  - [Idea y Concepto](#idea-y-concepto)
  - [Especificación Técnica](#especificación-técnica)
  - [Ordenamiento de Archivo](#ordenamiento-de-archivo)
  - [Variables](#variables)
  - [Utilización de la API](#utilización-de-la-api)
    - [Método GET](#método-get)
    - [Método POST](#método-post)
    - [Método DELETE](#método-delete)
    - [Método PUT](#método-put)

---
## Idea y Concepto
Clonar Repositorio:
~~~
git clone https://github.com/Tiago-Pujia/Dispensador-Comida
~~~

El presente proyecto consiste en un alimentador de mascotas automático y manual, en donde una cantidad de comida X es dispensada todos los días en un horario establecido, y puede ser controlado desde un panel de control en forma de página web. Dicho horario puede ser creado, modificado o eliminado, y el alimento incluso puede ser dispensado de forma remota.

Una vez prendido el Web-Server, se puede acceder al panel de control entrando a la IP fija http://192.168.0.254/

![Interfaz Gráfica](/imgs/muestra.png)

---
## Especificación Técnica
**Componentes físicos necesarios:**
- Microcontrolador (que soporte Wi-Fi y Web-Server como ESP32)
- Servo 180°
- 1 botón
- Cables
  
**Softwares necesarios:**
- MicroPython (Microcontrolador)
- HTML (web)
- CSS (web)
- JSON (formato en red)
- JavaScript (web)
- Bootstrap (FrameWork CSS)

El microcontrolador creará una Web-Server HTTP, siendo allí donde el cliente realizará todas las peticiones pertinentes, y podrá entregar el panel de control en donde serán definidas todas las acciones tales como crear, modificar y eliminar horarios. Los horarios serán almacenados en un archivo en formato JSON denominado "horarios.json", y el microcontrolador se encargará de modificarlo.

El archivo JSON contendrá un array con una lista de objetos, que contarán con los siguientes atributos:
  - HORA (tiempo) (string);
  - PORCIONES (cantidad de 1 a 9) (number);
  - HABILITADO (1 habilitado y 0 deshabilitado) (number)

Todos los archivos estaran almacenados en la memoria ROM del microcontrolador excepto el framework Bootstrap que estara en la nube.

---
## Ordenamiento de Archivo
~~~
index.html 	  -> Panel de Control
index.py      -> Archivo principal del microcontrolador
horarios.json -> Lista de horarios
~~~
---
## Variables
Variables que deben ser modificadas en los siguientes archivos, según la adaptación del proyecto a un área:
> ### index.py
> 
> Wi-Fi
> ~~~
> 15 wifi_ssid = ""
> 16 wifi_password = ""
> ~~~

---
## Utilización de la API
El microcontrolador funcionará tal cual como una API:

### Método GET
> **/** 
> 
> Obtenemos el archivo principal "index.html"

> **/horarios** 
> 
> Obtenemos los horarios "horarios.json"
 
### Método POST
> **/**
> 
> Creamos un nuevo horario. Especificamos:
> - HORA
> - PORCIONES

> **/dispensar**
>
> Dispensamos alimento de manera remota. Especificamos:
> - PORCIONES

### Método DELETE
> /
>
> Eliminamos un horario. Especificamos:
> - HORA

### Método PUT
> /
>
> Modificamos un horario. Especificamos:
> - HORA
> - HORA_NUEVA (opcional)
> - PORCIONES_NUEVA (opcional)
> - HABILITAR_NUEVA (opcional)