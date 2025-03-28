while True:
    n = int(input())
    if n == -1:
        break
    arr = [i for i in range(1, n) if n%i==0]
    if n == sum(arr):
        print(n, " = ", " + ".join(str(i) for i in arr), sep="")
    else:
        print(n, "is NOT perfect.")

