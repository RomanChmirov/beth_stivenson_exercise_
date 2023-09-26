while factor <= n:

    if n % factor == 0:
        factor = factor

        n = int(n / factor)
    else:
        factor += 1