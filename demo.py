import asyncio
from prime import is_prime, print_matches, repetitive_message, fib, search, lucas


# g = async_search(lucas(), lambda x: len(str(x)) >= 6)


scheduler = asyncio.get_event_loop()
a = print_matches(lucas(), is_prime)
b = repetitive_message('This is a rep message', 1)
scheduler.create_task(a)
scheduler.create_task(b)
scheduler.run_forever()
