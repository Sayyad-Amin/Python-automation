import shutil
import psutil

# Set thresholds
DISK_THRESHOLD = 80  # 80% full
MEMORY_THRESHOLD = 80  # 80% usage

# Check disk usage
total, used, free = shutil.disk_usage("/")
disk_usage_percent = (used / total) * 100

if disk_usage_percent > DISK_THRESHOLD:
    print(f"⚠️ Warning: Disk usage is {disk_usage_percent:.2f}%!")
else:
    print(f"✅ Disk usage is normal: {disk_usage_percent:.2f}%")

# Check memory usage
memory_info = psutil.virtual_memory()
memory_usage_percent = memory_info.percent

if memory_usage_percent > MEMORY_THRESHOLD:
    print(f"⚠️ Warning: Memory usage is {memory_usage_percent:.2f}%!")
else:
    print(f"✅ Memory usage is normal: {memory_usage_percent:.2f}%")
