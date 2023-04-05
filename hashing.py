from passlib.context import CryptContext

hex_pass = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        return hex_pass.hash(password)
    def verify(plain_password, hash_password):
        return hex_pass.verify(plain_password,hash_password)