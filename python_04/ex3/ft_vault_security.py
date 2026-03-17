try:
    with open("classified_data.txt", "r+") as file:
        content = file.read()
        print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
        print()

        print("Initiating secure vault access...")
        print("Vault connection established with failsafe protocols")
        print()

        print("SECURE EXTRACTION:")
        print(content)
        print()

        print("SECURE PRESERVATION:")

    with open("security_protocols.txt", 'w') as file:
        file.write("[CLASSIFIED] New security protocols archived")

        print("[CLASSIFIED] New security protocols archived")
        print("Vault automatically sealed upon completion")
        print()

    print("All vault operations completed with maximum security.")

except FileNotFoundError:
    print("ERROR: Classified vault not found.")
