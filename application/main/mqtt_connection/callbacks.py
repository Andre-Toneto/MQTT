from application.configs.broker_configs import mqtt_broker_configs

def on_connect(client, userdata, flags, rc): #rc são os erros que podem acontecer
    if rc == 0: #se rc for 0 significa que a conexão foi bem sucedida
        print(f"Conecteeeeeeiiii {client}")
        client.subscribe(mqtt_broker_configs["TOPIC"]) #se conectar, se inscreve no topico teste
    else:
        print("Erro na conexão: ", rc) #se não for 0 significa que houve erro na conexão

def on_subscribe(client, userdata, mid, granted_qos):
    print(f"Inscrito com sucesso no tópico: {mqtt_broker_configs["TOPIC"]}",) #quando se inscreve no topico, imprime a mensagem de sucesso
    print(f"mid: {mid}, granted_qos: {granted_qos}") #imprime o mid e o qos

def on_message(client, userdata, msg):
    print(f"Mensagem recebida no tópico {msg}") #quando receber uma mensagem, imprime o topico e a mensagem
    # Aqui você pode adicionar o código para processar a mensagem recebida
    # Por exemplo, você pode decodificar a mensagem e fazer algo com ela
    # message = msg.payload.decode()
    # print(f"Mensagem: {message}")
    print(client)
    print(msg.payload) #com o payload trazemos a mensagem como é enviada, e não em binário