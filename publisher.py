import paho.mqtt.client as mqtt

mqtt_client = mqtt.Client("meu_publisher")
mqtt_client.connect(host="localhost", port=1883 ) # Conecta ao broker MQTT
mqtt_client.puiblish(topic="/messages", payload='{"minha": "mensagem"}') # Publica uma mensagem no tópico "/messages"