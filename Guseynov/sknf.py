s = ""
symb = ["a", "b", "c", "d", "e"]
k = int(input())
for i in range(2 ** k):
    arr = list(map(int, input().split()))
    if not (arr[-1]):
        s += "("
        for j in range(len(arr) - 1):
            if j != 0: s += " + "
            if not (arr[j]):
                s += symb[j]
            else:
                s = s + "-" + symb[j]
        s += ")"

print(s)