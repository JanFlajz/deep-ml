import torch

def GeLU(x: torch.Tensor) -> torch.Tensor:
    # Your code here
    fnc =  torch.nn.GELU()
    return fnc(x)