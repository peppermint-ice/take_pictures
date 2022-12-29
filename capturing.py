import cv2


def capturing_frame(port, datetime_str):
    cap = cv2.VideoCapture(port)  # video capture source camera (Here webcam of laptop)
    ret, frame = cap.read()   # return a single frame in variable `frame`
    while True:
        cv2.imshow('img1', frame)  # display the captured image
        if cv2.waitKey(1) & 0xFF == ord('y'):  # save on pressing 'y'
            cv2.imwrite(''.join(['images/', datetime_str, '_c', str(port) + '.png']), frame)
            cv2.destroyAllWindows()
            break
        # cv2.imwrite(''.join(['images/', datetime_str, '_c', str(port) + '.png']), frame)
        cv2.destroyAllWindows()
        break

    cap.release()





