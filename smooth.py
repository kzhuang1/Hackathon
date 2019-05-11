import numpy as np
import matplotlib.pylab as plt

def med_smooth(data,wind_length=10):
    for i in range(wind_length,len(data)):
        data[i] = np.median(data[(i-wind_length):(i+wind_length)])
    return data

def mea_smooth(data,wind_length=10):
    for i in range(wind_length,len(data)):
        data[i] = np.mean(data[(i-wind_length):(i+wind_length)])
    return data

"""
def main():
    noise = np.random.normal(0,0.3,201)
     
    x = np.linspace(-np.pi, np.pi, 201)
    y = np.sin(x)
    plt.plot(x, y)
    plt.xlabel('Angle [rad]')
    plt.ylabel('sin(x)')
    plt.axis('tight')
    plt.show()
    y=y+noise
    
    plt.plot(x, y)
    plt.xlabel('Angle [rad]')
    plt.ylabel('sin(x)')
    plt.axis('tight')
    plt.show()
    
    
    
    y2 = mea_smooth(y,5)
    plt.plot(x, y2)
    plt.xlabel('Angle [rad]')
    plt.ylabel('sin(x)')
    plt.axis('tight')
    plt.show()
    
    y3 = med_smooth(y,5)
    plt.plot(x, y3)
    plt.xlabel('Angle [rad]')
    plt.ylabel('sin(x)')
    plt.axis('tight')
    plt.show()
    
main()
"""