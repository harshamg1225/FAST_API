import time

from timeit import default_timer as timer


def run_task(name, sec):

    print(f"{name} started at : {timer()}")
    time.sleep(sec)

    print(f"{name} completed at: {timer()}")


start = timer()

run_task("Task 1", 2)
run_task("Task 2", 1)
run_task("Task 3", 3)

print(f"Total time taken is {timer() - start:.2f}")
