s = ""
symb = ["a", "b", "c", "d", "e"]
k = int(input())
for i in range(2 ** k):
    arr = list(map(int, input().split()))
    if arr[-1]:
        if s != "":
            s += "+"
        for j in range(len(arr) - 1):
            if j != 0: s += "^"
            if arr[j]:
                s += symb[j]
            else:
                s = s + "(-" + symb[j] + ")"
print(s)

