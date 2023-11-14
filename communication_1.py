import network
from umqtt.simple import MQTTClient
import time

class ESP2_COM:
    def __init__(self):
        self.mqtt_broker = '192.168.186.205'
        self.mqtt_port = 1883
        self.pm_topic = b'pm25_topic'
        self.co_topic=b"carbon_monoxide"
        self.client = MQTTClient("ESP1", self.mqtt_broker,port=self.mqtt_port)
        self.client.connect()
        
    def send_pm25(self,value):
        self.client.publish(self.pm_topic,value)
        
    def send_co(self,value):
        self.client.publish(self.co_topic,value)
    def disconnect(self):
        self.client.disconnect()
        print('disconnected')
        
        