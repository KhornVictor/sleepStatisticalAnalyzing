
from scipy import stats
import descriptive
import math

def margin_of_error(data, confidence_level):
    alpha = 1 - confidence_level
    z_score = stats.norm.ppf(1 - alpha / 2)
    margin_of_error = z_score * (descriptive.standard_deviation(data) / math.sqrt(len(data)))
    return margin_of_error  

def proportion_confidence_interval(successes: int, trials: int, confidence_level: float):
    if trials == 0:
        return [None, None]
    p_hat = successes / trials
    alpha = 1 - confidence_level
    z_score = stats.norm.ppf(1 - alpha / 2)
    moe = z_score * math.sqrt((p_hat * (1 - p_hat)) / trials)
    lower_bound = max(0, p_hat - moe)
    upper_bound = min(1, p_hat + moe)
    return [lower_bound, upper_bound]

def mean_confidence_interval(data, confidence_level: float):
    mean_value = descriptive.mean(data)
    moe = margin_of_error(data, confidence_level=confidence_level)
    lower_bound = mean_value - moe
    upper_bound = mean_value + moe
    return [lower_bound, upper_bound]

def variance_confidence_interval(data, confidence_level: float):
    n = len(data)
    if n < 2:
        return [None, None]
    variance_value = descriptive.variance(data)
    alpha = 1 - confidence_level
    chi2_lower = stats.chi2.ppf(alpha / 2, df=n - 1)
    chi2_upper = stats.chi2.ppf(1 - alpha / 2, df=n - 1)
    lower_bound = (n - 1) * variance_value / chi2_upper
    upper_bound = (n - 1) * variance_value / chi2_lower
    return [lower_bound, upper_bound]

def standard_deviation_confidence_interval(data, confidence_level: float):
    variance_ci = variance_confidence_interval(data, confidence_level=confidence_level)
    if variance_ci[0] is None or variance_ci[1] is None:
        return [None, None]
    lower_bound = math.sqrt(variance_ci[0])
    upper_bound = math.sqrt(variance_ci[1])
    return [lower_bound, upper_bound]

def proportion_confidence_interval_alternative(successes: int, trials: int, confidence_level: float):
    if trials == 0:
        return [None, None]
    p_hat = successes / trials
    alpha = 1 - confidence_level
    z_score = stats.norm.ppf(1 - alpha / 2)
    denominator = 1 + (z_score ** 2) / trials
    center_adjusted_probability = p_hat + (z_score ** 2) / (2 * trials)
    adjusted_standard_deviation = math.sqrt((p_hat * (1 - p_hat) + (z_score ** 2) / (4 * trials)) / trials)
    lower_bound = (center_adjusted_probability - z_score * adjusted_standard_deviation) / denominator
    upper_bound = (center_adjusted_probability + z_score * adjusted_standard_deviation) / denominator
    lower_bound = max(0, lower_bound)
    upper_bound = min(1, upper_bound)
    return [lower_bound, upper_bound]

def mean_confidence_interval_t(data, confidence_level: float):
    n = len(data)
    if n < 2:
        return [None, None]
    mean_value = descriptive.mean(data)
    standard_error_value = descriptive.standard_deviation(data) / math.sqrt(n)
    alpha = 1 - confidence_level
    t_score = stats.t.ppf(1 - alpha / 2, df=n - 1)
    moe = t_score * standard_error_value
    lower_bound = mean_value - moe
    upper_bound = mean_value + moe
    return [lower_bound, upper_bound]

def variance_confidence_interval_chi2(data, confidence_level: float):
    n = len(data)
    if n < 2:
        return [None, None]
    variance_value = descriptive.variance(data)
    alpha = 1 - confidence_level
    chi2_lower = stats.chi2.ppf(alpha / 2, df=n - 1)
    chi2_upper = stats.chi2.ppf(1 - alpha / 2, df=n - 1)
    lower_bound = (n - 1) * variance_value / chi2_upper
    upper_bound = (n - 1) * variance_value / chi2_lower
    return [lower_bound, upper_bound]

def standard_deviation_confidence_interval_chi2(data, confidence_level: float):
    variance_ci = variance_confidence_interval_chi2(data, confidence_level=confidence_level)
    if variance_ci[0] is None or variance_ci[1] is None:
        return [None, None]
    lower_bound = math.sqrt(variance_ci[0])
    upper_bound = math.sqrt(variance_ci[1])
    return [lower_bound, upper_bound]

def paired_mean_confidence_interval(sample1: list, sample2: list, confidence_level: float):
    if len(sample1) != len(sample2) or len(sample1) < 2: return [None, None]
    differences = [a - b for a, b in zip(sample1, sample2)]
    return mean_confidence_interval_t(differences, confidence_level=confidence_level)

def paired_proportion_confidence_interval(successes1: int, trials1: int, successes2: int, trials2: int, confidence_level: float):
    if trials1 == 0 or trials2 == 0: return [None, None]
    p1 = successes1 / trials1
    p2 = successes2 / trials2
    diff = p1 - p2
    alpha = 1 - confidence_level
    z_score = stats.norm.ppf(1 - alpha / 2)
    se1 = math.sqrt((p1 * (1 - p1)) / trials1)
    se2 = math.sqrt((p2 * (1 - p2)) / trials2)
    se_diff = math.sqrt(se1 ** 2 + se2 ** 2)
    moe = z_score * se_diff
    lower_bound = diff - moe
    upper_bound = diff + moe
    return [lower_bound, upper_bound]

def paired_variance_confidence_interval(sample1: list, sample2: list, confidence_level: float):
    if len(sample1) != len(sample2) or len(sample1) < 2: return [None, None]
    differences = [a - b for a, b in zip(sample1, sample2)]
    return variance_confidence_interval_chi2(differences, confidence_level=confidence_level)

def paired_standard_deviation_confidence_interval(sample1: list, sample2: list, confidence_level: float):
    variance_ci = paired_variance_confidence_interval(sample1, sample2, confidence_level=confidence_level)
    if variance_ci[0] is None or variance_ci[1] is None: return [None, None]
    lower_bound = math.sqrt(variance_ci[0])
    upper_bound = math.sqrt(variance_ci[1])
    return [lower_bound, upper_bound]

def proportion_confidence_interval_wilson(successes: int, trials: int, confidence_level: float):
    if trials == 0: return [None, None]
    p_hat = successes / trials
    alpha = 1 - confidence_level
    z_score = stats.norm.ppf(1 - alpha / 2)
    denominator = 1 + (z_score ** 2) / trials
    center_adjusted_probability = p_hat + (z_score ** 2) / (2 * trials)
    adjusted_standard_deviation = math.sqrt((p_hat * (1 - p_hat) + (z_score ** 2) / (4 * trials)) / trials)
    lower_bound = (center_adjusted_probability - z_score * adjusted_standard_deviation) / denominator
    upper_bound = (center_adjusted_probability + z_score * adjusted_standard_deviation) / denominator
    lower_bound = max(0, lower_bound)
    upper_bound = min(1, upper_bound)
    return [lower_bound, upper_bound]