from datetime import datetime
from check_for_cameras import list_ports
from capturing import capturing_frame
import threading


class CamThread(threading.Thread):
    def __init__(self, port, datetime_str):
        threading.Thread.__init__(self)
        self.datetime_str = datetime_str
        self.port = port

    def run(self):
        print("Starting " + str(self.port))
        capturing_frame(self.port, self.datetime_str)


dt = datetime.now()
current_time = dt.strftime("%Y_%m_%d_%H_%M_%S")
print(current_time)

working_ports = list_ports()[1]
print(working_ports)
# for i in working_ports:
#     capturing_frame(i, current_time)
thread0 = CamThread(0, current_time)
thread1 = CamThread(1, current_time)
# thread2 = CamThread(2, current_time)
# thread3 = CamThread(3, current_time)
# thread4 = CamThread(4, current_time)
# thread5 = CamThread(5, current_time)


thread0.start()
thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()
# thread5.start()

