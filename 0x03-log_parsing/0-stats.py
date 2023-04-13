# #!/usr/bin/python3
""" Parses Logs """
import sys
import signal

# Define the allowed status codes
ALLOWED_STATUS_CODES = {200, 301, 400, 401, 403, 404, 405, 500}

# Define the variables to store the metrics
total_file_size = 0
status_code_counts = {}

# Define a signal handler to catch CTRL+C


def signal_handler(signal, frame):
    print_statistics()
    sys.exit(0)


# Register the signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

# Function to print the statistics


def print_statistics():
    print("Total file size:", total_file_size)
    for status_code in sorted(status_code_counts.keys()):
        print(f"{status_code}: {status_code_counts[status_code]}")


# Read from stdin line by line
for i, line in enumerate(sys.stdin, start=1):
    line = line.strip()

    # Parse the line based on the provided format
    try:
        _, _, _, _, status_code, file_size = line.split()
        status_code = int(status_code)
        file_size = int(file_size)
    except ValueError:
        # Skip the line if the format is not as expected
        continue

    # Update the metrics
    total_file_size += file_size
    if status_code in ALLOWED_STATUS_CODES:
        status_code_counts[status_code] = status_code_counts.get(
            status_code, 0) + 1

    # Print statistics after every 10 lines
    if i % 10 == 0:
        print_statistics()

# Print final statistics
print_statistics()















# import sys


# i = 0
# FileSize = 0
# status = {'200': 0, '301': 0, '400': 0, '401': 0,
#           '403': 0, '404': 0, '405': 0, '500': 0}
# codes = ['200', '301', '400', '401', '403', '404', '405', '500']
# try:
#     for line in sys.stdin:
#         i += 1
#         sp = line.split(' ')
#         if len(sp) > 2:
#             FileSize += int(sp[-1])
#             if sp[-2] in status:
#                 status[sp[-2]] += 1
#         if i % 10 == 0:
#             print("File size: {}".format(FileSize))
#             for code in codes:
#                 if status[code]:
#                     print("{}: {}".format(code, status[code]))
# except KeyboardInterrupt:
#     pass
# finally:
#     print("File size: {}".format(FileSize))
#     for code in codes:
#         if status[code]:
#             print("{}: {}".format(code, status[code]))
