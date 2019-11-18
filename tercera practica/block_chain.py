from rsa import *


class block_chain:

    def __init__(self, transaction, i):
        '''
        genera una cadena de blocs que es una llista de blocs,
        el primer bloc es un bloc "genesis" generat amb la transaccio "transaction"
        '''
        first_block = block(i)
        self.list_of_blocks = [first_block.genesis(transaction)]


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
                # pass
        return True

    def __repr__(self):
        return f'''{self.list_of_blocks}'''


class block:

    def __init__(self, seed):
        self.block_hash = None
        self.previous_block_hash = None
        self.transaction = None
        # self.seed = None
        self.seed = seed

    def _generate_block_hash_(self):
        entrada = str(self.previous_block_hash)
        entrada += str(self.transaction.public_key.publicExponent)
        entrada += str(self.transaction.public_key.modulus)
        entrada += str(self.transaction.message)
        entrada += str(self.transaction.signature)
        entrada += str(self.seed)
        return int(sha256(entrada.encode()).hexdigest(), 16)

    def genesis(self, transaction):
        '''
        genera el primer bloc d'una cadena amb la transacciò "transaction" que es caracteritza per:
        - previous_block_hash=0
        - ser válid
        '''
        # self.seed = 33289
        self.seed = self.seed
        self.previous_block_hash = 0
        self.transaction = transaction
        self.block_hash = self._generate_block_hash_()
        return self

    def next_block(self, transaction):
        '''
        genera el seguent block valid amb la transaccio "transaction"
        '''
        new_block = block(self.seed)
        # new_block.seed = 33289
        new_block.previous_block_hash = self.block_hash
        new_block.transaction = transaction
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
        first = self.previous_block_hash < 2 ** 240
        second = self.block_hash < 2 ** 240
        third = self.transaction.verify()
        # print(first, second, third)
        return first and second and third

    def __repr__(self):
        return f'''
            prevHash = {self.previous_block_hash}
            hash = {self.block_hash}
            limit = {2 ** 240}
            transaccion = {self.transaction}
            seed = {self.seed}
        '''


class transaction:

    def __init__(self, message, RSAkey):
        '''
        message: hasheado
        '''
        self.public_key = rsa_public_key(RSAkey)
        self.message = message  # Es un entero que representa el hash del mensaje -> solo hay que implementar m**da mod ma
        self.signature = RSAkey.sign(message)

    def verify(self):
        '''
        retorna el boolea True si "signature" es correspon amb una
        signatura de "message" feta amb la clau publica "public_key".
        En qualsevol altre cas retorma el boolea False
        '''
        return self.public_key.verify(self.message, self.signature)

    def __str__(self):
        return f'''holi'''


if __name__ == "__main__":
    RSA = rsa_key()
    transaccion = transaction(int(sha256("hola".encode()).hexdigest(), 16), RSA)
    # transaccion2 = transaction(int(sha256("hola 2".encode()).hexdigest(), 16), RSA)
    # transaccion3 = transaction(int(sha256("hola 3".encode()).hexdigest(), 16), RSA)
    # blockChain.add_block(transaccion2)
    # blockChain.add_block(transaccion3)
    # print(blockChain)
    
    for i in range(100000000000000000):

        blockChain = block_chain(transaccion, i)
        if blockChain.verify():
            print(i)
        
    
