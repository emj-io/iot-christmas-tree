import paho.mqtt.client as mqtt

def __on_connect(client, userdata, flags, rc):
    print("CONNECT")

def __on_message(client, userdata, msg):
    print("MESSAGE")
    print(str(msg.payload))

def new_client():
    client = mqtt.Client()
    client.on_connect = __on_connect
    client.on_message = __on_message

    client.connect("localhost", 1883, 60)
    client.subscribe("awsiot_to_localgateway")
    return client
