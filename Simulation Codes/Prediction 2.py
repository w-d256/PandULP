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
    while time<=60:
        S_history.append(S)
        I_history.append(I)
        R_history.append(R)
        time_history.append(time)
        S = S - beta_1*S*I*delta/population
        I_new = I + beta_1*S*I*delta/population - gamma*I*delta
        R = R + gamma*I*delta
        time = time + delta
        I = I_new
        if count%5==0:
            t = round(time)
            try:
                error = error +(data[t]-I-R)**2
            except OverflowError:
                return
    return error

def plot_figure(initial_S,initial_I,initial_R):
    time = 30
    S = initial_S
    I = initial_I
    R = initial_R
    S_history = []
    time_history = []
    IR_history = []
    count = 0
    while time<=90:
        S_history.append(S)
        IR_history.append(I+R)
        time_history.append(time)
        S = S - beta_1*S*I*delta/population
        I_new = I + beta_1*S*I*delta/population - gamma*I*delta
        R = R + gamma*I*delta
        time = time + delta
        I = I_new 
        count = count+1
        if count %25==0:
            print('time:',time+30)
            print('model:',I+R)
            print('data:',data[round(time)-30])
    S_history.append(S)
    IR_history.append(I+R)
    time_history.append(time)
    plt.scatter(time_history,IR_history,s=3,c='wheat',label = 'Infective and removed_model')
    plt.scatter(checkpoint,data,s=3,label= 'Infective and removed_data')
    plt.xlabel('Time /day')
    plt.ylabel('Number of infections and removed')
    plt.legend()
    plt.show()

data = [42952,51178,60184,73538,90615,110597,131819,155443,180386,206473,229815,256145,283864,306936,330449,355269,377517,397933,416834,435329,452958,476328,497386,516841,533821,547383,558005,573037,583218,591090,598423,604092,609074,613725,617994,622208,626183,630130,633144,634631,636080,638176,639857,641226,642164,642987,643842,644561,645419,646287,646909,647467,647947,648334,648672,648936,649106,649228,649295,649326,649341]
length = len(data)
population = 25000000
checkpoint = []
for i in range(length):
    checkpoint.append(30+i)
min_error = float('inf')
gap_2 = 0.005
delta = 0.2

for j in range(250):
    for k in range(250):
        gamma = gap_2*j
        beta_1 = k*gap_2
        e = simulation(population-42400,27600,14800)
        if e:
            if e <= min_error:
                print('error:',e,'beta_1:',beta_1,'gamma=',gamma)
                min_error = e
                marker = beta_1
                marker_1 = gamma
gamma = marker_1
beta_1 = marker
plot_figure(population-42400,27600,14800)