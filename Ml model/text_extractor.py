from PIL import Image
import pytesseract
from audio import say
import cv2

def read_text(path):
    try:
        text = pytesseract.image_to_string(Image.open(path))
        # print(pytesseract.image_to_data(Image.open(path)))
        if len(text)==0:
            say("No text found")
        else:
            say(text)
    except:
        say("No text found")
    
# read_text('./Img for text extraction/Text-msg.webp')

def read_realtime():
    cam = cv2.VideoCapture(0)
    res, image = cam.read()
    path = "Img for text extraction/detect.jpg"
    cv2.imwrite(path,image)
    cam.release()
    cv2.destroyAllWindows()
    read_text(path)

# read_realtime()