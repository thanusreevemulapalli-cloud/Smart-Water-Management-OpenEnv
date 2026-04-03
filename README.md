# 💧 Smart Water Management OpenEnv

> A real-world reinforcement learning environment for optimizing water distribution under scarcity, cost, and leakage constraints.

---

## 🌍 Problem Statement
Water scarcity and inefficient distribution are critical urban challenges. Cities must balance:
- Household vs Industrial demand
- Limited reservoir supply
- Energy costs for pumping
- Water loss due to leakage

🎯 **Goal:** Learn a policy that allocates water efficiently while minimizing cost and wastage.

---

## 🧠 Environment Overview
This environment follows a standard RL interface:

- `reset()` → initializes the system
- `step(action)` → applies allocation decision
- `state()` → returns current system state

---

## 📦 Observation Space
```json
{
  "reservoir_level": "float (0–1000)",
  "household_demand": "float",
  "industrial_demand": "float",
  "energy_cost": "float",
  "leakage_rate": "float (0–0.3)"
}
