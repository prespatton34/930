import random

def generate_phone_number():
  area_code = random.randint(100,999)
  exchange_code = random.randint(100,999)
  subscriber_number = random.randint(1000,9999)
  return f"({area_code}) {exchange_code}-{subsciber_number}"

phone_number = generate_phone_number()
print("You have reached", generate_phone_number())
