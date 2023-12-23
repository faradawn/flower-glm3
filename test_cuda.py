import torch
print("is avaible:", torch.cuda.is_available())
print("device name:",torch.cuda.get_device_name(0))