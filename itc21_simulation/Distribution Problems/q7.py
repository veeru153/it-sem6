from scipy.stats import norm

Px = norm(loc=69, scale=2.8).cdf(75)
print(f"Probability that Z takes on a value between -1 and 3: {Px:.4f}")