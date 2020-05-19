import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected to Server: Code-" + str(rc))

    # Subscribing in on_connect - if we lose the connection
    # Reconnect then the subscription will be renewed.

    client.subscribe("CoreElectronics/test")
    client.subscribe("CoreElectronics/topic")

# When a server publishes a message this will be called.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

    # Here you can do if(msg.payload == "hello"):
        # do something


# Client Shit

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever()

