import paho.mqtt.client as mqtt
from .callbacks import on_connect, on_subscribe, on_message

class MqttClientConnection:
    def __init__(self, broker_ip: str, port: int, client_name: str, keepalive=60):
        self.__broker_ip = broker_ip
        self.__port = port
        self.__client_name = client_name
        self.__keepalive = keepalive
    
    def start_connection(self):
        mqtt_client = mqtt.Client(self.__client_name)

        #callbacks
        mqtt_client.on_connect = on_connect
        mqtt_client.on_subscribe = on_subscribe
        mqtt_client.on_message = on_message

        mqtt_client.connect(host=self.__broker_ip, port=self.__port, keepalive=self.__keepalive) #passa os dados de conexão 
        self._mqtt_client= mqtt_client #salva o cliente mqtt na variavel mqtt_client
        mqtt_client.loop_start() #inicia o loop par verificar o status do mqtt
    
    def end_connection(self):
        try:
            self._mqtt_client.loop_stop() #para o loop do mqtt
            self._mqtt_client.disconnect() #desconecta do broker
            print("Desconectado do broker com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao desconectar do broker: {e}")