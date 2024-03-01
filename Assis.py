def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_fibonacci_sequence(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_num = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_num)
    return fibonacci_sequence

n = int(input("Enter the number of Fibonacci numbers to generate: "))
fibonacci_sequence = generate_fibonacci_sequence(n)
print("Fibonacci Sequence:")
prime_numbers = []
prime_sum = 0
for num in fibonacci_sequence:
    print(num, end=" ")
    if is_prime(num):
        print("(Prime)")
        prime_numbers.append(num)
        prime_sum += num
    else:
        print("(Not Prime)")

if prime_numbers:
    max_prime = max(prime_numbers)
    min_prime = min(prime_numbers)
    average_prime = prime_sum / len(prime_numbers)
    print("Maximum Prime Number:", max_prime)
    print("Minimum Prime Number:", min_prime)
    print("Average of Prime Numbers:", average_prime)
else:
    print("No prime numbers found in the Fibonacci sequence.")
