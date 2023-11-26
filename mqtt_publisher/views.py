from django.http import HttpResponse
from django.shortcuts import render
import paho.mqtt.client as mqtt


def publish_mqtt_message(topic, message):
    client = mqtt.Client()
    client.username_pw_set("btliot", "Bang1234")
    client.connect("8f7725991cd94c77a6a40c759d55192c.s2.eu.hivemq.cloud", 8883)  # Replace with your MQTT broker's address and port

    client.publish(topic, message)

    client.disconnect()


def publish_mqtt(request):
    topic = "my/topic"
    message = "Hello, MQTT!"

    publish_mqtt_message(topic, message)

    return HttpResponse("MQTT message published successfully!")
#hivemq.webclient.1700930780721
#IMi.bm6!O,$73RFna1Dh