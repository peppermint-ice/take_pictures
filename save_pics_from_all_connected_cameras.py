import cv2
from datetime import datetime


def set_time():
    # determines current date & time. needed to give files proper names
    dt = datetime.now()
    time_str = dt.strftime("%Y_%m_%d_%H_%M_%S")
    print(time_str)
    return time_str


def list_ports():
    # Tests the ports and returns a tuple with the available ports and the ones that are working.
    non_working_ports = []
    dev_port = 0
    working_ports = []
    available_ports = []
    while len(non_working_ports) < 6: # if there are more than 5 non working ports stop the testing.
        camera = cv2.VideoCapture(dev_port)
        if not camera.isOpened():
            non_working_ports.append(dev_port)
            print("Port %s is not working." % dev_port)
        else:
            is_reading, img = camera.read()
            w = camera.get(3)
            h = camera.get(4)
            if is_reading:
                print("Port %s is working and reads images (%s x %s)" %(dev_port, h, w))
                working_ports.append(dev_port)
            else:
                print("Port %s for camera ( %s x %s) is present but does not reads." % (dev_port, h, w))
                available_ports.append(dev_port)
        dev_port += 1
    return available_ports, working_ports, non_working_ports


def capturing_frame(port, datetime_str):
    cap = cv2.VideoCapture(port)  # video capture from the set source camera
    ret, frame = cap.read()   # return a single frame in variable `frame`. "ret" is True if the operation was successful
    while True:
        cv2.imwrite(''.join(['images/', datetime_str, '_c', str(port) + '.png']), frame)  # saves the picture
        # cv2.destroyAllWindows()
        break
    cap.release()


# launches the function which returns current date & time
current_time = set_time()

# actually runs the script for every connected & working camera
current_ports = list_ports()[1]
for i in current_ports:
    capturing_frame(i, current_time)
