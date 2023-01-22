from matplotlib import pyplot as plt

def simulation(initial_S,initial_I,initial_R):
    time = 0
    S = initial_S
    I = initial_I
    R = initial_R
    S_history = []
    I_history = []
    R_history = []
    time_history = []
    I_max = 0
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
        if I>I_max:
            I_max = I
            peak_time = time
    S_history.append(S)
    I_history.append(I)
    R_history.append(R)
    time_history.append(time)
    print(c)
    #print('total time',time)
    #print('total infections',I+R)
    #print('I max:',I_max)
    print('lockdown time',(time-lockdown_start), (time-lockdown_start)*(1-c))
    return (time-lockdown_start), (time-lockdown_start)*(1-c)
    print('Uninfected at the end',S)
    
    print('lockdown time',time-lockdown_start)
    plt.scatter(time_history,S_history,s=10,label = 'Susceptible')
    plt.scatter(time_history,I_history,s=10,label = 'Infective')
    plt.scatter(time_history,R_history,s=10,label = 'Removed')
    plt.xlabel('Time /day')
    
    plt.ylabel('Proportions')
    title = 'Trajectory when c=' + str(c)
    plt.title(title)
    plt.legend()
    plt.show()

beta_0 = 1/2.2
c = 0.1
delta = 0.05
tightness = []
c_bound = 0.5
for i in range(int(c_bound/delta)-1):
    tightness.append(0.5-delta*i)
gamma = 1/15
delta = 0.2
threshold = 0.0003
epsilon = 0.00001
beta_1 = beta_0*c
duration = []
peak = []
max = 0
max_change = 0
pre = -1
for c in tightness:
    beta_1 = beta_0*c
    i,t = simulation(1-epsilon,epsilon,0)
    #if pre == -1:
    #    pre = t
    #else:
    #    change = pre-t
    #    if change > max_change:
    #        max_change = change
    #        mark = c
    #    pre = t
#    if t>max:
#        max = t
#        mark = c
    #duration.append(i)
    #peak.append(t)
#plt.subplot(2,1,1)
#plt.plot(tightness,peak)
#plt.ylabel('Estimated economic loss')
#plt.subplot(2,1,2)
#plt.plot(tightness, peak)
#plt.xlabel('Value of c')
#plt.ylabel('Time when peak appears')
#plt.show()
#simulation(1-epsilon, epsilon,0)
    