import scipy.stats as stats
import numpy as np

# Data for the drug group
mean_drug = 10  # Example mean reduction in mmHg
std_dev_drug = 5  # Example standard deviation in mmHg
n_drug = 25  # Sample size

# Data for the placebo group
mean_placebo = 4  # Example mean reduction in mmHg
std_dev_placebo = 3  # Example standard deviation in mmHg
n_placebo = 25  # Sample size

# Calculate the standard errors
se_drug = std_dev_drug / np.sqrt(n_drug)
se_placebo = std_dev_placebo / np.sqrt(n_placebo)

# Confidence level
confidence = 0.95
z_score = stats.norm.ppf((1 + confidence) / 2)

# Calculate the confidence intervals
ci_drug = (mean_drug - z_score * se_drug, mean_drug + z_score * se_drug)
ci_placebo = (mean_placebo - z_score * se_placebo, mean_placebo + z_score * se_placebo)

print(f"95% Confidence Interval for the drug group: {ci_drug}")
print(f"95% Confidence Interval for the placebo group: {ci_placebo}")
