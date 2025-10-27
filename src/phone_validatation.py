# Contain main logic for processing phone numbers
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def get_phone_info(number_str, default_region=None):
    try:
        number = phonenumbers.parse(number_str, default_region)
        if not phonenumbers.is_valid_number(number):
            return {"error": "Invalid number"}

        return {
            "formatted": phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164),
            "country_code": number.country_code,
            "national_number": number.national_number,
            "region": geocoder.description_for_number(number, "en"),
            "carrier": carrier.name_for_number(number, "en"),
            "time_zones": timezone.time_zones_for_number(number),
        }
    except phonenumbers.NumberParseException as e:
        return {"error": str(e)}
