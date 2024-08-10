import os
import ssl
import paho.mqtt.client as mqtt

username = os.getenv("MQTT_USERNAME")
password = os.getenv("MQTT_PASSWORD")
host = os.getenv("MQTT_HOST")
port = int(os.getenv("MQTT_PORT", 8883))

if not username:
    raise ValueError("MQTT_USERNAME not set")

if not password:
    raise ValueError("MQTT_PASSWORD not set")

if not host:
    raise ValueError("MQTT_HOST not set")

if not port:
    raise ValueError("MQTT_PORT not set")


def on_connect(client, userdata, flags, return_code, v5Config):
    if return_code == 0:
        print("connected")
        client.subscribe("hi")
        client.subscribe("hi2")
    else:
        print("could not connect, return code:", return_code)


def on_message(client, userdata, message):
    try:
        print("Received message: ", str(message.payload.decode("utf-8")))
    except:
        print("Error while decoding message")


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv311)
client.username_pw_set(username, password)
client.tls_set(cert_reqs=ssl.CERT_NONE)
client.on_connect = on_connect
client.on_message = on_message

client.connect(host, port)
client.loop_forever()
