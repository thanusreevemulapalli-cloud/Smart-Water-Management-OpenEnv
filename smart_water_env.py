import random

class SmartWaterEnv:
    def __init__(self, task="easy"):
        self.task = task
        self.reset()

    def reset(self):
        if self.task == "easy":
            self.state_data = {
                "reservoir_level": random.uniform(700, 1000),
                "household_demand": random.uniform(100, 200),
                "industrial_demand": random.uniform(100, 200),
                "energy_cost": random.uniform(1, 3),
                "leakage_rate": random.uniform(0.05, 0.1)
            }

        elif self.task == "medium":
            self.state_data = {
                "reservoir_level": random.uniform(500, 900),
                "household_demand": random.uniform(150, 300),
                "industrial_demand": random.uniform(150, 300),
"energy_cost": random.uniform(2, 6),
                "leakage_rate": random.uniform(0.1, 0.2)
            }

        else:  # hard
            self.state_data = {
                "reservoir_level": random.uniform(300, 600),
                "household_demand": random.uniform(200, 400),
                "industrial_demand": random.uniform(200, 400),
                "energy_cost": random.uniform(3, 8),
                "leakage_rate": random.uniform(0.2, 0.3)
            }

        return self.state()

    def state(self):
        return self.state_data

    def step(self, action):
        demand_met = min(action["household_supply"], self.state_data["household_demand"]) + \
                     min(action["industrial_supply"], self.state_data["industrial_demand"])

        total_demand = self.state_data["household_demand"] + self.state_data["industrial_demand"]

        efficiency = demand_met / (total_demand + 1e-5)
      penalty = (
            max(0, action["household_supply"] + action["industrial_supply"] - self.state_data["reservoir_level"]) * 0.1
            + self.state_data["leakage_rate"] * 0.2
            + self.state_data["energy_cost"] * 0.01
        )

        reward = max(0.0, min(1.0, efficiency - penalty))

        total_supply = action["household_supply"] + action["industrial_supply"]
        self.state_data["reservoir_level"] -= total_supply

        done = self.state_data["reservoir_level"] <= 0

        return self.state(), reward, done, {}
