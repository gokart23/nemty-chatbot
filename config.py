import torch

MODEL_TYPE = 'bert-base-uncased'
MAX_TOK_LEN = 128

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print ("Using %s" % (device))
