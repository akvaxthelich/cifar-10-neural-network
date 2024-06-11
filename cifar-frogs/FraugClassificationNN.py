import torch
import torch.nn as nn

class FraugClassificationNN(nn.Module):
    def __init__(self):
        super().__init__()

        self.model = nn.Sequential(

            nn.Linear(1024, 600),
            nn.Sigmoid(),
            nn.Linear(600, 300),
            nn.Sigmoid(),
            nn.Linear(300, 50),
            nn.Sigmoid(),
            nn.Linear(50, 1)

            #classify!
        )
        self.loss_function = nn.MSELoss()
        self.optimiser = torch.optim.SGD(self.parameters(), lr = 0.1)

    def forward(self, inputs):
        inputs = torch.FloatTensor(inputs)
        return self.model(inputs)
    
    def train(self, inputs, targets):
        targets = torch.FloatTensor(targets)
        outputs = self.forward(inputs)

        loss = self.loss_function(outputs, targets)

        self.optimiser.zero_grad()

        loss.backward()
        self.optimiser.step()
