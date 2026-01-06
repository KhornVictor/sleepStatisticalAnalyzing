import math
import matplotlib.pyplot as plt

def mean(data):
    mean_value = sum(data) / len(data)
    return mean_value


def variance(data):
    mean_value = mean(data)
    variance_value = sum((x - mean_value) ** 2 for x in data) / len(data)
    return variance_value

def standard_deviation(data):
    variance_value = variance(data)
    std_dev_value = math.sqrt(variance_value)
    return std_dev_value

def median(data):
    sorted_values = sorted(data)
    n = len(sorted_values)
    mid = n // 2
    if n % 2 == 0: median_value = (sorted_values[mid - 1] + sorted_values[mid]) / 2
    else: median_value = sorted_values[mid]
    return median_value

def mode(data):
    frequency = {}
    for value in data: frequency[value] = frequency.get(value, 0) + 1
    max_freq = max(frequency.values())
    modes = [key for key, freq in frequency.items() if freq == max_freq]
    if len(modes) == len(frequency): return None
    return modes

def range(data):
    range_value = max(data) - min(data)
    return range_value

# Shows relative variability; useful to compare different datasets
def coefficient_of_variation(data):
    mean_value = mean(data)
    standard_deviation_value = standard_deviation(data)
    if mean_value == 0: return None
    coefficient_of_variation_value = (standard_deviation_value / mean_value) * 100
    return coefficient_of_variation_value


def quartiles(data):
    sorted_values = sorted(data)
    n = len(sorted_values)

    mid = n // 2
    if n % 2 == 0:
        lower_half = sorted_values[:mid]
        upper_half = sorted_values[mid:]
    else:
        lower_half = sorted_values[:mid]
        upper_half = sorted_values[mid + 1:]

    sorted_lower = sorted(lower_half)
    sorted_upper = sorted(upper_half)

    m = len(sorted_lower)
    mid_lower = m // 2
    if m % 2 == 0:
        Q1 = (sorted_lower[mid_lower - 1] + sorted_lower[mid_lower]) / 2
    else:
        Q1 = sorted_lower[mid_lower]
    p = len(sorted_upper)
    mid_upper = p // 2
    if p % 2 == 0:
        Q3 = (sorted_upper[mid_upper - 1] + sorted_upper[mid_upper]) / 2
    else:
        Q3 = sorted_upper[mid_upper]

    return Q1, Q3

def interquartile_range(data):
    Q1, Q3 = quartiles(data)
    IQR = Q3 - Q1
    return IQR

def outliers(data):
    Q1, Q3 = quartiles(data)
    IQR = interquartile_range(data)
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outlier_values = [x for x in data if x < lower_bound or x > upper_bound]
    return outlier_values

# Shows how many standard deviations a value is from the mean
def z_scores(data):
    mean_value = mean(data)
    standard_deviation_value = standard_deviation(data)
    if standard_deviation_value == 0:
        return [0 for _ in data]
    z_scores_values = [(x - mean_value) / standard_deviation_value for x in data]
    return z_scores_values

# Position of the Pth percentile
def percentile(data, p):
    if not 0 <= p <= 100: raise ValueError("Percentile must be between 0 and 100")
    sorted_data = sorted(data)
    k = (len(sorted_data) - 1) * (p / 100)
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return sorted_data[int(k)]
    d0 = sorted_data[int(f)] * (c - k)
    d1 = sorted_data[int(c)] * (k - f)
    return d0 + d1

# Positive = right-skewed, Negative = left-skewed
def skewness(data):
    n = len(data)
    if n < 3: return 0
    mean_value = mean(data)
    standard_deviation_value = standard_deviation(data)
    if standard_deviation_value == 0: return 0
    skewness_value = (n * sum((x - mean_value) ** 3 for x in data)) / ((n - 1) * (n - 2) * (standard_deviation_value ** 3))
    return skewness_value

def skewness_interpretation(skewness_value):
    if skewness_value > 1: return "Highly positively skewed"
    elif 0.5 < skewness_value <= 1: return "Moderately positively skewed"
    elif -0.5 <= skewness_value <= 0.5: return "Approximately symmetric"
    elif -1 <= skewness_value < -0.5: return "Moderately negatively skewed"
    else: return "Highly negatively skewed"

# Measures “peakedness” of the distribution
def kurtosis(data):
    n = len(data)
    if n < 4: return 0
    mean_value = mean(data)
    standard_deviation_value = standard_deviation(data)
    if standard_deviation_value == 0: return 0
    kurtosis_value = (n * (n + 1) * sum((x - mean_value) ** 4 for x in data)) / ((n - 1) * (n - 2) * (n - 3) * (standard_deviation_value ** 4)) - (3 * (n - 1) ** 2) / ((n - 2) * (n - 3))
    return kurtosis_value

def kurtosis_interpretation(kurtosis_value):
    if kurtosis_value > 3: return "Leptokurtic (more peaked than normal)"
    elif kurtosis_value == 3: return "Mesokurtic (normal peakedness)"
    else: return "Platykurtic (less peaked than normal)"

# Measures asymmetry of the probability distribution
def coefficient_of_skewness(data):
    mean_value = mean(data)
    median_value = median(data)
    standard_deviation_value = standard_deviation(data)
    if standard_deviation_value == 0: return 0
    coeffient_of_skewness_value = 3 * (mean_value - median_value) / standard_deviation_value
    return coeffient_of_skewness_value

def coefficient_of_skewness_interpretation(coeffient_of_skewness_value):
    if coeffient_of_skewness_value > 0: return "Positively skewed"
    elif coeffient_of_skewness_value < 0: return "Negatively skewed"
    else: return "Symmetric"

def frequency_distribution(data, class_intervals):
    frequencies = []
    for interval in class_intervals:
        lower, upper = map(float, interval.split('-'))
        freq = sum(1 for x in data if lower <= x < upper)
        frequencies.append(freq)
    return frequencies

def class_interval(frequency_distribution):
    class_intervals = []
    for interval in frequency_distribution:
        lower, upper = map(float, interval.split('-'))
        class_intervals.append((lower, upper))
    return class_intervals

def group_data_mean(class_intervals, frequencies):
    total_frequency = sum(frequencies)
    midpoints = [(interval[0] + interval[1]) / 2 for interval in class_intervals]
    weighted_sum = sum(midpoint * freq for midpoint, freq in zip(midpoints, frequencies))
    mean_value = weighted_sum / total_frequency
    return mean_value