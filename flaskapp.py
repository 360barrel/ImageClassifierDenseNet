import torch
import numpy as np
import io 
import json
import os
import torchvision.models as models
import torchvision.transforms as transforms 
from PIL import Image
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
model = models.densenet121(pretrained=True)
model.eval()

img_class_map = None
mapping_file_path = 'index_to_name.json'
if os.path.isfile(mapping_file_path):
  with open (mapping_file_path) as f:
    img_class_map = json.load(f)


def transform_image(infile):
    img = Image.open(infile).convert('RGB')
    width, height = img.size
    shortest_side = min(width, height)

    scale_factor = 256 / shortest_side

    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)

    img_resized = img.resize((new_width, new_height), Image.Resampling.BILINEAR)

    # Center crop
    crop_size = 224
    left = (new_width - crop_size) // 2
    top = (new_height - crop_size) // 2
    right = left + crop_size
    bottom = top + crop_size

    img_cropped = img_resized.crop((left, top, right, bottom))

    # Convert to NumPy array
    img_np = np.array(img_cropped).astype(np.float32)

    # Normalize the image
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    img_normalized = (img_np / 255.0 - mean) / std
    
    img_np = img_normalized.transpose((2, 0, 1))  # Channels first
    img_tensor = torch.tensor(img_np, dtype=torch.float32).unsqueeze(0)
    
    return img_tensor


def get_prediction(input_tensor):
  outputs = model.forward(input_tensor)
  _, y_hat = outputs.max(1)
  prediction = y_hat.item()
  return prediction

def render_prediction(prediction_idx):
  stridx = str(prediction_idx)
  class_name = 'Unknown'
  if img_class_map is not None:
    class_name = img_class_map[stridx]
  return prediction_idx, class_name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/root', methods=['GET'])
def root():
    return jsonify({'msg' : 'Try POSTing to the /predict endpoint with an RGB image attachment'})


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        if file is not None:
            input_tensor = transform_image(file)
            prediction_idx = get_prediction(input_tensor)
            class_id, class_name = render_prediction(prediction_idx)
            return jsonify({'class_id': class_id, 'class_name': class_name})


if __name__ == '__main__':
    app.run()
