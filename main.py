import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def lookup_phone_number(raw_number: str):
    try:
        # Parse the number
        number = phonenumbers.parse(raw_number, None)

        # Validate & get metadata
        valid = phonenumbers.is_valid_number(number)
        possible = phonenumbers.is_possible_number(number)
        region = geocoder.description_for_number(number, "en")
        carrier_name = carrier.name_for_number(number, "en")
        tz = timezone.time_zones_for_number(number)

        print("-" * 40)
        print(f"Valid: {valid}")
        print(f"Possible: {possible}")
        print(f"Region: {region}")
        print(f"Carrier: {carrier_name if carrier_name else 'N/A'}")
        print(f"Timezones: {tz}")
        print(f"Country Code: +{number.country_code}")
        print(f"National Number: {number.national_number}")
        print("-" * 40)

    except phonenumbers.NumberParseException as e:
        print(f"Error parsing phone number: {e}")

def main():
    print("=== Phone Number Lookup ===")
    print("Type 'exit' or 'q' to quit.\n")
    try:
        while True:
            raw_number = input("Enter phone number with country code (e.g. +66812345678): ").strip()
            if not raw_number:
                continue
            if raw_number.lower() in ["exit", "q", "quit"]:
                print("Exiting...")
                break
            lookup_phone_number(raw_number)
    except (EOFError, KeyboardInterrupt):
        print("\nExiting...")

if __name__ == "__main__":
    main()

