from scipy.stats import poisson

print(f"a) Probability of having 16 or less cars crossing the bridge in a particular minute: {poisson.cdf(16, 12):.4f}")
print(f"b) Probability of having 17 or more cars crossing the bridge in a particular minute: {poisson.sf(16, 12):.4f}")