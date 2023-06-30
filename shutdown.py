import os
from datetime import timedelta, datetime

timer = int(input('How long until shutdown (in hours)? '))

timer_delta = timedelta(hours=timer)
timer_seconds = timer_delta.total_seconds()

os.system(f"shutdown -s -t {int(timer_seconds)}")