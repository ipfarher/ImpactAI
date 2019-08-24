__version__ = "1.0"
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/home/ivan/kivyBrasilApp/pybrapp/screens')
import threading  
from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemeManager
import uuid

import paho.mqtt.client as mqtt
import config_mqtt
import ast
import Queue
import re
import time
from startcount import update_bumps

q = Queue.Queue(maxsize=20)
empiric_time_diff = 3000
bump = 8

def get_bumps():
    global bump
    return bump


def process_data(q):
    global bump, somthing_detected,empiric_time_diff
    current_time_stamp = 0
    preview_time_stamp = 0
    preview_event_type = ""
    second_q_element = False


    while True:
        while not q.empty():
            mqtt_message_rx = q.get()  #get the first message which was received and delete
            mqtt_msg_dict = ast.literal_eval(mqtt_message_rx)
            
            if second_q_element == True:
                second_q_element = False
                
                if 'AI_RULE' in mqtt_msg_dict.values() or 'SMART_RULE' in mqtt_msg_dict.values():
                    current_time_stamp = mqtt_msg_dict.get('triggeredTimestamp')
                    print("current_time_stamp", current_time_stamp)
                    
                    if mqtt_msg_dict.get('type') != preview_event_type:
                        print('current_time_stamp - preview_time_stamp = ', current_time_stamp - preview_time_stamp)
                        if abs(current_time_stamp - preview_time_stamp) < empiric_time_diff:
                            bump = bump + 1
                            update_bumps(bump)
                            print('BUMP DETECTED = ', bump)
                            strbump = str(bump)
                else: 
                    print('An event different than AI_RULE or SMART_RULE was detected')
                    second_q_element = False
            
            else:
                if 'AI_RULE' in mqtt_msg_dict.values() or 'SMART_RULE' in mqtt_msg_dict.values():
                    preview_time_stamp = mqtt_msg_dict.get('triggeredTimestamp')
                    preview_event_type = mqtt_msg_dict.get('type')
                    second_q_element = True

                else:
                    second_q_element = False

        
# class PybrApp(App):
#     # theme_cls = ThemeManager()
#     Thread()
#     # def build(self):
#     #     # self.load_kv('thread.kv')
#     #     return Thread()


class PybrApp(App):
    theme_cls = ThemeManager()
    def on_connect(client, userdata, flags, rc):
            print('Connected with result code {code}'.format(code=rc))

    def on_message(client, userdata, msg):
        global msg_eval
        global go_process
        global bump, somthing_detected,empiric_time_diff
        preview_event_type = "SMART_RULE"

        # mqtt_msg = '{"id":"5d5dc7f70eeebf00015ae982","type":"AI_RULE","triggeredTimestamp":1566427122705,"datasource":null,"condition":null,"value":null,"datasourceUnits":null,"triggeredValue":null,"motionTypeName":"bump","motionTypeCode":0,"patternId":null,"patternName":null,"anomalyType":null,"ruleId":"72753ed1-c6e2-485a-803d-6c58f01d3231","projectId":747,"projectName":"Impacto","deviceId":"TO136-0202100001000A8C","deviceName":"AI Module","receivedAt":1566427127783}'
        mqtt_msg2 = re.sub(r"null", "\"null\"", msg.payload)
        # print(mqtt_msg2)
        q.put(mqtt_msg2)    
    
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
    threading.Thread(target = process_data, args=(q,)).start()
    PybrApp().run()
  