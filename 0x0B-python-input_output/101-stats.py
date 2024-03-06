#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics
"""


import sys
from collections import defaultdict


def print_metrics(total_size, status_counts):
    """
    Prints the metrics computed from the given total file size
    and status counts.

    Parameters:
    total_size (int): The total file size.
    status_counts (dict): A dictionary containing the counts
    of different status codes.

    Returns:
    None

    Example:
    >>> total_size = 1000
    >>> status_counts = {'200': 5, '404': 2, '500': 1}
    >>> print_metrics(total_size, status_counts)
    Total file size: 1000
    200: 5
    404: 2
    500: 1
    """
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")


def main():
    """
    Reads stdin line by line and computes metrics.

    Returns:
    None

    Example:
    >>> main()
    Total file size: 1000
    200: 5
    404: 2
    500: 1
    """
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            # Parse the input line
            parts = line.split()
            if len(parts) < 9:
                continue  # Skip invalid lines

            status_code = parts[8]
            file_size = int(parts[9])

            # Update total file size and status counts
            total_size += file_size
            status_counts[status_code] += 1

            # Increment line count
            line_count += 1

            # Print metrics every 10 lines
            if line_count % 10 == 0:
                print_metrics(total_size, status_counts)
    except KeyboardInterrupt:
        print_metrics(total_size, status_counts)

if __name__ == "__main__":
    main()
