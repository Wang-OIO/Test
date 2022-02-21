
import json

from kafka import KafkaProducer

def sendData():
    producer = KafkaProducer(
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        bootstrap_servers=['cbp3.chinaoly.com:19092','cbp4.chinaoly.com:19092','cbp6.chinaoly.com:19092','cbp7.chinaoly.com:19092','cbp8.chinaoly.com:19092']
        #bootstrap_servers=['192.168.51.41:9092','192.168.51.42:9092','192.168.51.43:9092']
    )

    data = {'sjyCode':'tldp',
            "gjKey":"330110199907201376",
            "gjPicture":"",
            "cityCodeStart":"330104",
            "cityCodeEnd":"330104",
            "addressStart":"杭州东站",
            "addressEnd":"杭州东站",
            "activeTimeStart":"2021-06-23 17:25:00",
            "activeTimeEnd":"2021-06-23 17:25:00",
            "longitudeStart":"120.18081665",
            "longitudeEnd":"120.18081665",
            "latitudeStart":"30.24523973",
            "latitudeEnd":"30.24523973",
            "name":"王振壮",
            "sex":"男",
            "nation":"汉",
            "native":"浙江杭州市"
            }
    print(data)
    # msg = json.dumps(data).encode()
    key = '330110199907201376'
    resp = producer.send('ssbk2_input_person',key=key.encode("utf-8"),value=data)
    producer.close()
    print(resp)
if __name__ == '__main__':
    sendData()
