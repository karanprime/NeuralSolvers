import torch
import numpy as np
from pyDOE import lhs
from .Sampler import Sampler


class LHSSampler(Sampler):
    def __init__(self):
        """
        Constructor of the LHSSampler class
        """
        super(LHSSampler, self).__init__()

    def sample(self, lb, ub, n):        
        """Generate 'n' number of sample points in [lb,ub]
        
        Args:
            lb (numpy.ndarray): lower bound of the domain.
            ub (numpy.ndarray): upper bound of the domain.
            n (int): the number of sampled points.
        """
            
        torch.manual_seed(42)
        np.random.seed(42)
        
        lb =  lb.reshape(1,-1)
        ub =  ub.reshape(1,-1)
        
        dimension = lb.shape[1]
        xf = lb + (ub - lb) * lhs(dimension, n)
        return torch.tensor(xf).float()