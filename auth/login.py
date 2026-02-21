from passlib.context import CryptContext

pwd_context = CryptContext(
        schemes=['argon2', 'bcrypt'],
        deprecated='auto'
        )

def hash_password(password_string):
    return pwd_context.hash(password_string)

def authentication(stored_password, plain_password):
    '''Simple Authentication part for verifying password'''
    return pwd_context.verify(plain_password, stored_password)
