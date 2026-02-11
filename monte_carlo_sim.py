import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Pro Parameters (Nifty realistic)
S0 = 100      # Starting price ₹100
mu = 0.12     # 12% annual return
sigma = 0.25  # 25% volatility
T = 1.0       # 1 year
dt = 1/252    # Daily
steps = int(T/dt)
n_sims = 5000 # 5K paths

print(" Running 5,000 GBM Simulations...")

# Store ALL paths for VaR
all_paths = []
final_prices = np.zeros(n_sims)

for i in range(n_sims):
    shocks = np.random.normal(0, np.sqrt(dt), steps)
    path = S0 * np.exp(np.cumsum((mu - 0.5 * sigma**2) * dt + sigma * shocks))
    all_paths.append(path)
    final_prices[i] = path[-1]

#  Calculate KEY METRICS
var_95 = np.percentile(final_prices, 5)
mean_final = np.mean(final_prices)
prob_profit = np.mean(final_prices > S0) * 100

print("\n RESULTS:")
print(f"Initial Price:     ₹{S0}")
print(f"Mean Final Price:  ₹{mean_final:.1f}")
print(f"95% VaR Floor:     ₹{var_95:.1f}")
print(f"VaR Loss:          ₹{S0 - var_95:.1f}")
print(f"Profit Probability: {prob_profit:.1f}%")

#  Plot: Histogram of Final Prices
plt.figure(figsize=(12, 6))
plt.hist(final_prices, bins=75, density=True, alpha=0.7, color='#1f77b4', edgecolor='white')
plt.axvline(var_95, color='red', lw=3, linestyle='--', 
            label=f'VaR 95%: ₹{var_95:.1f}')
plt.axvline(mean_final, color='green', lw=2, linestyle='-', 
            label=f'Mean: ₹{mean_final:.1f}')
plt.axvline(S0, color='orange', lw=2, linestyle='-', label='Start: ₹100')
plt.title('Monte Carlo GBM: 5K Stock Paths - Price Distribution & 95% VaR', fontsize=16)
plt.xlabel('Final Stock Price (₹)', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)

#  SAVE HIGH-RES IMAGE
plt.tight_layout()
plt.savefig('simulation_results.png', dpi=300, bbox_inches='tight')
print("\n Plot saved: simulation_results.png")
plt.show()

