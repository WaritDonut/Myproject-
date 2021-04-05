IDXING = [312,2132.3,4542.7,43563.2,70423,1432521,32315] 
IDXmax = IDXING[0]
i = 0 
for m in IDXING: 
    if(m>IDXmax): 
        IDXmax = m 
        smax = i 
    i += 1
print('ตำแหน่งที่ %d คือค่าดัชนีที่มากที่สุด %.1f'%(smax,IDXmax))
