import time

wait_time = 1
max_retries = 5
attempt = 0
while attempt < max_retries:
    time.sleep(wait_time)
    print("attempt", attempt+1," - wait time",wait_time)
    wait_time*=2
    attempt+=1