# utf-8
# python3.5

import numpy as np
import pandas as pd
import time

np.random.seed(2) # reproducible

N_STATE = 6     # the length of the 1 dimensional world
ACTIONS = ['left', 'right']     # available actions
EPSILON = 0.9   # greed police
ALPHA = 0.1     # learning rate
LAMBDA = 0.9   # discount factor
MAX_EPISODES = 15   # maximum episodes
FRESH_TIME = 0.3    # refresh time for one more

def build_q_table(n_states, actions):
    table = pd.DataFrame(
            np.zeros((n_states, len(actions))),     # q_table initial values
            columns = actions,  # actions's name
            )
    # print table
    return table

# build_q_table(N_STATE, ACTIONS)

def choose_actions(state, q_table):
    # This is hoe to choose an action
    state_action = q_table.iloc[state, :]

    if (np.random.uniform() > EPSILON) or (state_action.all() == 0):     # act non-greedy or state-action have no value
        actions_name = np.random.choice(ACTIONS)
    else:   # act greedy
        actions_name = state_action.argmax()

    return actions_name

def get_env_feedaback(S, A):
    # This is how agent will interact with the enviroment
    if A == 'right':    # move right
        if S == N_STATE - 2:    # terminate
            S_ = 'terminal'
            R = 1
        else:
            S_ = S + 1
            R = 0
    else:   # move left
        R = 0
        if S == 0:
            S_ = S  # reach the wall
        else:
            S_ = S - 1

    return S_, R

def update_env(S, episode, step_counter):
    # This is how environment be updated
    env_list = ['-'] * (N_STATE - 1) + ['T']    # '--------T' our environment
    if S == 'terminal':
        interaction = 'Episode %s: total_steps = %s' % (episode+1, step_counter)
        print('\r{}'.format(interaction),end='') 
        time.sleep(2)
        print('\r                            ', end='')
    else:
        env_list[S] = 'o'
        interaction = ''.join(env_list)
        print('\r{}'.format(interaction), end='')
        time.sleep(FRESH_TIME)

def RL_loop():
    # main part of RL
    q_table = build_q_table(N_STATE, ACTIONS)
    for episode in range(MAX_EPISODES):
        step_counter = 0
        S = 0
        is_terminaled = False
        update_env(S, episode, step_counter)
        while not is_terminaled:
            A = choose_actions(S, q_table)
            S_, R = get_env_feedaback(S, A) # take action & get next state and reward
            q_predict = q_table.ix[S, A]
            if S_ != 'terminal':
                q_target = R + LAMBDA * q_table.iloc[S_, :].max()   # next state is not terminal
            else:
                q_target = R # next state is terminal
                is_terminaled = True    # terminal this episode
            
            q_table.ix[S, A] += ALPHA * (q_target - q_predict)  # update
            S = S_   # move to next step

            update_env(S, episode, step_counter + 1)
            step_counter += 1

    return q_table

if __name__ == "__main__":
    q_table = RL_loop()
    print('\r\nQ-table:\n')
    print(q_table)


