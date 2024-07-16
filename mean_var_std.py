import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    
    array = np.reshape(list, [3,3])

    calculations = {}
    calculations['mean'] = [array.mean(axis = 0, dtype = float).tolist(), array.mean(axis = 1, dtype = float).tolist(), array.mean(dtype = float).tolist()]
    calculations['variance'] = [array.var(axis = 0, dtype = float).tolist(), array.var(axis = 1, dtype = float).tolist(), array.var(dtype = float).tolist()]
    calculations['standard deviation'] = [array.std(axis = 0, dtype = float).tolist(), array.std(axis = 1, dtype = float).tolist(), array.std(dtype = float).tolist()]
    calculations['max'] = [array.max(axis = 0).tolist(), array.max(axis = 1).tolist(), array.max().tolist()]
    calculations['min'] = [array.min(axis = 0).tolist(), array.min(axis = 1).tolist(), array.min().tolist()] 
    calculations['sum'] = [array.sum(axis = 0).tolist(), array.sum(axis = 1).tolist(), array.sum().tolist()]
    
    return calculations

print(calculate([2,6,2,8,4,0,1,5,7]))