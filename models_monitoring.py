#librarys

import numpy as np
from scipy.stats import wasserstein_distance
import matplotlib.pyplot as plt


def wasserstein_jensen_shannon_distances(p,q):
    wasserstein_dist = wasserstein_distance(p,q)
    print(f"Distancia de Wasserstein: {wasserstein_dist}")
    
    m = 0.5 * (p + q)
    js_distance = 0.5 * (wasserstein_distance(p, m) + wasserstein_distance(q,m))
    print(f"Distancia de Jensen-Shannon: {js_distance}")
    
    
    fig, ax = plt.subplots()
    ax.hist(p,density=True)
    
    fig, ax = plt.subplots()
    ax.hist(p,density=True,)
    
    


data_distribution_1 = np.array([0.2, 0.3, 0.1, 0.4])
data_distribution_2 = np.array([0.1, 0.4, 0.2, 0.3])

wasserstein_jensen_shannon_distances(p=data_distribution_1,q=data_distribution_2)