from matplotlib import pyplot as plt

def simulation_1(initial_S,initial_I,initial_R):
    time = 0
    S = initial_S
    I = initial_I
    R = initial_R
    S_history = []
    I_history = []
    R_history = []
    time_history = []
    lockdown = False
    while I>=epsilon:
        S_history.append(S)
        I_history.append(I)
        R_history.append(R)
        time_history.append(time)
        if lockdown:
            S = S - beta_1*S*I*delta
            I_new = I + beta_1*S*I*delta - gamma*I*delta
            R = R + gamma*I*delta
            time = time + delta
        else:
            S = S - beta_0*S*I*delta
            I_new = I + beta_0*S*I*delta - gamma*I*delta
            R = R + gamma*I*delta
            time = time + delta
        if not lockdown:
            if I_new - I >threshold:
                lockdown = True
                lockdown_start = time
        I = I_new
    S_history.append(S)
    I_history.append(I)
    R_history.append(R)
    time_history.append(time)
    print('c=',c)
    print('Policy 1:')
    print('Uninfected at the end',S)
    print('total time',time)
    print('lockdown time',time-lockdown_start)
    print('estimated economic loss:', (time-lockdown_start)*(1-c))
    plt.scatter(time_history,S_history,s=3,c='lightsteelblue',label = 'Susceptible_1')
    plt.scatter(time_history,I_history,s=3,c='wheat',label = 'Infective_1')
    plt.scatter(time_history,R_history,s=3,c='lightgreen',label = 'Removed_1')

def simulation_2(initial_S,initial_I,initial_R):
    time = 0
    S = initial_S
    I = initial_I
    R = initial_R
    S_history = []
    I_history = []
    R_history = []
    time_history = []
    lockdown = False
    while I>=epsilon:
        S_history.append(S)
        I_history.append(I)
        R_history.append(R)
        time_history.append(time)
        if lockdown:
            S = S - beta_1*S*I*delta
            I_new = I + beta_1*S*I*delta - gamma*I*delta
            R = R + gamma*I*delta
            time = time + delta
        else:
            S = S - beta_0*S*I*delta
            I_new = I + beta_0*S*I*delta - gamma*I*delta
            R = R + gamma*I*delta
            time = time + delta
        if not lockdown:
            if I_new>threshold:
                lockdown = True
                lockdown_start = time
        I = I_new
    S_history.append(S)
    I_history.append(I)
    R_history.append(R)
    time_history.append(time)
    print('Policy 2:')
    print('Uninfected at the end',S)
    print('total time',time)
    print('lockdown time',time-lockdown_start)
    print('estimated economic loss:', (time-lockdown_start)*(1-c))
    plt.scatter(time_history,S_history,s=3,label = 'Susceptible_2')
    plt.scatter(time_history,I_history,s=3,label = 'Infective_2')
    plt.scatter(time_history,R_history,s=3,label = 'Removed_2')
    

beta_0 = 1/2.2
c = 0.1
gamma = 1/15
delta = 0.2
threshold = 0.0003
threshold_2 = 0.002
epsilon = 0.00001
beta_1 = beta_0*c
simulation_1(1-epsilon,epsilon,0)
simulation_2(1-epsilon,epsilon,0)
plt.xlabel('Time /day')
plt.ylabel('Proportions')
title = 'Trajectory when c=' + str(c)
plt.title(title)
plt.legend()
plt.show()