def solution(s):
    pares = []
    for i in range(0, len(s), 2):
        par = s[i:i+2]
        if len(par) < 2: #último par
            par += '_'
        pares.append(par)
    return pares