import stomp

host =  "localhost"
port = 61613
dest_queue = "test_queue"

conn = stomp.Connection(host_and_ports = [(host, port)])
conn.connect()
for i in range(100):
    conn.send(destination=dest_queue, body="This is Test message " + str(i))

conn.disconnect()