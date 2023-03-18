from OpenSSL import crypto

KEY_SIZE = 4096

def write_to_file(data, filename):
    with open(filename, "wb") as file:
        file.write(data)
        file.close()

def create_public_key_pair(key_file):
    k = crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, KEY_SIZE)
    pem_key = crypto.dump_privatekey(crypto.FILETYPE_PEM, k)
    write_to_file(pem_key, key_file)
    return k

def create_self_signed_cert(cert_file, key):
    cert = crypto.X509()
    cert.set_serial_number(1001)
    cert.set_notBefore(b"20230101000000Z")
    cert.set_notAfter(b"20250101000000Z")

    subject = cert.get_subject()
    subject.C = "NO"
    subject.ST = "Aust-Agder"
    subject.L = "Grimstad"
    subject.O = "UiA"
    subject.OU = "IKT"
    subject.CN = "localhost"

    cert.set_issuer(subject)
    cert.set_pubkey(key)
    cert.sign(key, "SHA256")

    pem_cert = crypto.dump_certificate(crypto.FILETYPE_PEM, cert)
    write_to_file(pem_cert, cert_file)
    return cert

if __name__ == "__main__":
    key_file = "example.key"
    cert_file = "example.crt"

    key = create_public_key_pair(key_file)
    create_self_signed_cert(cert_file, key)