print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
print()

try:
    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    with open("lost_archive.txt", 'r') as f:
        content = f.read()
        print("SUCCESS:", content)
except FileNotFoundError:
    print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable")

print()

try:
    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    with open('classified_vault.txt', 'w') as f:
        f.write("IT SHOULD FAIL ANYWAY")
except PermissionError:
    print("RESPONSE: Security protocols deny access")
    print("STATUS: Crisis handled, security maintained")

print()

try:
    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    with open("standard_archive.txt", 'r') as f:
        content = f.read()
        print(f"SUCCESS: Archive recovered - ''{content}''")
        print("STATUS: Normal operations resumed")
except FileNotFoundError:
    print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable")

# print()

# try:
#     print("CRISIS ALERT: Attempting access to 'system_lockdown'...")
#     with open("/dev/null", 'r') as f:
#             pass
#     raise ValueError("Simulated system anomaly")
# except Exception as e:
#         print(f"RESPONSE: System anomaly - {e}")
#         print("STATUS: Crisis handled, failover protocols engaged")

print()
print("All crisis scenarios handled successfully. Archives secure.")
