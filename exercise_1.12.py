def Paskal(n,m):  #n-ը տողի համարն է, իսկ m-ը տողում եղած դիրքի
    if m == 1 or n == m:
        return 1
    return Paskal(n - 1, m - 1) + Paskal(n - 1, m)