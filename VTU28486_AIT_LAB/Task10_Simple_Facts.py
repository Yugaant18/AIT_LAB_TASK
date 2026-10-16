
# Task 10: Implementation of Simple Facts using Python

facts = [
    "john_is_cold",
    "raining",
    "john_forgot_his_raincoat",
    "fred_lost_his_car_key",
    "peter_football"
]

def verify_fact(fact):
    fact = fact.strip().lower()

    if fact == "john_forgot_his_raincoat":
        return True
    elif fact == "raining":
        return True
    elif fact == "foggy":
        return True
    elif fact == "cloudy":
        return False
    else:
        return False

for fact in facts:
    if verify_fact(fact):
        print(f"{fact} - YES")
    else:
        print(f"{fact} - NO")
