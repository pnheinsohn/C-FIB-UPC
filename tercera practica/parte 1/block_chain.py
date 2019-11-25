import pickle
from time import time
from random import randint
from hashlib import sha256

from rsa import rsa_key
from transaction import transaction


class block_chain:

    def __init__(self, transaction):
        '''
        genera una cadena de blocs que es una llista de blocs,
        el primer bloc es un bloc "genesis" generat amb la transaccio "transaction"
        '''
        new_block = block()
        first_block = new_block.genesis(transaction)
        self.list_of_blocks = [first_block]

    def add_block(self, transaction):
        '''
        afegeix a la llista de blocs un nou bloc valid generat amb la transaccio "transaction"
        '''
        new_block = self.list_of_blocks[-1].next_block(transaction)
        self.list_of_blocks.append(new_block)

    def verify(self):
        '''
        verifica si la cadena de blocs es valida:
        - Comprova que tots el blocs son valids
        - Comprova que el primer bloc es un bloc "genesis"
        - Comprova que per cada bloc de la cadena el seguent es el correcte
        Si totes les comprovacions son correctes retorna el boolea True.
        En qualsevol
        '''
        for b in self.list_of_blocks:
            if not b.verify_block():
                return False
        return True

    def __repr__(self):
        return f'''{self.list_of_blocks}'''


class block:

    def __init__(self):
        self.block_hash = None
        self.previous_block_hash = None
        self.transaction = None
        self.seed = None

    def _generate_block_hash_(self):
        while True:  # For setting a correct seed
            self.seed = randint(0, 2 ** 256)
            entrada = str(self.previous_block_hash)
            entrada += str(self.transaction.public_key.publicExponent)
            entrada += str(self.transaction.public_key.modulus)
            entrada += str(self.transaction.message)
            entrada += str(self.transaction.signature)
            entrada += str(self.seed)
            entrada = int(sha256(entrada.encode()).hexdigest(), 16)
            if entrada < 2 ** (256 - D):
                break
        return entrada

    def genesis(self, transaction):
        '''
        genera el primer bloc d'una cadena amb la transacciò "transaction" que es caracteritza per:
        - previous_block_hash=0
        - ser válid
        '''
        self.previous_block_hash = 0
        self.transaction = transaction
        self.block_hash = self._generate_block_hash_()
        return self

    def next_block(self, transaction):
        '''
        genera el seguent block valid amb la transaccio "transaction"
        '''
        new_block = block()
        new_block.transaction = transaction
        new_block.previous_block_hash = self.block_hash
        new_block.block_hash = new_block._generate_block_hash_()
        return new_block

    def verify_block(self):
        '''
        Verifica si un bloc es valid:
        -Comprova que el hash del bloc anterior cumpleix las condicions exigides
        -Comprova la transaccio del bloc es valida
        -Comprova que el hash del bloc cumpleix las condicions exigides
        Si totes les comprovacions son correctes retorna el boolea True.
        En qualsevol altre cas retorma el boolea False
        '''
        first = self.previous_block_hash < 2 ** (256 - D)
        second = self.block_hash < 2 ** (256 - D)
        third = self.transaction.verify()
        return first and second and third

    def __repr__(self):
        return f"seed = {self.seed}\nprevHash = {self.previous_block_hash}\nhash = {self.block_hash}\nlimit = {2 ** 256 - D}\ntransaccion = {self.transaction}"


if __name__ == "__main__":
    D = 16  # Para el exponente
    RSA = rsa_key()

    # Genera un iterable (solo puede ser iterado una única vez)
    transactions = map(lambda i: transaction(int(sha256(f"hola {i}".encode()).hexdigest(), 16), RSA), range(100))
    
    now = time()
    blockChain = block_chain(next(transactions))  # Obtenemos la primera transacción para generar el Block Chain
    for _ in range(99):  # Toma entre 400 a 600 segundos
        blockChain.add_block(next(transactions))  # Obtenemos las próximas transacciones y las agregamos a Block Chain

    with open("output/100blocks.pickle", 'wb') as output_file:
        pickle.dump(blockChain, output_file)

    print(f"File 'output/100blocks.pickle' has been created!\nVerification: {blockChain.verify()}\nTime elapsed: {time() - now}")
