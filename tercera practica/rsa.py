from hashlib import sha256
from Crypto import Random
from Crypto.Util import number


class rsa_key:

    def __init__(self, bits_modulo=2048, e=2**16+1):
        '''
        genera una clau RSA (de 2048 bits i amb exponent public 2**16+1 per defecte)
        '''
        self.publicExponent = e
        self.primeP = number.getPrime(bits_modulo, randfunc=Random.get_random_bytes)
        self.primeQ = number.getPrime(bits_modulo, randfunc=Random.get_random_bytes)
        self.modulus = self.primeP * self.primeQ

        self.privateExponent = number.inverse(self.publicExponent, (self.primeP - 1) * (self.primeQ - 1))

        self.inverseQModulusP = number.inverse(self.primeQ, self.primeP)
        self.privateExponentModulusPhiP = number.inverse(self.privateExponent, self.primeP - 1)
        self.privateExponentModulusPhiQ = number.inverse(self.privateExponent, self.primeQ - 1)

    def sign(self, message):
        '''
        message: hasheado
        retorma un enter que és la signatura de "message" feta amb la clau RSA fent servir el TXR
        '''
        d_1 = self.privateExponent % (self.primeP - 1)
        d_2 = self.privateExponent % (self.primeQ - 1)
        p_1 = number.inverse(self.primeP, self.primeQ)
        q_1 = number.inverse(self.primeQ, self.primeP)

        c_1 = pow(message, d_1, self.primeP)
        c_2 = pow(message, d_2, self.primeQ)

        return (c_1 * q_1 * self.primeQ + c_2 * p_1 * self.primeP) % self.modulus

    def sign_slow(self, message):
        '''
        message: hasheado
        retorma un enter que és la signatura de "message" feta amb la clau RSA sense fer servir el TXR
        '''
        return pow(message, self.privateExponent, self.modulus)

    def print_key(self):
        print(f'''
            prime p: {self.primeP}
            prime q: {self.primeQ}
            modulus: {self.modulus}
            Public exponent: {self.publicExponent}
            Private exponent: {self.privateExponent}
        ''')

class rsa_public_key:

    def __init__(self, rsa_key):
        self.publicExponent = rsa_key.publicExponent
        self.modulus = rsa_key.modulus

    def verify(self, message, signature):
        '''
        retorna el booleà True si "signature" es correspon amb una
        signatura de "message" feta amb la clau RSA associada a la clau
        pública RSA.
        En qualsevol altre cas retorma el booleà False
        '''
        h = pow(signature, self.publicExponent, self.modulus)
        return h == message


if __name__ == "__main__":
    RSA = rsa_key()
    public_rsa = rsa_public_key(RSA)
