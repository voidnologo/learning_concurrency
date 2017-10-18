#!/usr/bin/env python

from code import fib, search, async_search

# ...Example 1...
# Synconous search

# print(search(fib(), lambda x: len(str(x)) >= 6))


# ...Example 2...
# Make search async

# g = async_search(fib(), lambda x: x >= 10)
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print("hello world")
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# ...Example 3...
# Using a task scheduler

from code import Scheduler

# scheduler = Scheduler()
# scheduler.add(async_search(fib(), lambda x: len(str(x)) >= 6))
# scheduler.run_to_completion()


scheduler = Scheduler()
scheduler.add(async_search(fib(), lambda x: len(str(x)) >= 3))
scheduler.add(async_search(fib(), lambda x: len(str(x)) >= 6))
scheduler.run_to_completion()
print(scheduler.completed_task_results[0])
print(scheduler.completed_task_results[1])
