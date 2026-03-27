import sys


print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
print()

archivist_id: str = input("Input Stream active. Enter archivist ID: ")
status_report: str = input("Input Stream active. Enter status report: ")

print()
print(f"[STANDARD] Archive status from {archivist_id}: {status_report}")
print("[ALERT] System diagnostic: Communication channels verified",
      file=sys.stderr)
print("[STANDARD] Data transmission complete")
print()

print("Three-channel communication test successful.")
