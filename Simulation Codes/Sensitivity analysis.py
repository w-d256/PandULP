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
    
    plt.scatter(time_history,R_history,s=1)

beta_0 = 1/2.2
c = 0.1
gamma = 1/15
delta = 0.2
threshold = 0.0003
threshold_2 = 0.002
epsilon = 0.00001
c_bound = 0.5
gap = 0.05
tightness = []
for i in range(int(c_bound/gap)-1):
    tightness.append(0.5-gap*i)
for c in tightness:
    beta_1 = beta_0*c
    simulation_1(1-epsilon,epsilon,0)
plt.xlabel('Time /day')
plt.ylabel('Proportions')
plt.show()