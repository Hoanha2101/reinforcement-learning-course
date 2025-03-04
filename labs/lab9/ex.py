import numpy as np

class SoftmaxPolicy:
    def __init__(self, num_actions, temperature):
        self.num_actions = num_actions
        self.temperature = temperature

    def select_action(self, q_values):
        probabilities = self.softmax(q_values)
        print("probabilities", probabilities)
        # probabilities [0.08714432 0.64391426 0.0320586  0.23688282]
        # hành động có giá trị Q cao hơn sẽ có xác suất được chọn lớn hơn.
        
        action = np.random.choice(self.num_actions, p=probabilities) 
        return action

    def softmax(self, q_values):
        scaled_values = q_values / self.temperature
        exp_values = np.exp(scaled_values)
        probabilities = exp_values / np.sum(exp_values)
        return probabilities

# Example usage:
num_actions = 4  # Up, Down, Left, Right
temperature = 0.5  # Softmax temperature

# Initialize a softmax policy
softmax_policy = SoftmaxPolicy(num_actions, temperature)

# Example Q-values (arbitrary values for illustration)
q_values = np.array([1.0, 2.0, 0.5, 1.5])

# Select an action based on the softmax policy
selected_action = softmax_policy.select_action(q_values)
print("Selected Action:", selected_action)
