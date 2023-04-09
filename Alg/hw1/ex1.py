
def close_key(nod, nok):
    if nok < nod:
        temp = nok
        nok = nod
        nod = temp

    if nok % nod != 0:
        return(0)
    else:
        nok //= nod

        i = 2
        ans = 0
        while i**2 <= nok:
            if nok % i == 0:
                ans += 1
                while nok % i == 0:
                    nok //= i
            i += 1

        if nok != 1:
            ans += 1

        return (2 ** ans)



print(close_key(10, 20))