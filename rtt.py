import time
import requests
import sys
import numpy as np
import matplotlib.pyplot as plt

RTTs = np.array([])
RTTsMean = np.array([])
a = 0.125

def find_roundtriptime(url):
   initial_time = time.time()       #Store the time when request is sent
   request = requests.get(url)
   ending_time = time.time()    #Time when acknowledged the request
   elapsed_time = ending_time - initial_time
   print('The Round Trip Time for {} is {}'.format(url, str(elapsed_time)))
   return elapsed_time

for i in range(10):
    RTTs = np.append(RTTs, find_roundtriptime(sys.argv[1]))

EstimatedRTT = np.mean(RTTs)

for i in range(RTTs.shape[0]):
    EstimatedRTT = (1 - a) * EstimatedRTT + a * RTTs[i]

for i in range(RTTs.shape[0]):
    RTTsMean = np.append(RTTsMean, EstimatedRTT)

plt.plot(RTTs, 'b-')
plt.plot( RTTsMean, 'r-')
plt.show()