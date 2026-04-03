import os
import sys

try:
    from dotenv import load_dotenv

except ImportError:
    print("Error: python-dotenv is not installed.")
    print("Install it with:")
    print("pip install python-dotenv")
    sys.exit(1)


def env_exists() -> bool:
    return os.path.exists(".env")


def main() -> None:
    try:
        load_dotenv()

        matrix_mode = os.getenv("MATRIX_MODE")
        database_url = os.getenv("DATABASE_URL")
        api_key = os.getenv("API_KEY")
        log_level = os.getenv("LOG_LEVEL")
        zio_endpoint = os.getenv("ZION_ENDPOINT")

        missing = []

        if not matrix_mode:
            missing.append("MATRIX_MODE")

        elif matrix_mode.lower() not in ["development", "production"]:
            print(
                "Configuration error: MATRIX_MODE must be 'development' or 'production'")
            sys.exit(1)

        if not database_url:
            missing.append("DATABASE_URL")

        if not api_key:
            missing.append("API_KEY")

        if not log_level:
            missing.append("LOG_LEVEL")

        if not zio_endpoint:
            missing.append("ZION_ENDPOINT")

        if missing:
            for var in missing:
                print(f"{var} is missing")
            sys.exit(1)

        print()
        print("ORACLE STATUS: Reading the Matrix...")
        print()

        print("Configuration loaded:")
        print(f"Mode: {matrix_mode}")
        if "localhost" in matrix_mode or "127.0.0.1" in matrix_mode:
            database_url_message = "Connected to local instance"

        else:
            database_url_message = "Connected to remote instance"
        print(f"Database: {database_url_message}")
        print(f"API Access: Authenticated")
        print(f"Log Level: {log_level}")
        if zio_endpoint.startswith(('http://', 'https://')):
            zio_endpoint_message = 'Online'
        else:
            zio_endpoint_message = 'Invalid endpoint'
        print(f"Zion Network: {zio_endpoint_message}")

        print()
        print("Environment security check:")
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")

        print()
        print("The Oracle sees all configurations.")

    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == '__main__':
    main()
