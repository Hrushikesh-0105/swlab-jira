DIGITS = [chr(ord('A')+i) for i in range(20)]

def base20(n: int) -> str:
    if n == 0: return "A"
    sign = "-" if n < 0 else ""
    n = abs(n)
    out = []
    while n:
        n, r = divmod(n, 20)
        out.append(DIGITS[r])
    return sign + "".join(reversed(out))

if __name__ == "__main__":
    print(base20(400))  # BAA
