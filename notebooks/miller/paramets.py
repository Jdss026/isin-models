import torch

# Simulating the TDGL equation
a, b, c, k = -1.0, 1.0, 0.1, 1.0 #configuração: (a<0, b>0) ou (a>0, b>0)
dh, dt = 1.0, 1e-3
Ng, Tf = 64, 10001

a = torch.tensor(a, device='cpu')
b = torch.tensor(b, device='cpu')
k = torch.tensor(k, device='cpu')
dh = torch.tensor(dh, device='cpu')
dt = torch.tensor(dt, device='cpu')
Ng = torch.tensor(Ng, device='cpu')
Tf = torch.tensor(Tf, device='cpu')
# T = torch.tensor([0.5], device='cpu')

# Ng, Tf = 64, 10001