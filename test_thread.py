import threading   
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty

import paho.mqtt.client as mqtt
import config_mqtt
import ast
import Queue
import uuid
import re
import time

q = Queue.Queue(maxsize=20)
empiric_time_diff = 3000


def Print_delay(q):
    while True:
        while not q.empty():
            print("queue not empty")
            time.sleep(2)

def process_data(q):
    global bump, somthing_detected,empiric_time_diff
    current_time_stamp = 0
    preview_time_stamp = 0
    preview_event_type = ""
    second_q_element = False
    bump = 0

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
                            print('BUMP DETECTED = ', bump)
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

class Thread(BoxLayout):
    counter = NumericProperty(0)
    
    def Counter_function(self):
        self.counter += 1
        self.ids.lbl.text = "{}".format(self.counter)
        while not q.empty():
            print q.get()

    def First_thread(self):
        threading.Thread(target = self.Counter_function).start()
        self.counter += 1
        self.ids.lbl.text = "{}".format(self.counter)

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
    #     mqtt_msg_transformed = ast.literal_eval(mqtt_msg2)
    #     # mqtt_message_rx2 = q.get()  #get the first message which was received and delete
    #     # msg_eval = ast.literal_eval(msg.payload)
    #     # jota = msg.payload
    #     # print('jota.values()  ', jota.values())
    #     # if 'AI_RULE' in mqtt_msg_transformed.values() or 'SMART_RULE' in mqtt_msg_transformed.values():
    #     #     print ("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\n\n\n",mqtt_msg_transformed.values())
    #     # print('queue message:', mqtt_msg_transformed)
    # # if somthing_detected == True:
    #     if 'AI_RULE' in mqtt_msg_transformed.values() or 'SMART_RULE' in mqtt_msg_transformed.values():
    #         print ("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\n\n\n",mqtt_msg_transformed.values())
    #         print(mqtt_msg_transformed.get('type') )
    #         current_time_stamp = mqtt_msg_transformed.get('triggeredTimestamp')
    #         if mqtt_msg_transformed.get('type') != preview_event_type:
    #             print("Boushetttttttttttttttttttttttttttttttttttt")
    #         #     if abs(current_time_stamp - preview_time_stamp) < empiric_time_diff:
    #         #         bump = bump + 1
    #         #         print('BUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUMP = ', bump)

    #     else: 
    #         print('An event different than AI_RULE or SMART_RULE was detected')
    #         somthing_detected = False
    # # else:
    #     if 'AI_RULE' in mqtt_msg_transformed.values() or 'SMART_RULE' in mqtt_msg_transformed.values():
    #         preview_time_stamp = mqtt_msg_transformed.get('triggeredTimestamp')
    #         print ("                         preview_time_stamp                         ", preview_time_stamp )
    #         preview_event_type = mqtt_msg_transformed.get('type')
    #         somthing_detected = True

    #     else:
    #         somthing_detected = False
    #     mqtt_message_rx = 'Msg received from topic={topic}\n{content}'.format(topic=msg.topic, content=str(msg.payload))
    #     print('Msg received from topic={topic}\n{content}'.format(topic=msg.topic, content=str(msg.payload)))
    #     q.put(("{'" + str(message.payload) + "', " + str(message.topic) + "}"))
   
    #     msg_eval = ast.literal_eval(content)
    #     go_process = True
        
    
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

class MyApp(App):
    def build(self):
        self.load_kv('thread.kv')
        return Thread() 

if __name__ == "__main__":
    app = MyApp()
    # threading.Thread(target = Print_delay, args=(q,)).start()
    threading.Thread(target = process_data, args=(q,)).start()
    app.run()