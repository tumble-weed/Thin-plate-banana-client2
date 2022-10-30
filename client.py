import banana_dev as banana
import json
import argparse
import base64 #
import skimage.io #
from PIL import Image #
TODO = None
def encodeBase64Image(image: Image) -> str:
    # https://stackoverflow.com/questions/31826335/how-to-convert-pil-image-image-object-to-base64-string
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

def main(args):
    #===============================================
    # SECRETS
    secrets = json.load('secrets.json')
    api_key = secrets['API_KEY']
    model_key = secrets['MODEL_KEY']
    #===============================================
    # REQUEST
    image  = skimage.io.imread(args.impath)
    image = Image.fromarray(image)
    image_base64 = encodeBase64Image(image)
    request_json = {'image':image_64}
    model_inputs = request_json
    # model_inputs = {YOUR_MODEL_INPUT_JSON} # anything you want to send to your model
    #===============================================
    # RESPONSE
    out = banana.run(api_key, model_key, model_inputs)
    model_outputs = out['modelOutputs']
    video_base64 = model_outputs['result']
    with open(args.output_path,'wb') as f:
        f.write(base64.b64decode(video_base64))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--impath',type=str,default='assets/source.png')
    parser.add_argument('--output-path',type=str,defualt='result.mp4')
    args = parser.parse_args()
    main(args)
