# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 09:36:15 2021

@author: a.h
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 19:24:13 2020

@author: a.h
"""

def Q_Learning_Algorithm (fault,state,State,Reward,Policy,CSTH_model,loop_circle,y_out,error_mse):
    import numpy as np
    actions11=list(range(-2,3)) 
    state11=list(range(0,11))
    loop_Q_Learning = 0
    alpha=0.1#float(input('Enter alpha:   '))
    gama=1 # float(input('Enter gama:   '))
    epsilon = 0.1
    # Q=np.random.rand(np.size(state11),np.size(actions11))
    # Q[0,:]=0
    Q = np.zeros((np.size(state11),np.size(actions11))) 
    while state >0 :
        A = Policy(Q,state,epsilon)
        S_perim = State(A,fault,CSTH_model)
        R = Reward(S_perim)
        Q[state,A] = Q[state,A] + alpha * (R + gama * max(Q[S_perim,:])-Q[state,A])
        state = S_perim
        y_out[loop_circle] = CSTH_model(A) + fault
        error_mse[loop_circle] = (125 - y_out[loop_circle])**2
        loop_Q_Learning += 1
        loop_circle += 1
    return (A,y_out,loop_circle,loop_Q_Learning,error_mse)
        

