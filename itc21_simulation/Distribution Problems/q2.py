from scipy.stats import binom

xB = binom(n=12, p=0.2)
Px = xB.cdf(4)
print(f"Probability of having four or less correct answers: {Px:.4f}")