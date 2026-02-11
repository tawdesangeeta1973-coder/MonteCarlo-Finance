
#  MonteCarlo-Finance: GBM Stock Simulation + VaR Analysis

**5,000 path Geometric Brownian Motion simulation** for Nifty50-style stock. Calculates **Value at Risk (VaR)** using stochastic calculus.

##  Objective
Predict stock price distribution after 1 year to compute **95% VaR** – essential for risk management in quantitative finance.

##  The Math
$$S_t = S_0 \exp\left(\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W_t\right)$$

**Parameters** (India market realistic):
- $S_0 = 100$: Starting price
- $\mu = 12\%$: Expected return
- $\sigma = 25\%$: Volatility
- $T = 1$ year, daily steps

##  Quick Run
```bash
pip install numpy matplotlib
python monte_carlo_sim.py
