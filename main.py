import cv2
from datetime import datetime
from check_for_camears import List_Ports
from capturing import capturing_frame

dt = datetime.now()
current_time = dt.strftime("%Y_%m_%d_%H_%M_%S")
print(current_time)

working_ports = List_Ports()[1]
print(working_ports)
for i in working_ports:
    capturing_frame(i, current_time)

