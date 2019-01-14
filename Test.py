import random
total_sleep_time = 0
for _ in range(20):
    sleep_for = random.uniform(0.05, 1.0)
    print(sleep_for)
    total_sleep_time += sleep_for
    # print(total_sleep_time)
        # queue.put_nowait(sleep_for)