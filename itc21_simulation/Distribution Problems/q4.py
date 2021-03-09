from scipy.stats import norm

Px = norm(loc=72, scale=15.2).sf(84)
print(f"Percentage of students scoring 84 or more in the exam: {Px:.4f}")

