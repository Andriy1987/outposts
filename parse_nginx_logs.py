import re
import csv
import subprocess
from datetime import datetime

log_file = "/home/andriy/devops/nginx.log"  
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"parsed_logs_{timestamp}.csv"

log_pattern = re.compile(r'(?P<ip>[\d\.]+) - - \[(?P<timestamp>[^\]]+)\] \"(?P<method>[A-Z]+) (?P<url>[^ ]+) HTTP/[^\"]+\" (?P<status>\d+) (?P<bytes>\d+) \"(?P<referrer>[^\"]*)\" \"(?P<user_agent>[^\"]*)\"')

parsed_logs = []
with open(log_file, "r") as file:
    for line in file:
        match = log_pattern.search(line)
        if match:
            parsed_logs.append(match.groupdict())

with open(output_file, "w", newline="") as csv_file:
    fieldnames = ["ip", "timestamp", "method", "url", "status", "bytes", "referrer", "user_agent"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(parsed_logs)

print(f"Parsed logs have been saved to {output_file}")

try:
    subprocess.run(["git", "add", output_file], check=True)
    subprocess.run(["git", "commit", "-m", "Add parsed Nginx logs"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("CSV file has been pushed to Git.")
except subprocess.CalledProcessError as e:
    print(f"Error while pushing to Git: {e}")

