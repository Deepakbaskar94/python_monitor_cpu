import psutil

psutil.cpu_percent(interval=1)

per_cpu = psutil.cpu_percent(percpu=True)
# For individual core usage with blocking, psutil.cpu_percent(interval=1, percpu=True)
for idx, usage in enumerate(per_cpu):
    print(f"CORE_{idx+1}: {usage}%")