#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np  
import matplotlib.pyplot as plt

areas = []
intervals = [(-1.4142,-1.0),(-1.0,1.0),(1.0,1.4142)]


print("Results for equation np.sqrt(np.absolute(x)) + np.sqrt(2-x**2):\n")
for a, b in intervals:
    f = lambda x : np.sqrt(np.absolute(x)) + np.sqrt(2-x**2)
    N = 100
    n = 20 # Use n*N+1 points to plot the function smoothly
    x = np.linspace(a,b,N+1)
    y = f(x)
    
    X = np.linspace(a,b,n*N+1)
    Y = f(X)
    plt.plot(X,Y)
    for i in range(N):
        xs = [x[i],x[i],x[i+1],x[i+1]]
        ys = [0,f(x[i]),f(x[i+1]),0]
        plt.fill(xs,ys,'b',edgecolor='b',alpha=0.2)
        
    plt.title('Trapezoid Rule, N = {}'.format(N))
    y = f(x)
    y_right = y[1:] # Right endpoints
    y_left = y[:-1] # Left endpoints
    dx = (b - a)/N
    T = (dx/2) * np.sum(y_right + y_left)
    areas.append(T)
    print("The area for the interval "+str(a)+" to "+str(b)+" is "+str(T))

    print("\n\nResults for equation np.sqrt(np.absolute(x)) - np.sqrt(2-x**2):\n")
for a, b in intervals:
    f = lambda x : np.sqrt(np.absolute(x)) - np.sqrt(2-x**2)
    N = 100
    n = 20 # Use n*N+1 points to plot the function smoothly
    x = np.linspace(a,b,N+1)
    y = f(x)
    
    X = np.linspace(a,b,n*N+1)
    Y = f(X)
    plt.plot(X,Y)
    for i in range(N):
        xs = [x[i],x[i],x[i+1],x[i+1]]
        ys = [0,f(x[i]),f(x[i+1]),0]
        if a == -1.0:
            plt.fill(xs,ys,'b',edgecolor='b',alpha=0.2)
        else:
            plt.fill(xs,ys,'b',edgecolor='r',alpha=0.2)
        
    plt.title('Trapezoid Rule, N = {}'.format(N))
    y = f(x)
    y_right = y[1:] # Right endpoints
    y_left = y[:-1] # Left endpoints
    dx = (b - a)/N
    T = (dx/2) * np.sum(y_right + y_left)
    areas.append(-(T))
    print("The area for the interval "+str(a)+" to "+str(b)+" is "+str(T))


plt.show()

totarea = sum(areas)
area = round(totarea, 4)
print("The total area for the shape is {}".format(area))

