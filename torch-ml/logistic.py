import torch.nn as nn 

class BinaryLogisticRegression(nn.Module):

    def __init__(self, input_dim):
        super(BinaryLogisticRegression, self).__init__() #? 
        self.linear = nn.Linear(input_dim, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, input):
        outputs = self.sigmoid(self.linear(input)) # includes the bias term
        return outputs

class MultipleLogisticRegression(nn.Module):

    def __init__(self, input_dim, n_classes):
        super(MultipleLogisticRegression, self).__init__() #? 
        self.linear = nn.Linear(input_dim, n_classes)
        self.softmax = nn.Softmax(dim=n_classes)

    def forward(self, input):
        outputs = self.softmax(self.linear(input)) # includes the bias term
        return outputs
