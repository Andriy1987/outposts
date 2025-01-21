# Nginx Log Parser

This project is a Python script for parsing and managing Nginx logs. It reads a log file, extracts relevant data using regex, and saves the parsed data into a CSV file. The script also supports filtering and sorting logs by specific fields. Additionally, it integrates with Git to commit and push the resulting CSV file to a repository.

## Features
- **Parse Nginx logs**: Extract fields like IP address, timestamp, method, URL, status, bytes, referrer, and user agent.
- **Filter logs**: Use specific criteria to filter log entries (e.g., `status=404`).
- **Sort logs**: Sort log entries by fields such as `ip`, `timestamp`, or `status`.
- **Git integration**: Automatically commit and push the resulting CSV file to a Git repository.

## Prerequisites
- Docker installed on your system.
- Access to a Git repository.

## Files
- `parse_nginx_logs_new.py`: The main Python script for parsing logs.
- `Dockerfile`: Builds a Docker image for running the script.
- `nginx.log`: Example Nginx log file (replace with your actual log file).

## Docker Setup
### Build the Docker Image
To build the Docker image, run the following command in the directory containing the `Dockerfile`:

```bash
sudo docker build -t nginx-log-parser .
```

### Running the Container
#### Basic Usage
To parse the logs and save the output:

```bash
sudo docker run -v /path/to/your/logs:/log nginx-log-parser
```

#### Filtering Logs
To filter logs by a specific field, use the `--filter` argument:

```bash
sudo docker run -v /path/to/your/logs:/log nginx-log-parser --filter status=404
```

#### Sorting Logs
To sort logs by a specific field, use the `--sort` argument:

```bash
sudo docker run -v /path/to/your/logs:/log nginx-log-parser --sort ip
```

#### Viewing Help
To view the help message:

```bash
sudo docker run nginx-log-parser --help
```

### Git Integration
The script commits and pushes the resulting CSV file to a Git repository. Ensure the following:

1. Your Git repository is mounted as a volume (e.g., `-v /path/to/repo:/log`).
2. Set the `GITHUB_TOKEN` environment variable with your GitHub personal access token:

   ```bash
   sudo docker run -e GITHUB_TOKEN=<your_token> -v /path/to/repo:/log nginx-log-parser
   ```

## Example Outputs
- **Filtered Logs**: Logs filtered by `status=404` will be saved in a CSV file named like `parsed_logs_<timestamp>.csv`.
- **Sorted Logs**: Logs sorted by `ip` will also be saved in a similarly named CSV file.

## Notes
- Replace `/path/to/your/logs` with the actual path to your log file directory.
- Replace `<your_token>` with your GitHub personal access token.
- Ensure that the `nginx.log` file exists in the specified directory.

## License
This project is licensed under the MIT License.

