import utime, network, gc, machine, socket, ujson
from machine import Pin, PWM, Timer

print("Ejecutando Programa")

# ===========================
# VARIABLES
# ===========================
# Pins
servo = PWM(Pin(13,Pin.OUT),freq=50)
led = Pin(27,Pin.OUT)
boton = Pin(12,Pin.IN,Pin.PULL_UP)

# Wifi
wifi_ssid = "Fibertel WiFi444 2.4GHz"
wifi_password = "00427182700"

# Web Server
tcp_socket = ''

# Variables Globales
horarios = []

# ===========================
# FUNCIONES WIFI y Web Server
# ===========================
def conectarse_wifi():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(wifi_ssid,wifi_password)
    
    while not sta_if.isconnected():
        utime.sleep(0.1)

    ip_actual, mascara, puerta_enlace, dns = sta_if.ifconfig()
    sta_if.ifconfig(('192.168.0.254', mascara, puerta_enlace, dns))
    print('Dirección IP:', sta_if.ifconfig()[0])
    prender_led()
    
def crear_web_server():
    global tcp_socket
    try:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.bind(('0.0.0.0', 80))
        tcp_socket.listen(5)
        prender_led()
    except OSError as e:
        print("Error al crear el servidor:", e)

def peticion_web_server():
    global horarios

    conn, addr = tcp_socket.accept()
    request = conn.recv(1024).decode('utf-8')

    if 'GET /horarios' in request:
        response = (
            'HTTP/1.1 200 OK\n'
            'Content-Type: application/json\n'
            'Connection: close\n\n'
            + ujson.dumps(horarios)
        )
    elif 'GET /' in request:
        with open('index.html', 'r') as archivo:
            pagina_web = archivo.read()

        response = (
            'HTTP/1.1 200 OK\n'
            'Content-Type: text/html\n'
            'Connection: close\n\n'
            + pagina_web
        )
    elif 'POST /dispensar' in request:
        try:
            contenido = request.find('\r\n\r\n') + 4
            contenido = request[contenido:]
            contenido = ujson.loads(contenido)
    
            dispensar_comida(contenido['PORCIONES'])
    
            response = (
                'HTTP/1.1 200 OK\n'
                'Content-Type: text/html\n'
                'Connection: close\n\n'
            )
        except OSError as e:
            response = (
                'HTTP/1.1 406 Not Acceptable\n'
                'Content-Type: text/html\n'
                'Connection: close\n\n'
            )
    elif 'POST /' in request:
        try:
            contenido = request.find('\r\n\r\n') + 4
            contenido = request[contenido:]
            contenido = ujson.loads(contenido)
            contenido['HABILITADO'] = 1
    
            horarios.append(contenido)
    
            with open('horarios.json', "w") as archivo:
                archivo.write(ujson.dumps(horarios))
    
            response = (
                'HTTP/1.1 200 OK\n'
                'Content-Type: text/html\n'
                'Connection: close\n\n'
            )
        except OSError as e:
            response = (
                'HTTP/1.1 406 Not Acceptable\n'
                'Content-Type: text/html\n'
                'Connection: close\n\n'
            )
    elif 'DELETE /' in request:
        try:
            contenido = request.find('\r\n\r\n') + 4
            contenido = request[contenido:]
            contenido = ujson.loads(contenido)

            for i, array in enumerate(horarios):
                if array.get('HORA') == contenido['HORA']:
                    del horarios[i]

            with open('horarios.json', "w") as archivo:
                archivo.write(ujson.dumps(horarios))

            response = (
                'HTTP/1.1 200 OK\n'
                'Content-Type: text/html\n'
                'Connection: close\n\n'
            )
        except OSError as e:
            response = (
                'HTTP/1.1 406 Not Acceptable\n'
                'Content-Type: text/html\n'
                'Connection: close\n\n'
            )
    elif 'PUT /' in request:
        try:
            contenido = request.find('\r\n\r\n') + 4
            contenido = request[contenido:]
            contenido = ujson.loads(contenido)

            indiceArray = -1

            for i, array in enumerate(horarios):
                if array.get('HORA') == contenido['HORA']:
                    indiceArray = i

            horarios[indiceArray]['HORA'] = contenido.get('HORA_NUEVA', horarios[indiceArray]['HORA'])
            horarios[indiceArray]['PORCIONES'] = contenido.get('PORCIONES_NUEVA', horarios[indiceArray]['PORCIONES'])
            horarios[indiceArray]['HABILITADO'] = contenido.get('HABILITADO_NUEVA', horarios[indiceArray]['HABILITADO'])

            with open('horarios.json', "w") as archivo:
                archivo.write(ujson.dumps(horarios))

            response = (
                'HTTP/1.1 200 OK\n'
                'Content-Type: text/html\n'
                'Connection: close\n\n'
            )        
        except OSError as e:
            response = (
                'HTTP/1.1 406 Not Acceptable\n'
                'Content-Type: text/html\n'
                'Connection: close\n\n'
            )
    else:
        response = 'HTTP/1.1 404 Not Found\nContent-Type: text/plain\nConnection: close\n\n404 Not Found'

    conn.sendall(response.encode('utf-8'))
    conn.close()

# ===========================
# FUNCIONES Para Dispensar
# ===========================

def prender_led():
    led.on()
    utime.sleep(0.5)
    led.off()
    utime.sleep(0.5)
 
def evento_boton(pin):
    dispensar_comida(1)

def controlar_horarios(timer):
    hora_actual = int(utime.localtime()[3])
    minuto_actual = int(utime.localtime()[4])

    for horario in horarios:
        hora_evento = int(horario['HORA'].split(':')[0])
        minuto_evento = int(horario['HORA'].split(':')[1])

        if hora_actual == hora_evento and minuto_actual == minuto_evento and horario['HABILITADO'] == 1:
            dispensar_comida(int(horario['PORCIONES']))
    
    gc.collect()

def dispensar_comida(porciones):
    prender_led()
    # X/1.8+25 Funcion lineal para transformar valor grados a un valor que comprenda el servo
    servo.duty(58) # 60°
    for i in range(0,porciones):
        utime.sleep(3)
    servo.duty(25) # 0°

# ===========================
# MAIN
# ===========================
servo.duty(25)
with open('horarios.json', 'r') as archivo:
    horarios = ujson.load(archivo)
conectarse_wifi()
crear_web_server()
Timer(1).init(mode=Timer.PERIODIC, period=60000, callback=controlar_horarios)
boton.irq(trigger=machine.Pin.IRQ_FALLING, handler=evento_boton)

while True:
    peticion_web_server()
    utime.sleep(0.01)    