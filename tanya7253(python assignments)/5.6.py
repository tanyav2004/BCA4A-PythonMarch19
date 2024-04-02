import statistics

# Given list of numbers
numbers = [10, 20, 30, 40, 50]

# Calculate mean
mean = statistics.mean(numbers)

# Calculate variance
variance = statistics.variance(numbers)

# Calculate standard deviation
std_deviation = statistics.stdev(numbers)

# Display results
print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std_deviation)
