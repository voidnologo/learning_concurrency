from prime import async_is_prime, async_print_matches, async_repetitive_message, fib, async_search, lucas
from concurrency import Scheduler


s = Scheduler()
a = async_print_matches(lucas(), async_is_prime)
b = async_repetitive_message('This is a rep message', 1)
s.add(a)
s.add(b)
s.run_to_completion()
