# from django.shortcuts import render
# from django.http import HttpResponse
# import random
# import json
# from time import sleep
# #import torch
# from .model import NeuralNet
# from .nltk_utils import bag_of_words, tokenize
# import torch



# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# intents_path = "E:\\C\\Graduation project\\backend\\chatbot\\intents\\intents.json"

# with open(intents_path, 'r') as json_data:
#     intents = json.load(json_data)

# FILE = "E:\\C\\Graduation project\\backend\\chatbot\\intents\\data.pth"
# data = torch.load(FILE)

# input_size = data["input_size"]
# hidden_size = data["hidden_size"]
# output_size = data["output_size"]
# all_words = data['all_words']
# tags = data['tags']
# model_state = data["model_state"]

# model = NeuralNet(input_size, hidden_size, output_size)
# model.load_state_dict(model_state)
# model.eval()

# bot_name = "Sam"
# def get_response(msg):
#     sentence = tokenize(msg)
#     X = bag_of_words(sentence, all_words)
#     X = X.reshape(1, X.shape[0])
#     X = torch.from_numpy(X).to(device)

#     output = model(X)
#     _, predicted = torch.max(output, dim=1)

#     tag = tags[predicted.item()]

#     probs = torch.softmax(output, dim=1)
#     prob = probs[0][predicted.item()]
#     if prob.item() > 0.75:
#         for intent in intents['intents']:
#             if tag == intent["tag"]:
#                 return random.choice(intent['responses'])
    
#     return "I do not understand..."
   

# def chat(request):
#     return render(request,"chatbot/chat.html")

# def get_bot_response(request):
#     text = request.POST.get('message')
#     response = get_response(text)
#     return render(request,"chatbot/chat.html",{'response':response,'text':text})