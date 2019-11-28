from rsa import rsa_public_key


class transaction:

    def __init__(self, message, RSAkey):
        '''
        message: hasheado
        '''
        self.message = message
        self.signature = RSAkey.sign(message)
        self.public_key = rsa_public_key(RSAkey)

    def verify(self):
        '''
        retorna el boolea True si "signature" es correspon amb una
        signatura de "message" feta amb la clau publica "public_key".
        En qualsevol altre cas retorma el boolea False
        '''
        return self.public_key.verify(self.message, self.signature)

    # def __str__(self):
    #     return f"(\nMessage: {self.message}\nSignature: {self.signature}\n)\n"
