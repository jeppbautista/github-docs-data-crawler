  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Copilot Chat Cookbook](https://docs.github.com/en/copilot/copilot-chat-cookbook "Copilot Chat Cookbook")/
  * [Refactoring code](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code "Refactoring code")/
  * [Performance optimization](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/refactoring-for-performance-optimization "Performance optimization")


# Refactoring for performance optimization
Copilot Chat can suggest ways to speed up slow-running code.
## In this article
  * [Example scenario](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/refactoring-for-performance-optimization#example-scenario)
  * [Example prompt](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/refactoring-for-performance-optimization#example-prompt)
  * [Example response](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/refactoring-for-performance-optimization#example-response)
  * [Further reading](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/refactoring-for-performance-optimization#further-reading)


Existing code may function correctly but be inefficient, leading to performance bottlenecks. Examples of coding that can adversely impact performance include inefficient loops, unnecessary computations, and excessive memory allocation.
Copilot Chat can identify performance hotspots and suggest refactoring strategies such as optimizing data structures (for example, using hashmaps instead of arrays), reducing redundant calculations, and improving algorithmic efficiency. It can also recommend caching mechanisms or parallelizing operations to improve performance.
## [Example scenario](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/refactoring-for-performance-optimization#example-scenario)
The following Python code prints every 1000th prime number up to the 10,000th prime. It includes a timer, and prints how long the code takes to run as the last line of the output. The program takes several seconds to complete.
```
import time

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def every_1000th_prime():
    primes = []
    num = 2
    while len(primes) < 10000:
        if is_prime(num):
            primes.append(num)
        num += 1
    return [primes[i] for i in range(999, 10000, 1000)]

if __name__ == "__main__":
    start_time = time.time()
    primes = every_1000th_prime()
    for prime in primes:
        print(prime)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time:.10f} seconds")

```

## [Example prompt](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/refactoring-for-performance-optimization#example-prompt)
`Optimize this code for performance`
## [Example response](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/refactoring-for-performance-optimization#example-response)
Copilot suggests using a sieve function to generate the prime numbers much more efficiently. If you run this program it will complete in a fraction of a second.
Copilot Chat responses are non-deterministic, so you may get a different response from the one shown here.
```
import time

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, limit + 1, start):
                sieve[multiple] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]

def every_1000th_prime():
    limit = 105000  # Higher than needed to ensure 10,000 primes
    primes = sieve_of_eratosthenes(limit)
    return [primes[i] for i in range(999, 10000, 1000)]

if __name__ == "__main__":
    start_time = time.time()
    primes = every_1000th_prime()
    for prime in primes:
        print(prime)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time:.10f} seconds")

```

## [Further reading](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/refactoring-for-performance-optimization#further-reading)
  * [Prompt engineering for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)
  * [Best practices for using GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)


