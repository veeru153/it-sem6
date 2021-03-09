from scipy.stats import norm

xN = norm(loc=6, scale=4)
Px = xN.cdf(3) - xN.cdf(-1)
print(f"Probability that Z takes on a value between -1 and 3: {Px:.4f}")