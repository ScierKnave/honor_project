import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
from torch.utils.data import Dataset, DataLoader, random_split, SubsetRandomSampler, Subset


def generate_dataset(ntrain, ntest):
    mnist_data = datasets.MNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor()
    )
    print(mnist_data)
    mnist_data = Subset(mnist_data, range(ntrain+ntest))
    (train_mnist, test_mnist) = random_split(mnist_data, (ntrain, ntest))

    torch.save(train_mnist, 'src/datasets/train_mnist.pt')
    torch.save(test_mnist, 'src/datasets/test_mnist.pt')
    

generate_dataset(2000, 500)