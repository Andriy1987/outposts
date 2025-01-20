import re
import csv
import subprocess

log_file_path = "/home/andriy/devops/nginx.log"  
csv_file_path = "parsed_logs.csv"

log_pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<timestamp>[^\]]+)\] '
    r'"(?P<method>\w+) (?P<url>[^ ]+) HTTP/[^"]+" (?P<status>\d+) (?P<bytes>\d+) '
    r'"(?P<referrer>[^"]*)" "(?P<user_agent>[^"]*)"'
)

parsed_data = []
with open(log_file_path, "r") as log_file:
    for line in log_file:
        match = log_pattern.search(line)
        if match:
            parsed_data.append(match.groupdict())

with open(csv_file_path, "w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=parsed_data[0].keys())
    writer.writeheader()
    writer.writerows(parsed_data)

print(f"Logs have been parsed and saved to {csv_file_path}")

try:
    subprocess.run(["git", "add", csv_file_path], check=True)
    subprocess.run(["git", "commit", "-m", "Add parsed Nginx logs"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("CSV file has been pushed to Git.")
except subprocess.CalledProcessError as e:
    print(f"Error while pushing to Git: {e}")

