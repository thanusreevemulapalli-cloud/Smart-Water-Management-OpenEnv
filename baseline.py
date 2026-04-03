from smart_water_env import SmartWaterEnv
import random

random.seed(42)

def baseline_policy(state):
    return {
        "household_supply": state["household_demand"],
        "industrial_supply": state["industrial_demand"] * 0.8
    }

env = SmartWaterEnv(task="medium")
state = env.reset()

total_reward = 0

for _ in range(20):
    action = baseline_policy(state)
    state, reward, done, _ = env.step(action)
    total_reward += reward

print("Average Reward:", total_reward / 20)
