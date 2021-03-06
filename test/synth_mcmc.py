# Run as script using 'python -m test.synth'
from glm_shared import *
from models.model_factory import *
from inference.gibbs import gibbs_sample

import cPickle
import numpy as np
import scipy.io

from inference.coord_descent import coord_descent
from utils.avg_dicts import *
from synth_harness import initialize_test_harness

def run_synth_test():
    """ Run a test with synthetic data and MCMC inference
    """
    # Make a population with N neurons
    N = 2
    population, data, x_true = initialize_test_harness(N)
    
    # Sample random initial state
    x0 = population.sample()
    ll0 = population.compute_log_p(x0)
    print "LL0: %f" % ll0

    # Perform inference
    x_inf = gibbs_sample(population, data, x0=x0, N_samples=1000)
    ll_inf = population.compute_log_p(x_inf)
    print "LL_inf: %f" % ll_inf

    # Save results
    
    # Plot results
    plot_results(population, x_true, x_inf)

if __name__ == "__main__":
    run_synth_test()
