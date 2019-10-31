import timeit

exp_table = []
log_table = [0]*256

def mcd(a, b):
	rest = 0
	while(b > 0):
		rest = b
		b = a % b
		a = rest
	return a

def Modul(numero):
    aux = numero << 1
    if (aux & 0x100) == 0x100:
        aux ^= 0x1D
    return (aux & 0xFF)

def GF_product_p(a,b):
	res = 0
	for i in range(8):
	    if (b & 0x01) == 0x01:
	        res ^= a
	    a = Modul(a)
	    b >>= 1
	return res & 0xFF

def GF_es_generador(a):
	list = []
	for i in range(255):
		if mcd(i,255) == 1:
			list.append(2**i)
	return a in list

#Generador mes petit del cos es 0x02
def GF_tables():
	prod = 1
	exp_table.append(prod)
	for i in range(0,255):
		log_table[prod] = i
		prod = GF_product_p(prod,2)
		exp_table.append(prod)

def GF_product_t(a,b):
	if (a == 0 or b == 0): return 0
	else :
		iA = log_table[a]
		iB = log_table[b]
		return exp_table[(iA+iB)%255]

def GF_invers(a):
	if a == 0: return 0
	else :
		iA = log_table[a-1]
		return exp_table[255-iA-1]


#Los resultados de los tiempos estan en el documento GraficasParte2.pdf

GF_tables()

start = timeit.default_timer()
res = GF_product_p(0x32,0x02)
stop = timeit.default_timer()
print("Time GF product p(0x32,0x02) = " + str(stop - start) + " and result = " + str(res))

start = timeit.default_timer()
res = GF_product_t(0x32,0x02)
stop = timeit.default_timer()
print("Time GF product t(0x32,0x02) = " + str(stop - start) + " and result = " + str(res))

start = timeit.default_timer()
res = GF_product_p(0x32,0x03)
stop = timeit.default_timer()
print("Time GF product p(0x32,0x03) = " + str(stop - start) + " and result = " + str(res))

start = timeit.default_timer()
res = GF_product_t(0x32,0x03)
stop = timeit.default_timer()
print("Time GF product t(0x32,0x03) = " + str(stop - start) + " and result = " + str(res))

start = timeit.default_timer()
res = GF_product_p(0x32,0x09)
stop = timeit.default_timer()
print("Time GF product p(0x32,0x09) = " + str(stop - start) + " and result = " + str(res))

start = timeit.default_timer()
res = GF_product_t(0x32,0x09)
stop = timeit.default_timer()
print("Time GF product t(0x32,0x09) = " + str(stop - start) + " and result = " + str(res))

start = timeit.default_timer()
res = GF_product_p(0x32,0x0B)
stop = timeit.default_timer()
print("Time GF product p(0x32,0x0B) = " + str(stop - start) + " and result = " + str(res))

start = timeit.default_timer()
res = GF_product_t(0x32,0x0B)
stop = timeit.default_timer()
print("Time GF product t(0x32,0x0B) = " + str(stop - start) + " and result = " + str(res))

start = timeit.default_timer()
res = GF_product_p(0x32,0x0D)
stop = timeit.default_timer()
print("Time GF product p(0x32,0x0D) = " + str(stop - start) + " and result = " + str(res))

start = timeit.default_timer()
res = GF_product_t(0x32,0x0D)
stop = timeit.default_timer()
print("Time GF product t(0x32,0x0D) = " + str(stop - start) + " and result = " + str(res))

start = timeit.default_timer()
res = GF_product_p(0x32,0x0E)
stop = timeit.default_timer()
print("Time GF product p(0x32,0x0E) = " + str(stop - start) + " and result = " + str(res))

start = timeit.default_timer()
res = GF_product_t(0x32,0x0E)
stop = timeit.default_timer()
print("Time GF product t(0x32,0x0E) = " + str(stop - start) + " and result = " + str(res))
