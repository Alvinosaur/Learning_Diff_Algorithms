def convert(s: str, numRows: int) -> str:
    if numRows == 1: return s
    substrings = ["" for i in range(numRows)]
    n = numRows + numRows - 2
    print(n)
    for index in range(len(s)):
        i = index + 1
        if i % n == 1:
            substrings[0] += s[index]
        elif i % n == 2 or i % n == 0:
            substrings[1] += s[index]
        else:
            j = 2
            k = n
            while (k - j >= 0):
                if i % n == j or i % n == k:
                    substrings[j-1] += s[index]
                    break
                j += 1
                k -= 1
    result = ""
    for substring in substrings:
        result += substring
    return result

print(convert(s = "PAYPALISHIRING", numRows = 4))
    