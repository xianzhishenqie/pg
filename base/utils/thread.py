import sched
import threading
import time


def delay_exe(func, delay_time, args):
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(delay_time, 10, func, args)
    thread = threading.Thread(target=scheduler.run)
    thread.start()

    return thread
