# sudo `which python` process_finder.py
import psutil


for pid in psutil.pids():
    p = psutil.Process(pid)
    try:
        executable = p.exe()
    except psutil.AccessDenied as ex:
        print(f"Access Denied for pid {pid}")
        continue
    if 'python' in executable:
      print(f"{pid:10}    {p.cwd()}")

