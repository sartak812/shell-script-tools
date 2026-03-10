"""Practice Homework 5: Minimal Fail2Ban-style log analyzer."""

# Store the simulated login attempts as a list of dictionaries.
login_logs = [
    # Record 1: failed admin attempt from 192.168.1.15.
    {"ip": "192.168.1.15", "user": "admin", "status": "failed"},
    # Record 2: successful root login from 10.0.0.45.
    {"ip": "10.0.0.45", "user": "root", "status": "success"},
    # Record 3: failed root attempt from the same 192.168.1.15 host.
    {"ip": "192.168.1.15", "user": "root", "status": "failed"},
    # Record 4: successful ubuntu login from 172.16.0.5.
    {"ip": "172.16.0.5", "user": "ubuntu", "status": "success"},
    # Record 5: another failed admin attempt from 192.168.1.15.
    {"ip": "192.168.1.15", "user": "admin", "status": "failed"},
    # Record 6: failed admin attempt from 10.0.0.45.
    {"ip": "10.0.0.45", "user": "admin", "status": "failed"},
    # Record 7: failed root attempt from 203.0.113.8.
    {"ip": "203.0.113.8", "user": "root", "status": "failed"},
    # Record 8: another failed root attempt from 203.0.113.8.
    {"ip": "203.0.113.8", "user": "root", "status": "failed"},
    # Record 9: failed admin attempt from 203.0.113.8.
    {"ip": "203.0.113.8", "user": "admin", "status": "failed"},
    # Record 10: successful root login from 10.0.0.45.
    {"ip": "10.0.0.45", "user": "root", "status": "success"},
]

# Define a helper that mimics pushing an IP address to multiple firewalls.
def block_ip(ip_address: str) -> None:
    """Simulate placing an IP address on three separate firewalls."""

    # Initialize the firewall counter at the first firewall.
    firewall_id = 1

    # Keep looping while there are firewalls left to update.
    while firewall_id <= 3:
        # Report which firewall we are "blocking" on right now.
        print(f"Blocking {ip_address} on Firewall {firewall_id}...")
        # Increment the firewall counter so we eventually exit.
        firewall_id += 1

# Define the analyzer that inspects logs and decides which IPs to ban.
def analyze_logs(logs: list[dict[str, str]]) -> list[str]:
    """Count failed attempts per IP and block the noisy ones."""

    # Start with an empty dictionary that will track failed attempts per IP.
    failed_counts: dict[str, int] = {}

    # Iterate over every dictionary (record) inside the logs list.
    for record in logs:
        # Check whether the status of this record equals "failed".
        if record.get("status") == "failed":
            # Capture the IP address from the record (defaulting to "unknown").
            ip_address = record.get("ip", "unknown")
            # If we have seen this IP before, add one to its failure counter.
            if ip_address in failed_counts:
                # Increment the existing counter for this IP.
                failed_counts[ip_address] += 1
            # If the IP is brand new, seed its counter at one failure.
            else:
                # Create a new key in the dictionary for the fresh IP.
                failed_counts[ip_address] = 1

    # Prepare a list that will eventually contain the banned IP addresses.
    banned_ips: list[str] = []

    # Loop over both the IP and its failure count at the same time.
    for ip_address, count in failed_counts.items():
        # Only take action if the failure count is three or higher.
        if count >= 3:
            # Remember this IP in the banned list so we can audit later.
            banned_ips.append(ip_address)
            # Trigger the simulated firewall updates for this IP.
            block_ip(ip_address)

    # Return the completed list of banned IP addresses to the caller.
    return banned_ips

# Run the analyzer immediately when the script executes as a program.
analyze_logs(login_logs)
