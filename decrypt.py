from cryptography.fernet import Fernet
def run(user, passw):
    key = b'PLmGOJrVJY_fgEA97zO503a-oa23PzieUikPJpOceoY='
    f = Fernet(key)
    encrypted = f.encrypt(passw)
    try:
        fry = open(user, "r").read()
        if fry == encrypted:
            return "200"
        else:
            return "404"
    except:
        return "500"