# Lab 2.2 implement Temporal Difference- HoaDNt@fe.edu.vn
import numpy as np

class GridWorld:
    def __init__(self):
        
        # [0, 0, 0], 
        # [0, 0, 0], 
        # [0, 0, 1]
        
        self.grid_size = (3, 3)
        self.start_state = (0, 0)
        self.goal_state = (2, 2)
        self.num_actions = 4  # Up, Down, Left, Right

    def step(self, state, action):
        row, col = state
        if action == 0:  # Up
            row = max(0, row - 1)
        elif action == 1:  # Down
            row = min(self.grid_size[0] - 1, row + 1)
        elif action == 2:  # Left
            col = max(0, col - 1)
        elif action == 3:  # Right
            col = min(self.grid_size[1] - 1, col + 1)

        next_state = (row, col)
        reward = -1
        if next_state == self.goal_state:
            reward = 10
        return next_state, reward

def td_learning(grid_world, num_episodes, alpha, gamma):
    V = np.zeros(grid_world.grid_size)  # Value function initialization

    for _ in range(num_episodes):
        state = grid_world.start_state
        while state != grid_world.goal_state:
            action = np.random.randint(grid_world.num_actions)  # Random action
            next_state, reward = grid_world.step(state, action)
            V[state] += alpha * (reward + gamma * V[next_state] - V[state])
            state = next_state
    return V

# Create a grid world environment
grid_world = GridWorld()

# Perform Temporal Difference learning
num_episodes = 1000
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
values = td_learning(grid_world, num_episodes, alpha, gamma)

print("Value function:")
print(values)
