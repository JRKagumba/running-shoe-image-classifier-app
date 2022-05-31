import io
from PIL import Image
import torch
import torch.nn as nn
from torchvision import transforms, models


AlexNet_model_load_path='image_models\Epochs300_TestAcc26_shoeimage_model.pt'
class_names = ['adidas', 
               'altra', 
               'asics', 
               'brooks', 
               'hoka', 
               'mizuno', 
               'newbalance', 
               'nike', 
               'onrunning', 
               'puma', 
               'reebok', 
               'saucony', 
               'skechers', 
               'underarmour']

proper_names_dict = {
    'adidas': 'Adidas', 
    'altra' : 'Altra', 
    'asics' : 'Asics', 
    'brooks': 'Brooks', 
    'hoka' :  'Hoka', 
    'mizuno' : 'Mizuno', 
    'newbalance' : 'New Balance', 
    'nike' : 'Nike', 
    'onrunning' : 'ON Running', 
    'puma': 'Puma', 
    'reebok':'Reebok', 
    'saucony':'Saucony', 
    'skechers':'Skechers', 
    'underarmour':'Under Armour'}

test_transform = transforms.Compose([
    transforms.Resize(size=223, max_size=224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                          [0.229, 0.224, 0.225])
    ])

def get_model():
    AlexNet_model = models.alexnet(pretrained=True)
    in_feats = AlexNet_model.classifier[6].in_features
    AlexNet_model.classifier[6] = nn.Linear(in_feats, 14)
    AlexNet_model.load_state_dict(torch.load(AlexNet_model_load_path), strict=False)
    AlexNet_model.eval()
    return AlexNet_model

def transform_image(image_bytes, transformation):
    image = Image.open(io.BytesIO(image_bytes))
    return transformation(image).unsqueeze(0)

def get_class_names(values, indicies):
    rounded_values = [round(val, 3) for val in values.tolist()[0]]  
    shoe_names = [proper_names_dict[class_names[index]] for index in indicies.tolist()[0]]
    return list(zip(shoe_names, rounded_values))

def get_top_5_predictions(image_bytes, model):
    tensor = transform_image(image_bytes=image_bytes, transformation=test_transform)
    outputs = model.forward(tensor)
    values, indicies = outputs.topk(5)
    return get_class_names(values, indicies)

# def diplay_image(image_bytes):
#     image = Image.open(io.BytesIO(image_bytes))
#     return image