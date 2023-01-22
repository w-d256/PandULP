from matplotlib import pyplot as plt

def simulation(initial_S,initial_I,initial_R):
    time = 0
    count = 0
    error = 0
    S = initial_S
    I = initial_I
    R = initial_R
    S_history = []
    I_history = []
    R_history = []
    time_history = []
    while time<=29:
        S_history.append(S)
        I_history.append(I)
        R_history.append(R)
        time_history.append(time)
        S = S - beta_0*S*I*delta/population
        I_new = I + beta_0*S*I*delta/population - gamma*I*delta
        R = R + gamma*I*delta
        time = time + delta
        I = I_new
        if count%5==0:
            t = round(time)
            try:
                error = error + (data[t]-I-R)**2
            except OverflowError:
                return
    return error

def plot_figure(initial_S,initial_I,initial_R):
    time = 0
    error = 0
    S = initial_S
    I = initial_I
    R = initial_R
    S_history = []
    I_history = []
    time_history = []
    IR_history = []
    count = 0
    while time<=29:
        S_history.append(S)
        IR_history.append(I+R)
        time_history.append(time)
        S = S - beta_0*S*I*delta/population
        I_new = I + beta_0*S*I*delta/population - gamma*I*delta
        R = R + gamma*I*delta
        time = time + delta
        I = I_new 
        count = count + 1
        if count %25==0:
            print('time:',time)
            print('model:',I+R)
            print('data:',data[round(time)])
    print('time:',time)
    print('model:',I+R)
    print('data:',data[round(time)])
    S_history.append(S)
    IR_history.append(I+R)
    time_history.append(time)
    plt.scatter(time_history,IR_history,s=3,c='wheat',label = 'Infective and removed_model')
    plt.scatter(checkpoint,data,s=3,label= 'Infective and removed_data')
    plt.xlabel('Time /day')
    plt.ylabel('Number of infections and removed')
    plt.legend()
    plt.show()

data = [10,26,45,73,121,176,241,321,396,479,544,713,852,1054,1212,1472,1846,2355,3113,4009,4990,5973,7582,9851,12527,16027,20504,26486,32139,36641]
length = len(data)
population = 25000000
checkpoint = []
for i in range(30):
    checkpoint.append(i)
min_error = float('inf')
gap = 0.005
delta = 0.2

for i in range(400):  
    for j in range(300):
        gamma = gap*j
        beta_0 = 0.3+i*gap
        e = simulation(population-data[0],data[0],0)
        if e:
            if e <= min_error:
                print('error:',e,'beta:',beta_0,'gamma=',gamma)
                min_error = e
                marker = beta_0
                marker_1 = gamma

gamma = marker_1
beta_0 = marker
plot_figure(population-data[0],data[0],0)


