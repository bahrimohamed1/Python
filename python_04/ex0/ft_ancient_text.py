try:
    file = open("ancient_fragment.txt", 'r')
    content = file.read()

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault: ancient\\_fragment.txt")
    print("Connection established...\n")
    print("RECOVERED DATA:")
    print(content)
    print("\nData recovery complete. Storage unit disconnected.")

    file.close()
except FileNotFoundError:
    print(" ERROR: Storage vault not found")
