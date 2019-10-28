##################
##  Parte N°1   ##
##################

from time import time


def GF_product_p(px, qx, mod=0x11d):
    res = 0
    while qx > 0:
        if qx % 2 != 0:
            res ^= px
        px <<= 1  # Multiply by x 
        if px > 0xff:
            px ^= mod
        qx >>= 1
    return res

def GF_es_generador(a):
    if a == 0:
        return False
    res = 1
    for i in range(1, 256):
        res = GF_product_p(res, a)
        if res == 1:
            if i == 255:
                return True
            return False
    return False

def GF_tables(gen=2):
    # Exponential
    exp_res = 1
    exp_table = []
    for _ in range(1, 256):
        exp_table.append(exp_res)
        exp_res = GF_product_p(exp_res, gen)
    exp_table.append(1)

    # Logarithmic
    log_res = 1
    log_table = ["*" for _ in range(0, 256)]
    for i in range(0, 255):
        log_table[log_res] = i
        log_res = GF_product_p(log_res, gen)
    return exp_table, log_table

def GF_product_t(a, b):
    return EXP_TABLE[(LOG_TABLE[a] + LOG_TABLE[b]) % 255]

def GF_invers(polynom):
    if polynom < 1 or polynom > 255:
        return "Input de inverso inválido"
    return EXP_TABLE[255 - LOG_TABLE[polynom]]


if __name__ == "__main__":
    EXP_TABLE, LOG_TABLE = GF_tables()
    while True:
        a = int(input("Ingrese número: "))
        t1 = time()
        p = GF_product_p(a, 0x02)
        tf1 = time() - t1
        t2 = time()
        t = GF_product_t(a, 0x02)
        tf2 = time() - t2
        print("a,0x02")
        print(f"Resultado: {p} == {t}")
        print(f"Tiempo: {tf1} vs {tf2}\n")

        t1 = time()
        p = GF_product_p(a, 0x03)
        tf1 = time() - t1
        t2 = time()
        t = GF_product_t(a, 0x03)
        tf2 = time() - t2
        print("a,0x03")
        print(f"Resultado: {p} == {t}")
        print(f"Tiempo: {tf1} vs {tf2}\n")

        t1 = time()
        p = GF_product_p(a, 0x09)
        tf1 = time() - t1
        t2 = time()
        t = GF_product_t(a, 0x09)
        tf2 = time() - t2
        print("a,0x09")
        print(f"Resultado: {p} == {t}")
        print(f"Tiempo: {tf1} vs {tf2}\n")

        t1 = time()
        p = GF_product_p(a, 0x0b)
        tf1 = time() - t1
        t2 = time()
        t = GF_product_t(a, 0x0b)
        tf2 = time() - t2
        print("a,0x0b")
        print(f"Resultado: {p} == {t}")
        print(f"Tiempo: {tf1} vs {tf2}\n")

        t1 = time()
        p = GF_product_p(a, 0x0d)
        tf1 = time() - t1
        t2 = time()
        t = GF_product_t(a, 0x0d)
        tf2 = time() - t2
        print("a,0x0d")
        print(f"Resultado: {p} == {t}")
        print(f"Tiempo: {tf1} vs {tf2}\n")

        t1 = time()
        p = GF_product_p(a, 0x0e)
        tf1 = time() - t1
        t2 = time()
        t = GF_product_t(a, 0x0e)
        tf2 = time() - t2
        print("a,0x0e")
        print(f"Resultado: {p} == {t}")
        print(f"Tiempo: {tf1} vs {tf2}\n")
