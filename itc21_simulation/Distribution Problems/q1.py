from scipy.stats import binom

xB = binom(n=5, p=0.25)
Px = xB.pmf(0)
print(f"Probability of randomly guessing 0 out of 5 questions correct: {Px:.4f}")