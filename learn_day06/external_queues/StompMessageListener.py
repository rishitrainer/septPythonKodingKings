import stomp
import time

host =  "localhost"
port = 61613
dest_queue = "test_queue"

class KKListener:



    def on_error(self, message):
        print('received an error %s' % message)

    def on_message(self, message):
        print(message)
        print(message.headers)
        print(message.body)



conn = stomp.Connection(host_and_ports = [(host, port)])
conn.set_listener("KKListener", KKListener())
conn.connect()
conn.subscribe(destination=dest_queue, id=1, ack='auto')
print("Done")
print("Waiting for messages...")
while True:
    time.sleep(10)
