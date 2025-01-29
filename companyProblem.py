# Problem 1 (Qualifying Round): 

# In the digital epicenter of Bengaluru, India's Silicon Valley, you are part of an elite cybersecurity team tasked with safeguarding the nation's critical infrastructure servers. Recently, there's been a surge in unauthorized access attempts targeting these servers. Your mission is to analyze the access logs and identify any security violations in accordance with the country's stringent cybersecurity policies.

# Problem Statement
# You are provided with an access log containing entries of login attempts to the secure servers. Each log entry has the following format:
# timestamp username ip_address access_result

#  - timestamp: The time of the access attempt in ISO 8601 format (e.g., 2021-10-01T10:00:00Z).
#  - username: The username used for the attempt (lowercase letters, up to 20 characters).
#  - ip_address: The IPv4 address from which the attempt was made.
#  - access_result: Either SUCCESS or FAILURE.

# Security Policies
# The servers enforce the following multi-tiered security policies:

# 1. User Lockout Policy:
#  - If a user has three consecutive failed login attempts (from any IP address), they are locked out for the next 5 minutes (300 seconds).
#  - Any login attempts during the lockout period are considered lockout violations.
#  - A successful login resets the user's failure count.

# 2. IP Blacklist Policy:
#  - If an IP address accumulates five failed login attempts within any 20-minute window, it is blacklisted for the next 30 minutes (1800 seconds).
#  - Any login attempts from a blacklisted IP are considered blacklist violations.
#  - Successful logins do not reset the IP's failure count.

# 3. Account Suspension Policy:
#  - If a user has ten failed login attempts within a 24-hour window, regardless of IP address or successful logins in between, their account is suspended.
#  - Any login attempts after an account is suspended are considered suspension violations.
#  - Once suspended, the account remains suspended for the remainder of the logs (no automatic unsuspension).

# Your Task
# Write a program that processes the access log and identifies all violations according to the security policies above.

# For each violation, output a line in the following format:

# ViolationType timestamp username ip_address

#  - ViolationType: LOCKOUT_VIOLATION, BLACKLIST_VIOLATION, or SUSPENSION_VIOLATION.
#  - timestamp: The timestamp of the violating access attempt.
#  - username: The username used in the violating access attempt.
#  - ip_address: The IP address from which the violating access attempt was made.

# List the violations in chronological order (sorted by timestamp).

# ------------------------------------------------------------

# Sample Input 1 : 
# 14
# 2021-10-01T10:00:00Z alice 192.168.1.2 FAILURE
# 2021-10-01T10:01:00Z alice 192.168.1.3 FAILURE
# 2021-10-01T10:02:00Z alice 192.168.1.4 FAILURE
# 2021-10-01T10:03:00Z alice 192.168.1.5 FAILURE
# 2021-10-01T10:08:00Z alice 192.168.1.2 SUCCESS
# 2021-10-01T10:06:00Z bob 10.0.0.1 FAILURE
# 2021-10-01T10:07:00Z bob 10.0.0.1 FAILURE
# 2021-10-01T10:08:00Z bob 10.0.0.1 SUCCESS
# 2021-10-01T10:09:00Z bob 10.0.0.1 FAILURE
# 2021-10-01T10:12:00Z bob 10.0.0.1 FAILURE
# 2021-10-01T10:15:00Z bob 10.0.0.1 FAILURE
# 2021-10-01T10:18:00Z bob 10.0.0.1 FAILURE
# 2021-10-01T10:21:00Z bob 10.0.0.1 FAILURE
# 2021-10-01T10:24:00Z bob 10.0.0.1 FAILURE

# Sample Output 1 : 
# LOCKOUT_VIOLATION 2021-10-01T10:03:00Z alice 192.168.1.5
# BLACKLIST_VIOLATION 2021-10-01T10:18:00Z bob 10.0.0.1
# BLACKLIST_VIOLATION 2021-10-01T10:21:00Z bob 10.0.0.1
# BLACKLIST_VIOLATION 2021-10-01T10:24:00Z bob 10.0.0.1

# Explanation of the Output :
# 1. Alice:
#  - Failed login attempts at 10:00, 10:01, and 10:02.
#  - After the third failure, she is locked out until 10:07:00Z (5-minute lockout starting from 10:02:00Z).
#  - She attempts to log in again at 10:03 during her lockout period, resulting in a LOCKOUT_VIOLATION.
#  - At 10:08, after her lockout period has ended, she successfully logs in, resetting her failure count and lockout status.

# 2. Bob:
#  - Failed login attempts at 10:06, and 10:07.
#  - Successful login at 10:08, resetting his failure count for Lockout Policy but not for blacklisted.
#  - Failed attempts at 10:09, 10:12, and 10:15 from IP 10.0.0.1 within a 20-minute window.
#  - The five failures from 10:06 to 10:15 cause IP 10.0.0.1 to be blacklisted until 10:45:00Z (30-minute blacklist starting from 10:15:00Z).
#  - His attempt at 10:18, 10:21, and 10:24 is a BLACKLIST_VIOLATION because it's from a blacklisted IP.
#  - Since Bob has not yet reached ten total failures within 24 hours, there is no suspension violation at this point.

# ------------------------------------------------------------

# Sample Input 2 : 
# 4
# 2021-10-05T08:00:00Z user1 10.10.0.1 FAILURE
# 2021-10-05T08:01:00Z user1 10.10.0.1 FAILURE
# 2021-10-05T08:02:00Z user1 10.10.0.1 SUCCESS
# 2021-10-05T08:03:00Z user1 10.10.0.3 SUCCESS

# Sample Output 2 : 
# NO_VIOLATION

# Explanation of the Output :
# Since no violation has occurred, the output is ‘NO_VIOLATION’.

# ------------------------------------------------------------
# Your expertise in cybersecurity is crucial to keeping Bengaluru safe. Analyze the logs carefully, implement the security policies accurately, and help us thwart any malicious attempts to compromise our systems.

from typing import TypedDict
from datetime import datetime
from enum import StrEnum
import click

def print_error(message: str) -> None:
    click.echo(click.style(message, fg='red', bold=True))

def print_success(message: str) -> None:
    click.echo(click.style(message, fg='green', bold=True))

def print_warning(message: str) -> None:
    click.echo(click.style(message, fg='yellow', bold=True))

def print_info(message: str) -> None:
    click.echo(click.style(message, fg='blue', bold=True))

def print_default(message: str) -> None:
    click.echo(click.style(message, fg='white', bold=True))


class AccessResult(StrEnum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class Log(TypedDict):
    timestapm: datetime
    username: str
    ip_address: str
    access_result: AccessResult


def parse_log(log: str) -> Log:
    timestamp, username, ip_address, access_result = log.strip().split()
    return Log(timestapm=datetime.fromisoformat(timestamp),username=username, ip_address=ip_address, access_result=[x for x in AccessResult if x.value == access_result][0])

# def validate_output(tests, expected_results, output):


def main() -> None:
    with open('test_cases.txt', 'r') as test_case_file, open('expected_output.txt', 'r') as expected_output_file:
        tests = [parse_log(line) for line in test_case_file.readlines()]
        expected_results = expected_output_file.readlines()
    



if __name__ == '__main__':
    main()
