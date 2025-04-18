# IP Intel

A simple and efficient Python script to gather detailed information about one or multiple IP addresses using the [ipinfo.io](https://ipinfo.io/) API. It supports both manual input and file-based bulk lookup and displays the results in a clean table as well as saving them in a structured JSON file.

## Features

- 🔍 Fetches data such as hostname, location, country, ASN, and more for each IP.
- 📂 Supports both manual entry and loading IPs from a file.
- 📊 Displays results in a neatly formatted table using `PrettyTable`.
- 💾 Saves output as a JSON report inside a `results/` folder.
- ✅ Handles duplicate IPs and counts their occurrences.

## Dependencies

Before running the script, make sure you have the following packages installed:

```bash
pip install requests prettytable
```

## Usage

#### 1. Run the Script

```bash
python ip_lookup.py
```

#### 2. Choose Input Method

- **Option 1: Manual Entry**
  - You will be prompted to enter IP addresses separated by commas (`,`). Example: `8.8.8.8, 1.1.1.1`

- **Option 2: File Input**
  - Provide the full path to a file containing one IP address per line

## Terminal Table Includes

A table displaying the following fields for each IP:

- IP Address  
- Hostname  
- Country  
- Region  
- City  
- Postal Code  
- Latitude  
- Longitude  
- ASN (Autonomous System Number)  
- Count (number of times the IP appeared)

```
📌 IP Lookup Tool
1. Enter IP(s) manually
2. Load IPs from file
Select an option (1/2): 1
Enter IPs (comma-separated): 8.8.8.8,1.1.1.1

📊 IP Information:
+-------------+-------------------+---------+------------------+---------------+--------------+----------+-----------+------------------------------+-------+
| IP Address  |     Hostname      | Country |     Region       |     City      | Postal Code  | Latitude | Longitude |             ASN              | Count |
+-------------+-------------------+---------+------------------+---------------+--------------+----------+-----------+------------------------------+-------+
| 8.8.8.8     | dns.google        | US      | California       | Mountain View | 94043        | 37.386   | -122.084  | AS15169 Google LLC           | 1     |
| 1.1.1.1     | one.one.one.one   | AU      | New South Wales  | Sydney        | 2000         | -33.8591 | 151.2002  | AS13335 Cloudflare, Inc.     | 1     |
+-------------+-------------------+---------+------------------+---------------+--------------+----------+-----------+------------------------------+-------+

💾 Saved JSON output to: results/report_4872.json
```

## 🧾 JSON File

A JSON report is saved under the `results/` directory. The filename is randomly generated, e.g., `report_4872.json`.

## Optional: API Token

To use a personal token from [ipinfo.io](https://ipinfo.io/account/token), set it at the top of the script:

```python
IPINFO_TOKEN = 'your_token_here'
```

This may increase your request limits and provide more detailed data.

## Notes

- If an IP lookup fails, default placeholder values (`"N/A"`) will be used for missing fields.
- Timeout for API requests is set to 5 seconds per IP.
- Randomized filenames ensure saved reports do not overwrite existing ones.

## License

```
MIT License

Copyright (c) 2025 cx48

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
