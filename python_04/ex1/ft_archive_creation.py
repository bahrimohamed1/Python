file = open("new_discovery.txt", 'w')

print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
print()
print(f"Initializing new storage unit: {file.name}")
print("Storage unit created successfully...")
print()
print("Inscribing preservation data...")

file.write("[ENTRY 001] New quantum algorithm discovered\n")
print("[ENTRY 001] New quantum algorithm discovered")

file.write("[ENTRY 002] Efficiency increased by 347%\n")
print("[ENTRY 002] Efficiency increased by 347%")

file.write("[ENTRY 003] Archived by Data Archivist trainee")
print("[ENTRY 003] Archived by Data Archivist trainee")

print()

print("Data inscription complete. Storage unit sealed.")
print(f"Archive '{file.name}' ready for long-term preservation.")

file.close()
