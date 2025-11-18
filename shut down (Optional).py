import os
import time

# Time in seconds (5 hours = 5 * 60 * 60 = 18000 seconds)
shutdown_time = 5 * 60 * 60  

print(f"Computer will shut down in {shutdown_time/3600} hours...")

# Wait for 5 hours
time.sleep(shutdown_time)

# Shutdown command
# For Windows
os.system("shutdown /s /t 1")

# For Linux / MacOS (uncomment if using these systems)
# os.system("shutdown now")
