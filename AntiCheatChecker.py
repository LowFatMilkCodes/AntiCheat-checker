from struct import pack
import psutil
print("LowFatCodes Anticheat Checker")
def is_process_running(process_name):
    """Check if a process with the given name is running."""
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            return True
    return False

# Main program
#vanguard
if is_process_running('vgc.exe'):
    print("Vanguard is running")
else:
    print("Vanguard Is Not Running")
if is_process_running('be.exe'):
    print("Battle Eye is running")
else:
    print("Battle Eye Is Not Running")


if is_process_running('EasyAntiCheat.exe'):
    print("EAC is running")
else:
    print("EAC Is Not Running")

    #Ricochet
if is_process_running('Ricochet.exe'):
    print("Ricochet is running")
else:
    print("Ricochet Is Not Running")

print("Thanks For using :) ")
