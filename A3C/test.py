import numpy as np
from scipy import signal

"""gamma = 0.99
def discount_rewards(r):
     #take 1D float array of rewards and compute discounted reward
    discounted_r = np.zeros_like(r)
    running_add = 0
    for t in reversed(xrange(0, r.size)):
        running_add = running_add * gamma + r[t]
        discounted_r[t] = running_add
    return discounted_r

def discount(x, gamma):
    return signal.lfilter([1], [1, -gamma], x[::-1], axis=0)[::-1]

reward = np.asarray([10,6,4,1])

print "1: ",discount_rewards(reward)  
print "2: ",discount(reward,gamma)  
"""

a= np.ndarray(shape=(2,,))
a.append([[1],[2]])
a.append([[2],[4],[5]])
print a
print np.concatenate(a, axis=0)
