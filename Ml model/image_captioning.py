import torch
from PIL import Image
from lavis.models import load_model_and_preprocess
import os
from audio import say
import cv2
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def generate_caption(img_path):
    
    raw_image = Image.open(img_path).convert("RGB")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # loads BLIP caption base model, with finetuned checkpoints on MSCOCO captioning dataset.
    # this also loads the associated image processors
    model, vis_processors, _ = load_model_and_preprocess(name="blip_caption", model_type="base_coco", is_eval=True, device=device)

    # preprocess the image
    # vis_processors stores image transforms for "train" and "eval" (validation / testing / inference)
    image = vis_processors["eval"](raw_image).unsqueeze(0).to(device)
    # generate caption
    text = model.generate({"image": image})
    say(text)
    return text
    
# generate_caption("./img for captioning/download.png")

def realtime_caption():
    cam = cv2.VideoCapture(0)
    res, image = cam.read()
    path = "Img for captioning/generate.jpg"
    cv2.imwrite(path,image)
    cam.release()
    cv2.destroyAllWindows()
    generate_caption(path)