import paho.mqtt.publish as publish

publish.single("", "Hello", hostname="test.mosquitto.org")
publish.single("", "World!", hostname="test.mosquitto.org")
print("Done")
