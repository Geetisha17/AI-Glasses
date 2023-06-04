from audio import listen, say
from NLP import predict
from text import msg
from yolo_realtime import detect
from face_detector import detect_face
from call import call
from text_extractor import read_text,read_realtime
from image_captioning import generate_caption, realtime_caption

say("Listening")
text = listen()
label = predict(text)


print(label)

try:
    if label==0:
        msg()
    if label==1:
        detect()
    elif label==2:
        detect_face()
    elif label==3:
        call()
    elif label == 4:
        read_text('./Img for text extraction/Text-msg.webp')
    else: 
        generate_caption("./img for captioning/download.png")
except:
    say("Something went wrong....")
