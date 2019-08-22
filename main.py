__version__ = "1.0"
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.app import App
from kivymd.theming import ThemeManager
import uuid

import paho.mqtt.client as mqtt
import config_mqtt
import threading
from threading import Thread
import ast
import Queue


bump = 0
somthing_detected = False
empiric_time_diff = 1500
msg_eval = {}
go_process = False

q = Queue.Queue() #initialises a first in first out queue

def process_data(mqtt_message_rx):
    global bump, somthing_detected,empiric_time_diff

    while True:
        if not q.empty(): #check if the queue is empty
            mqtt_message_rx2 = q.get()  #get the first message which was received and delete
            print('########################queue message: ###############################', mqtt_message_rx2)
            if somthing_detected == True:
                if 'AI_RULE' in mqtt_message_rx2.values() or 'SMART_RULE' in mqtt_message_rx2.values():
                    current_time_stamp = mqtt_message_rx2.get('triggeredTimestamp')
                    if mqtt_message_rx2.get('type') != preview_event_type:
                        if abs(current_time_stamp - preview_time_stamp) < empiric_time_diff:
                            bump = bump + 1
                            print('BUMP = ', bump)

                else: 
                    print('An event different than AI_RULE or SMART_RULE was detected')
                    somthing_detected = False
            else:
                if 'AI_RULE' in mqtt_message_rx2.values() or 'SMART_RULE' in mqtt_message_rx2.values():
                    preview_time_stamp = mqtt_message_rx2.get('triggeredTimestamp')
                    preview_event_type = mqtt_message_rx2.get('type')
                    somthing_detected = True

                else:
                    somthing_detected = False

        
class PybrApp(App, threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    theme_cls = ThemeManager()
    
    def on_start(self):
        def on_connect(client, userdata, flags, rc):
            print('Connected with result code {code}'.format(code=rc))


        def on_message(client, userdata, msg):
            global msg_eval
            global go_process
            global q
            mqtt_message_rx = 'Msg received from topic={topic}\n{content}'.format(topic=msg.topic, content=str(msg.payload))
            print('Msg received from topic={topic}\n{content}'.format(topic=msg.topic, content=str(msg.payload)))
            q.put(("{'" + str(message.payload) + "', " + str(message.topic) + "}"))
            # save_data(mqtt_message_rx)
            # process_data(mqtt_message_rx)
            # m_decode=msg.payload.decode("utf-8","ignore")
            msg_eval = ast.literal_eval(content)
            go_process = True
            # thread.start_new_thread( process_data, (ast.literal_eval(msg.payload), ) )
            # process_data(msg_eval)

        # def connect():
        #     client = mqtt.Client(client_id=str(uuid.uuid4()), transport='websockets')
        #     client.on_connect = on_connect
        #     client.on_message = on_message

        #     client.tls_set(ca_certs = config_mqtt.ca_cert_path)
        #     client.username_pw_set(config_mqtt.mqtt_user_name, config_mqtt.mqtt_password)

        #     client.connect('ns01-wss.brainium.com', 443)
        #     # client.loop_start() #start loop to process received messages
        #     client.subscribe(config_mqtt.alerts_topic)
        #     # client.subscribe(config_mqtt.acc_norm_datasource_topic)

        #     client.loop_forever()
        
        client = mqtt.Client(client_id=str(uuid.uuid4()), transport='websockets')
        client.on_connect = on_connect
        client.on_message = on_message

        # client.tls_set(ca_certs = config_mqtt.ca_cert_path) # works for Python3
        client.tls_set('/home/ivan/kivyBrasilApp/pybrapp/cacert.crt') # For python2.7
        # client.tls_set('/kivy/pybrapp/cacert.crt') # For python2.7
        client.username_pw_set(config_mqtt.mqtt_user_name, config_mqtt.mqtt_password)

        client.connect('ns01-wss.brainium.com', 443)
        # client.loop_start() #start loop to process received messages
        client.subscribe(config_mqtt.alerts_topic)
        # client.subscribe(config_mqtt.acc_norm_datasource_topic)

        # client.loop_forever()
        client.loop_start()

if __name__ == "__main__":

    # worker = Thread(target=downloadEnclosures, args=(i, enclosure_queue,))
    # worker.setDaemon(True)
    # worker.start()
    process_data = Thread(target=process_data, args=(msg_eval,))
    # process_data = thread.start_new_thread( process_data, (msg_eval, ) )
    process_data.setDaemon(True)
    process_data.start()
    # PybrApp().run()
    threadapp = PybrApp().run()
    threadapp.start()