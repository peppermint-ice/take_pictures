from datetime import datetime
from check_for_cameras import list_ports
from capturing import capturing_frame


dt = datetime.now()
current_time = dt.strftime("%Y_%m_%d_%H_%M_%S")
print(current_time)

working_ports = list_ports()[1]
print(working_ports)
for i in working_ports:
    capturing_frame(i, current_time)

