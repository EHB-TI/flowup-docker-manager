import hashlib, time

def tokenGenerator():
    h = hashlib.sha256()
    timing = str(round(time.time()))
    salt = timing[:-2]
    h.update(bytes(salt, 'utf-8'))
    return h.hexdigest()

