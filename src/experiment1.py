# Imported psutil library for monitoring

import psutil


# Loop to check if process is running

def running_process(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            return True
    return False

# Return True if the process is running, False otherwise

result = running_process("firefox.exe")
print(result)