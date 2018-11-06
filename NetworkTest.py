import network.Network as network
import network.minist_loader as minist_loader


if __name__ == '__main__':
    training_data, validation_data, test_data = minist_loader.load_data_wrapper()
    net = network.Network([784,30,10])
    net.SGD(training_data, 30, 10, 3.0, test_data=test_data)