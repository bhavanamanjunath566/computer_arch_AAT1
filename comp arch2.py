BITS = 8


def ROR(binary, positions):
    """Rotate Right without Carry"""
    print("\nROR Rotation Process:")

    for i in range(positions):
        last_bit = binary[-1]
        binary = last_bit + binary[:-1]
        print("After rotation", i + 1, ":", binary)

    return binary


def RCR(binary, carry, positions):
    """Rotate Right through Carry"""
    print("\nRCR Rotation Process:")

    for i in range(positions):
        last_bit = binary[-1]

        # Carry enters the MSB
        binary = str(carry) + binary[:-1]

        # Old LSB becomes the new carry
        carry = int(last_bit)

        print("After rotation", i + 1,
              ":", binary, " Carry =", carry)

    return binary, carry


# --------------------------------------------------
# (a) Rotate Right without Carry
# --------------------------------------------------

binary1 = "10111101"
positions = 3

print("======================================")
print("(a) ROR on", binary1, "by", positions, "positions")
print("======================================")

print("Original 8-bit number:", binary1)

result1 = ROR(binary1, positions)

print("Final ROR result:", result1)


# --------------------------------------------------
# (b) Rotate Right with Carry
# --------------------------------------------------

binary2 = "10100001"
carry = 0
positions = 3

print("\n======================================")
print("(b) RCR on", binary2, "by", positions, "positions")
print("======================================")

print("Original 8-bit number:", binary2)
print("Initial Carry:", carry)

result2, final_carry = RCR(binary2, carry, positions)

print("Final RCR result:", result2)
print("Final Carry:", final_carry)
