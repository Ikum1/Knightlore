
#!pip install tensorflow==2.3.2 gym keras-rl2 gym[atari]

import gym
import random
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Convolution2D
from tensorflow.keras.optimizers import Adam
#We will use the keras DQN agent. COuld pick from the agent list here https://keras-rl.readthedocs.io/en/latest/
from rl.agents import DQNAgent
#Sequential memory allows us to hold a knowledge  from previous games for our agent
from rl.memory import SequentialMemory
#Greedy lets us find the best score
from rl.policy import LinearAnnealedPolicy, EpsGreedyQPolicy


#The window length is our memory length. Totally custom and doesn't have to be 3.
windowLength = 3
memoryLimit = 1000
learningRate = 1e-4
warmupSteps = 1000
#nbSteps = 10000
nbSteps = 10000
verbosity = 2
nbEpisodes = 10


#Grabs game enviroment from gym (the website)
env = gym.make('SpaceInvaders-v0')
#env = gym.make('SpaceInvaders-v0')
#Grabs the game window from gym
height, width, channels = env.observation_space.shape
#Grabs the possible inputs of the game from gym
actions = env.action_space.n


#Display what actions a player can make
env.unwrapped.get_action_meanings()
print(env.unwrapped.get_action_meanings())


def random_Game():
    #This is complete random action just to test our enviroment.
    #No reason for this to be specifically 5
    episodes = 5
    for episode in range(1, episodes+1):
      #Gets rid of any stats from the previous episode
      state = env.reset()
      done = False
      score = 0
    
      while not done:
        env.render()
        #makes completely random choice. We are just picking a random index from our list that correlates to an action.
        #action = random.choice([0, 1, 2, 3, 4, 5])
        action = random.choice([0, 1, 2, 3])
        #Gets new state after appling random action
        n_state, reward, done, info = env.step(action)
        score += reward
    
      print('Episode: {} Score: {}'.format(episode, score))
    
    env.close()

#random_Game()


def build_model(height, width, channels, actions):
    #Pass in arguments as it will obviously affect our input layer.
    #Strides are over each pixel. If not specified then strides are 1,1 . Consider alreting the CNN stacking later.
    #Don't forget to flatten before Dense.
    model = Sequential()
    model.add(Convolution2D(32, (8,8), strides=(4,4), activation='relu', input_shape=(windowLength,height, width, channels)))
    model.add(Convolution2D(64, (4,4), strides=(2,2), activation='relu'))
    model.add(Convolution2D(64, (3,3), activation='relu'))
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dense(256, activation='relu'))
    model.add(Dense(actions, activation='linear'))
    return model



model = build_model(height, width, channels, actions)

model.summary()



def build_agent(model, actions):
    policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps', value_max=1., value_min=.1, value_test=.2, nb_steps=10000)
    memory = SequentialMemory(limit= memoryLimit, window_length=windowLength)
    dqn = DQNAgent(model=model, memory=memory, policy=policy,
                  enable_dueling_network=True, dueling_type='avg', 
                   nb_actions=actions, nb_steps_warmup= warmupSteps)
    return dqn



def train(model_p):
    dqn_n = build_agent(model_p, actions)
    dqn_n.compile(Adam(lr= learningRate))
    dqn_n.fit(env, nb_steps= nbSteps, visualize=False, verbose= verbosity)
    dqn_n.save_weights('./savedWeights/new/dqn_weights.h5f')
    
    return dqn_n
   


def load_pregen():
    model = build_model(height, width, channels, actions)
    
    dqn_n = build_agent(model, actions)
    dqn_n.compile(Adam(lr= learningRate))
    
    dqn_n.load_weights('./savedWeights/SpaceInvaders/1m/dqn_weights.h5f')
    
    return dqn_n


#del model
#del dqn

dqn = train(model) 
#dqn = load_pregen()

scores = dqn.test(env, nb_episodes= nbEpisodes, visualize=True)
print(np.mean(scores.history['episode_reward']))
env.close()












