import matplotlib.pyplot as plt

# Data Setup
tasks = [
    "Project Setup",
    "Data Models",
    "TDD Red Phase",
    "TDD Green Phase",
    "Refactoring",
    "Mock API Tests",
    "Integration Tests",
    "Docker Setup",
    "CI/CD Pipeline",
]
start_days = [1, 2, 4, 6, 9, 11, 13, 15, 17]
durations = [1, 2, 2, 3, 2, 2, 2, 2, 2]

# Plotting Gantt Chart
fig, ax = plt.subplots(figsize=(10, 5))

for i, task in enumerate(tasks):
    ax.barh(task, durations[i], left=start_days[i], color="#2b5c8f")

ax.set_xlabel("Days")
ax.set_title("Python Project Development Gantt Chart")
ax.grid(axis="x", linestyle="--", alpha=0.7)
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()