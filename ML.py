from tabpy.tabpy_tools.client import Client
import numpy as np

client = Client('http://localhost:9004/')

def pearson_correlation_coefficient(x,y):
    return np.corrcoef(x,y)[0,1]
print("function created")

client.deploy('pcc',pearson_correlation_coefficient,'correlation coefficient is extracted of x and y',override='True')    

print("function Deployed")