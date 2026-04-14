num = (12, 7, 9, 20, 33, 40)

A = sorted(set(num))
if len(A) < 2:
    print("No second highest")
else:
    hig = A[-2]
    print("Second highest number is =", hig)
