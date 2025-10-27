from src.phone_validatation import get_phone_info
from src.utils import save_to_file

print("Phone Number Info Checker")
print("Type 'exit' to quit\n")

while True:
    user_input = input("Type phone number with country code: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    info = get_phone_info(user_input)
    if "error" in info:
        print("Something went wrong!", info["error"])
    else:
        for key, value in info.items():
            print(f"{key}: {value}")
        save_to_file(info)
        print("Result saved!\n")
