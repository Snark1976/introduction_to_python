st, dct = input(), {}
for i in st.split():
    if dct.setdefault(i, 0) > 0:
        print(f'{i}_{dct[i]}', end=' ')        
    else:
        print(f'{i}', end=' ')
    dct[i] += 1