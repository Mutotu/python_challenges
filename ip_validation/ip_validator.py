def ip_validator(ip):
    # Split the IP address into four parts based on the '.' delimiter
    split_ip = ip.split('.')

    # Check if we have exactly four parts
    if len(split_ip) != 4:
        return False

    for part in split_ip:
        # Check for leading zero (allow '0' but not '01', '001', etc.)
        if len(part) > 1 and part[0] == '0':
            return False

        # Check if the part is a valid integer within range
        try:
            num = int(part)  # Convert part to integer
        except ValueError:
            return False  # If conversion fails, it's not a valid IP segment

        if num < 0 or num > 255:
            return False  # Ensure it's within the valid IP range (0-255)

    # If all checks pass, the IP address is valid
    return True
