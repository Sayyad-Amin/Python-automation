import shutil

# Set threshold (80% full)
THRESHOLD = 80

total, used, free = shutil.disk_usage("/")
usage_percent = (used / total) * 100

if usage_percent > THRESHOLD:
    print(f"⚠️ Warning: Disk usage is {usage_percent:.2f}%!")
else:
    print(f"✅ Disk usage is normal: {usage_percent:.2f}%")
