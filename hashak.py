#haslib erabiltzen MD5 eta SHA256 bitartez fitxategien hash-ak kalkulatzeko.

import hashlib

class hasheatzen:

    def __init__(self):
        f = raw_input("Sartu hasheatu nahi duzun fitxategia :>")
        print("***************" + f + "*****************")
        self.eskatu_fitxategia(f)
        print("*****************************************")
    def file_hash_512(self, filename):
        h = hashlib.sha512()
        with open(filename, 'rb', buffering=0) as f:
           for b in iter(lambda: f.read(128*1024), b''):
               h.update(b)
        return h.hexdigest()

    def file_hash_256(self, filename):
        h  = hashlib.sha256()
        with open(filename, 'rb', buffering=0) as f:
           for b in iter(lambda: f.read(128*1024), b''):
               h.update(b)
        return h.hexdigest()

    def file_hash_MD5(self, filename):
        h = hashlib.md5()
        with open(filename, 'rb', buffering=0) as f:
           for b in iter(lambda: f.read(128 * 1024), b''):
               h.update(b)
        return h.hexdigest()

    def eskatu_fitxategia(self, fitxategia):
        m = self.file_hash_MD5(fitxategia)
        s2 = self.file_hash_256(fitxategia)
        s5 = self.file_hash_512(fitxategia)
        print("MD5: " + m)
        print("SHA256: " + s2)
        print("SHA512: " + s5)

h = hasheatzen()

