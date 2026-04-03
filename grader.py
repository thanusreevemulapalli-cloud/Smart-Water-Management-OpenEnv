from smart_water_env import SmartWaterEnv


def evaluate(task):
    env = SmartWaterEnv(task=task)
    total = 0

    for _ in range(50):
        state = env.reset()
        action = {
            "household_supply": state["household_demand"],
            "industrial_supply": state["industrial_demand"] * 0.8
        }
        _, reward, _, _ = env.step(action)
        total += reward

    return total / 50


print("Easy:", evaluate("easy"))
print("Medium:", evaluate("medium"))
print("Hard:", evaluate("hard"))
