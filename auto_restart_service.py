import os

service_name = "nginx"
status = os.system(f"systemctl is-active --quiet {service_name}")

if status != 0:
    print(f"⚠️ {service_name} is DOWN! Restarting...")
    os.system(f"sudo systemctl restart {service_name}")
    print(f"✅ {service_name} restarted successfully.")
else:
    print(f"✅ {service_name} is running fine.")
