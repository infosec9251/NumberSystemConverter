def decimal_to_binary(decimal_number):
    binary_number = bin(decimal_number)[2:]  # bin() funksiyasi 0b bilan boshlanadi, [2:] bilan uni olib tashlaymiz
    return binary_number

# Misol
decimal_number = 45
binary_result = decimal_to_binary(decimal_number)
print(f"{decimal_number} ning 2-lik sanoq sistemasidagi ko‘rinishi: {binary_result}")
