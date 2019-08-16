from pathlib import Path

# data_folder = Path("source_data/text_files/")

# file_to_open = data_folder / "raw_data.txt"
# pathlib.Path.cwd()
a = Path.cwd()
print ('a is: ',a)
ca_cert_path = Path.cwd() / 'cacert.crt'
print ('ca_cert_path is: ',ca_cert_path)
# ca_cert_path = Path(pathlib.Path.cwd()"source_data/text_files/cacert.crt")
# ca_cert_path = 'cacert.crt'
mqtt_user_name = 'oauth2-user'
mqtt_password = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJuczAxIiwic3ViIjoiMjQzNyIsInVzZXJfbmFtZSI6ImlwZmFyaGVyQGdtYWlsLmNvbSIsInNjb3BlIjpbInJlYWQtb25seSJdLCJleHAiOjE2MjA1NjM4NTksImF1dGhvcml0aWVzIjpbIlJPTEVfVVNFUiJdLCJqdGkiOiIyNTkzYmY1Yi1jOThmLTQ3YjgtOTE5Ni0xYjM4YTFhZjRhYjYiLCJjbGllbnRfaWQiOiJyZWFkLW9ubHkifQ.WbUeS0Xvcf3iiIzUIixgqeavi7Q3lDcgmIDv5IdxiSM'  # copy and paste here external client id from your account
user_id = '2437'  # copy and paste here your user id
# gateway_id = '7115-2639-0738-7925'  # copy and paste here your device id
device_id = 'TO136-0202100001000A8C'  # copy and paste here your device id


# alerts
#     /v1/users/{user_id}/in/ALERTS
alerts_topic                        = '/v1/users/{user_id}/in/alerts'.format(user_id=user_id)
#     /v1/users/{user_id}/in/devices/{device_id}/datasources/ALERTS

#     Datasource 	                Units of measure
#     ACCELERATION_NORM       	    meter per second squared
#     WORLD_ACCELERATION_NORM 	    meter per second squared
#     GYROSCOPE_NORM 	            degrees per second
#     MAGNETIC_FIELD_NORM 	        microtesla
#     PRESSURE 	                    pascal
#     HUMIDITY 	                    percent
#     HUMIDITY_TEMPERATURE 	        celsius
#     PROXIMITY 	                centimeter
#     IR_SPECTRUM_LIGHTNESS 	    lux
#     VISIBLE_SPECTRUM_LIGHTNESS 	lux
#     SOUND_LEVEL 	                decibel

acc_norm_datasource_topic           = '/v1/users/{user_id}/in/devices/{device_id}/datasources/ACCELERATION_NORM'.format(user_id=user_id, device_id=device_id)
world_acc_norm_datasource_topic     = '/v1/users/{user_id}/in/devices/{device_id}/datasources/WORLD_ACCELERATION_NORM'.format(user_id=user_id, device_id=device_id)
gyro_norm_datasource_topic          = '/v1/users/{user_id}/in/devices/{device_id}/datasources/GYROSCOPE_NORM'.format(user_id=user_id, device_id=device_id)
magfield_norm_datasource_topic      = '/v1/users/{user_id}/in/devices/{device_id}/datasources/MAGNETIC_FIELD_NORM'.format(user_id=user_id, device_id=device_id)
presure_datasource_topic            = '/v1/users/{user_id}/in/devices/{device_id}/datasources/PRESSURE'.format(user_id=user_id, device_id=device_id)
humidity_datasource_topic           = '/v1/users/{user_id}/in/devices/{device_id}/datasources/HUMIDITY'.format(user_id=user_id, device_id=device_id)
hum_temp_datasource_topic           = '/v1/users/{user_id}/in/devices/{device_id}/datasources/HUMIDITY_TEMPERATURE'.format(user_id=user_id, device_id=device_id)
prox_datasource_topic               = '/v1/users/{user_id}/in/devices/{device_id}/datasources/PROXIMITY'.format(user_id=user_id, device_id=device_id)
ir_light_datasource_topic           = '/v1/users/{user_id}/in/devices/{device_id}/datasources/IR_SPECTRUM_LIGHTNESS'.format(user_id=user_id, device_id=device_id)
visible_light_datasource_topic      = '/v1/users/{user_id}/in/devices/{device_id}/datasources/VISIBLE_SPECTRUM_LIGHTNESS'.format(user_id=user_id, device_id=device_id)
sound_datasource_topic              = '/v1/users/{user_id}/in/devices/{device_id}/datasources/SOUND_LEVEL'.format(user_id=user_id, device_id=device_id)


# motions    
#     /v1/users/{user_id}/in/devices/{device_id}/datasources/MOTION
motions_datasource_topic              = '/v1/users/{user_id}/in/devices/{device_id}/datasources/MOTION'.format(user_id=user_id, device_id=device_id)

# telemetry data

#     acceleration
#         /v1/users/{user_id}/in/devices/{device_id}/datasources/ACCELERATION_NORM  
#     world acceleration
#         /v1/users/{user_id}/in/devices/{device_id}/datasources/WORLD_ACCELERATION_NORM
#     gyroscope
#         /v1/users/{user_id}/in/devices/{device_id}/datasources/GYROSCOPE_NORM
#     rotation
#         /v1/users/{user_id}/in/devices/{device_id}/datasources/ROTATION
rotation_datasource_topic              = '/v1/users/{user_id}/in/devices/{device_id}/datasources/ROTATION'.format(user_id=user_id, device_id=device_id)
#     temperature
#         /v1/users/{user_id}/in/devices/{device_id}/datasources/HUMIDITY_TEMPERATURE
#     pressure
#         /v1/users/{user_id}/in/devices/{device_id}/datasources/PRESSURE
#     humidity
#         /v1/users/{user_id}/in/devices/{device_id}/datasources/HUMIDITY
#     proximity
#         /v1/users/{user_id}/in/devices/{device_id}/datasources/PROXIMITY
#     lightness (visible spectrum)
#         /v1/users/{user_id}/in/devices/{device_id}/datasources/VISIBLE_SPECTRUM_LIGHTNESS
#     lightness (IR spectrum)
#         /v1/users/{user_id}/in/devices/{device_id}/datasources/IR_SPECTRUM_LIGHTNESS
#     magnetic field
#         /v1/users/{user_id}/in/devices/{device_id}/datasources/MAGNETIC_FIELD_NORM
#     sound level
#         /v1/users/{user_id}/in/devices/{device_id}/datasources/SOUND_LEVEL


# predictive maintenance

#     pattern
#         /v1/users/{user_id}/in/devices/{device_id}/datasources/PDM_PATTERN
pdm_pattern_datasource_topic              = '/v1/users/{user_id}/in/devices/{device_id}/datasources/PDM_PATTERN'.format(user_id=user_id, device_id=device_id)
#     event
#         /v1/users/{user_id}/in/devices/{device_id}/datasources/PDM_EVENT
pdm_event_datasource_topic              = '/v1/users/{user_id}/in/devices/{device_id}/datasources/PDM_EVENT'.format(user_id=user_id, device_id=device_id)