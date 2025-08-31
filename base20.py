DIGITS = [
    "A","B","C","D","E","F","G","H","I","J",
    "K","L","M","N","O","P","Q","R","S","T"
]

def base20(n: int) -> str:
    # handle zero
    if n == 0:
        return "A"

    # handle sign
    sign = ""
    if n < 0:
        sign = "-"
        n = -n

    out = ""

    # manual division and remainder loop
    while n > 0:
        # find remainder manually
        q = n // 20   # quotient
        r = n - q*20  # remainder
        out = DIGITS[r] + out  # prepend digit
        n = q

    return sign + out

if __name__ == "__main__":
    print(base20(400))   # BAA
    print(base20(12345)) # Example bigger one
    print(base20(-789))  # Negative number
