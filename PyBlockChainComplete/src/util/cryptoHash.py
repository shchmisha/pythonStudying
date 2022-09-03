import hashlib
import json

def cryptoHash(*args):
    stringData = sorted([json.dumps(data) for data in args])
    joinedData = ''.join(stringData)

    return hashlib.sha256(joinedData.encode('utf-8')).hexdigest()