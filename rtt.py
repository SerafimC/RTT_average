import time
import requests
import sys
import numpy as np
import matplotlib.pyplot as plt

RTTs = np.array([])
RTTsMean = np.array([])
DevRTTMean = np.array([])
a = 0.125
b = 0.25

def find_roundtriptime(url):
   initial_time = time.time()       #Store the time when request is sent
   request = requests.get(url)
   ending_time = time.time()    #Time when acknowledged the request
   elapsed_time = ending_time - initial_time
   print('The Round Trip Time for {} is {}'.format(url, str(elapsed_time)))
   return elapsed_time

for i in range(200):
    RTTs = np.append(RTTs, find_roundtriptime(sys.argv[1]))

EstimatedRTT = np.mean(RTTs)

for i in range(RTTs.shape[0]):
    EstimatedRTT = (1 - a) * EstimatedRTT + a * RTTs[i]
    RTTsMean = np.append(RTTsMean, EstimatedRTT)

DevRTT = np.mean(RTTs)

for i in range(RTTs.shape[0]):
    DevRTT = (1 - b) * DevRTT + b * abs(RTTs[i] - EstimatedRTT)

TimeoutInterval = EstimatedRTT + 4 * DevRTT
    
print("Media Movel Ponderada: " + str(RTTsMean[0]))
print("Desvio Padrao: " + str(DevRTT))
print("Intervalo de timeout: " + str(TimeoutInterval))

plt.plot(RTTs, 'b-') # Amostras
plt.plot(RTTsMean, 'r-') # Media Movel Ponderada
plt.show()