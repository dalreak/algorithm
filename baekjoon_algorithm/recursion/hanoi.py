def T(N, Beg, Aux, End):
    if N == 1:
	    print(Beg, End)
    else:
	    T(N-1, Beg, End, Aux)
	    T(1, Beg, Aux, End)
	    T(N-1, Aux, Beg, End)

num = int(input())
print((2 ** num) -1)
T(num,1,2,3)