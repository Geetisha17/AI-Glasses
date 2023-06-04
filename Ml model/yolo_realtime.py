import cv2
import numpy as np
import time
from audio import say


# flag if true tells position of object
# num set the max number of objects
def detect(num=100):
    # Load Yolo
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    classes = []
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    start_time = position_time = time.time()

    items = []
    cnt = flag = 0
    obj = set()

    # Loading web cam
    camera = cv2.VideoCapture(0)
    # global frame
    
    while time.time() - start_time < 50:
        _, img = camera.read()
        # frame=img
        height, width, channels = img.shape

        # Detecting objects
        blob = cv2.dnn.blobFromImage(
            img, 0.00392, (320, 320), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)
        # print(outs)

        # Showing informations on the screen
        class_ids = []
        confidences = []
        boxes = []

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                # print(detection)
                if confidence > 0.6:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)

                    frame_center_x = img.shape[1] / 2
                    frame_center_y = img.shape[0] / 2

                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])

                    if time.time() - position_time > 7 and flag and cnt < num and classes[class_id] not in obj:
                        if center_x > frame_center_x:
                            direction_x = "to your right"
                        else:
                            direction_x = "to your left"

                        if center_y < frame_center_y:  # Flip the comparison for vertical direction
                            direction_y = "above you"  # Flip the direction description
                        else:
                            direction_y = "below you"  # Flip the direction description

                        words = f'{classes[class_id]} {direction_x} {direction_y}'
                        obj.add(classes[class_id])
                        print(words)
                        say(words)
                        cnt += 1
                        position_time = time.time()
                        # time.sleep(3)

                    confidences.append(float(confidence))
                    class_ids.append(class_id)
                    items.append(classes[class_id])

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

        font = cv2.FONT_HERSHEY_PLAIN
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                color = colors[i]
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.putText(img, label, (x, y + 30), font, 3, color, 3)
        cv2.imshow("Image", img)
        flag = 1
        key = cv2.waitKey(1)
        if key == 27:  # Press esc to break
            break

    final = list(set(items))  # to remove the repetative words.
    print(final)
    a = "person"  # Cuz index of person is 0
    if a in final:
        # name = face.face_recog(frame)
        # say("Say hello to "+name)
        say("Say hello to person")

    camera.release()
    cv2.destroyAllWindows()

# detect()