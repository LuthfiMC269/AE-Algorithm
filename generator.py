import random

def luhn_checksum(number):
    digits = [int(d) for d in str(number)]
    # Kalikan setiap digit genap dari kiri ke kanan (indeks genap di Python)
    for i in range(0, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    return sum(digits) % 10

def generate_luhn_number():
    while True:
        # Generate 15 random digits with the first digit not being 0 and no zeros
        random_number = str(random.randint(1, 9)) + ''.join(str(random.randint(1, 9)) for _ in range(14))

        # Pastikan tidak ada angka 0
        if '0' not in random_number:
            break

    # Calculate the check digit
    check_digit = (10 - luhn_checksum(random_number + '0')) % 10

    # Return the full number (15 digits + 1 check digit)
    return random_number + str(check_digit)

def verify_luhn(number):
    return luhn_checksum(number) == 0

# Generate and verify a Luhn number
number = generate_luhn_number()
print("Generated number:", number)
print("Is valid:", verify_luhn(number))