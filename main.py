__version__ = "1.0"
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.app import App
from kivymd.theming import ThemeManager
import uuid

# import paho.mqtt.client as mqtt
# import config_mqtt


class PybrApp(App):
    theme_cls = ThemeManager()
    # def on_start(self):
    #     def on_connect(client, userdata, flags, rc):
    #         print('Connected with result code {code}'.format(code=rc))


    #     def on_message(client, userdata, msg):
    #         mqtt_message_rx = 'Msg received from topic={topic}\n{content}'.format(topic=msg.topic, content=str(msg.payload))
    #         print('Msg received from topic={topic}\n{content}'.format(topic=msg.topic, content=str(msg.payload)))

    #     # def connect():
    #     #     client = mqtt.Client(client_id=str(uuid.uuid4()), transport='websockets')
    #     #     client.on_connect = on_connect
    #     #     client.on_message = on_message

    #     #     client.tls_set(ca_certs = config_mqtt.ca_cert_path)
    #     #     client.username_pw_set(config_mqtt.mqtt_user_name, config_mqtt.mqtt_password)

    #     #     client.connect('ns01-wss.brainium.com', 443)
    #     #     # client.loop_start() #start loop to process received messages
    #     #     client.subscribe(config_mqtt.alerts_topic)
    #     #     # client.subscribe(config_mqtt.acc_norm_datasource_topic)

    #     #     client.loop_forever()
        
    #     client = mqtt.Client(client_id=str(uuid.uuid4()), transport='websockets')
    #     client.on_connect = on_connect
    #     client.on_message = on_message

    #     # client.tls_set(ca_certs = config_mqtt.ca_cert_path) # works for Python3
    #     client.tls_set('/home/ivan/kivyBrasilApp/pybrapp/cacert.crt') # For python2.7
    #     # client.tls_set('/kivy/pybrapp/cacert.crt') # For python2.7
    #     client.username_pw_set(config_mqtt.mqtt_user_name, config_mqtt.mqtt_password)

    #     client.connect('ns01-wss.brainium.com', 443)
    #     # client.loop_start() #start loop to process received messages
    #     client.subscribe(config_mqtt.alerts_topic)
    #     # client.subscribe(config_mqtt.acc_norm_datasource_topic)

    #     # client.loop_forever()
    #     client.loop_start()


if __name__ == "__main__":
    PybrApp().run()
