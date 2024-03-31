import paho.mqtt.publish as publish

def publish_message(message):
    publish.single("lap/mensaje", message, hostname="192.168.1.100", port=1883)
    print("Mensaje enviado")
    return "Mensaje enviado"

    

def suscribe_message():
    import paho.mqtt.subscribe as subscribe
    msg = subscribe.simple("lap/mensaje", hostname="192.168.1.100", port=1883)
    
    print(str(msg.payload))
    cadena_texto = msg.payload.decode('utf-8').strip("'b")
    print(cadena_texto)
    return "Suscrito"

def loopSuscriber():
    import paho.mqtt.subscribe as subscribe
