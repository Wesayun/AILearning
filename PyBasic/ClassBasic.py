class Dog:
    def __init__(self,name):
        bark_able = True
        self.name = name
    def bark(self):
        print(f"{self.name} bark loudly")
orange_dog = Dog("Orange")
orange_dog.bark()

class Neuron:
    weight = 10
    bias = 1.0
    def forward(self,x):
        return x * self.weight + self.bias
    
neuron1 = Neuron()

print(neuron1.forward(int(input())))