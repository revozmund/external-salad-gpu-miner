import os
import psutil
import subprocess

TREX_PATH = r''
SALAD_GPU_PATH = r''

def is_process_running(process_name):
    return any(process.info['name'].lower() == process_name.lower() for process in psutil.process_iter(['pid', 'name']))

def start_mining():
    try:
        subprocess.Popen([TREX_PATH])
        print("Miner started.")
        
        subprocess.Popen([SALAD_GPU_PATH], shell=True)
        print("salad.bat started.")
    except Exception as e:
        print("Failed to start miner or salad.bat:", e)

def main():
    miner_running = is_process_running("t-rex.exe")
    vmwp_running = is_process_running("vmwp.exe")
    vmmemwsl_running = is_process_running("vmmemWSL")

    if not miner_running:  # If miner isn't running
        start_mining()
    else:
        print("Miner is already running.")

    if vmwp_running:  # If vmwp.exe is running
        print("vmwp.exe is running.")

    if vmmemwsl_running:  # If vmmemWSL is running
        print("vmmemWSL is running.")

if __name__ == "__main__":
    main()
