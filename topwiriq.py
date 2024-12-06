
# def decimal_to_binary(decimal_number):
#     binary_number = bin(decimal_number)[2:]  # bin() funksiyasi 0b bilan boshlanadi, [2:] bilan uni olib tashlaymiz
#     return binary_number
#
# # Misol
# decimal_number = 45
# binary_result = decimal_to_binary(decimal_number)
# print(f"{decimal_number} ning 2-lik sanoq sistemasidagi ko‘rinishi: {binary_result}")

# 10 => 8
# def decimal_to_octal(decimal_number):
#     octal_number = oct(decimal_number)[2:]
#     return octal_number
#
# decimal_number = int(input("10-lik sanoq sistemasidagi raqamni kiriting: "))
#
# octal_number = decimal_to_octal(decimal_number)
#
# print(f"{decimal_number} (10-lik) => {octal_number} (8-lik)")

# 10 => 16
def decimal_to_hexadecimal(decimal_number):
    hexadecimal_number = hex(decimal_number)[2:].upper()
    return hexadecimal_number

decimal_number = int(input("10-lik sanoq sistemasidagi raqamni kiriting: "))

hexadecimal_number = decimal_to_hexadecimal(decimal_number)

print(f"{decimal_number} (10-lik) => {hexadecimal_number} (16-lik)")

