from scipy.stats import norm
from math import sqrt

n = 9
z0 = norm.interval(0.95, loc=0, scale=1)
mean = 90
std = 36
cIntNeg = mean + z0[0] * (std / sqrt(n))
cIntPos = mean + z0[1] * (std / sqrt(n))
print(f"95% confidence interval around the mean for the expected value of Z: ({cIntNeg:.4f},{cIntPos:.4f})")
print(z0)


