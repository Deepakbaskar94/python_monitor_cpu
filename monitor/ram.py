import psutil

mem_usage = psutil.virtual_memory()

print(f"Free: {mem_usage.percent}%")
print(f"Total: {mem_usage.total/(1024**3):.2f}G")
print(f"Used: {mem_usage.used/(1024**3):.2f}G")