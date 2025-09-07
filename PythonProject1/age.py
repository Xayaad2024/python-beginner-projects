while True:
    magaca = input("magacaaga iisheeg walaal:")
    if magaca == 'kabax':
        break
    dada_sogali = input("meeqaa jirbaatahay?")
    if not dada_sogali.isdigit():
        print("khalad ayaad galisay fadlan badal")
        continue
    da = int(dada_sogali)
    if da <0:
        print("da eber kamayaraan karto ")
    elif da <16:
        print("wali waxaatahay caruur.")
    elif da < 21:
        print("waxaad kujirtaa tobaneeyada.")
    elif da < 60:
        print("waxaatahay qof weyn.")
    else:
        print("waayeel ayaatahay.")
    print("------------------------------------------------")