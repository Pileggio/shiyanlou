# coding=<utf-8>
import numpy as np
import pandas as pd



def gradient_descent():
    df = pd.read_csv('nyc-east-river-bicycle-counts.csv', index_col=0)
 
    x = df['Brooklyn Bridge'].values
    
    y = df['Manhattan Bridge'].values
  
    

    w = 0  
    b = 0  
    lr = 0.000000001  
    num_iter = 1000  
    for i in range(num_iter):  
     
        y_hat = (w * x) + b
   
        w_gradient = -(2/len(x)) * sum(x * (y - y_hat))
        b_gradient = -(2/len(x)) * sum(y - y_hat)
        
        w -= lr * w_gradient
        b -= lr * b_gradient
    print(w,b)
    return w, b

gradient_descent()

