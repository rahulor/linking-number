#import pandas as pd
import pickle

def pickle_to(filename, data):
    pikd = open(filename + '.pickle', 'wb')
    pickle.dump(data, pikd)
    pikd.close()
    
def unpickle_from(filename):
    pikd = open(filename + '.pickle', 'rb')
    data = pickle.load(pikd)
    pikd.close()
    return data

if __name__ == '__main__':
    pass
    