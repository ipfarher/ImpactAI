import ast
import re

b = '{"muffin" : "lolz", "foo" : "kitty", "foo2" : null}'

d = re.sub(r"null", "\"null\"", b)
# d = b.replace("$null$", "\"null\"")
c = ast.literal_eval(d)


mqtt_msg = '{"id":"5d5dc7f70eeebf00015ae982","type":"AI_RULE","triggeredTimestamp":1566427122705,"datasource":null,"condition":null,"value":null,"datasourceUnits":null,"triggeredValue":null,"motionTypeName":"bump","motionTypeCode":0,"patternId":null,"patternName":null,"anomalyType":null,"ruleId":"72753ed1-c6e2-485a-803d-6c58f01d3231","projectId":747,"projectName":"Impacto","deviceId":"TO136-0202100001000A8C","deviceName":"AI Module","receivedAt":1566427127783}'
mqtt_msg2 = re.sub(r"null", "\"null\"", mqtt_msg)
print(mqtt_msg2)

mqtt_msg_transformed = ast.literal_eval(mqtt_msg2)
a=1