import numpy as np
import matplotlib.pyplot as plt

# Parameters
S0 = 100      # Initial stock price
mu = 0.05     # Expected annual return (5%)
sigma = 0.2   # Annual volatility (20%)
T = 1.0       # Time period (1 year)
dt = 1/252    # Time step (daily, 252 trading days)
N = int(T/dt) # Number of time steps
n_sims = 100  # Number of simulated paths

# Simulation
plt.figure(figsize=(10,6))

for i in range(n_sims):
    # Generate random shocks
    shocks = np.random.normal(0, np.sqrt(dt), N)
    # Calculate price path using the GBM formula
    price_path = S0 * np.exp(np.cumsum((mu - 0.5 * sigma**2) * dt + sigma * shocks))
    plt.plot(price_path, linewidth=0.8, alpha=0.6)

plt.title(f"Monte Carlo Simulation: {n_sims} Possible Price Paths")
plt.xlabel("Days")
plt.ylabel("Price ($)")
plt.grid(True)
plt.show()
