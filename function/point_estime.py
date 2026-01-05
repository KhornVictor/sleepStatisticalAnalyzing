import math
import descriptive


# measures the accuracy of a sample statistic (like the mean) as an estimate of the true population value
def standard_error(data: list):
    standard_deviation_value = descriptive.standard_deviation(data)
    n = len(data)
    if n == 0: return None
    standard_error_value = standard_deviation_value / math.sqrt(n)
    return standard_error_value

def proportion_standard_error(successes: int, trials: int):
    if trials == 0: return None
    p = successes / trials
    standard_error_value = math.sqrt(p * (1 - p) / trials)
    return standard_error_value
