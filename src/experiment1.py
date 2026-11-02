# Imported psutil library for monitoring

import psutil

def running_process(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            return True
    return False

# Check if process is detected

result = running_process("firefox.exe")
print(result)