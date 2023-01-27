import math

def RSA(m):
    p = int(input("Enter p >> "))
    q = int(input("Enter q >> "))

    n = p*q

    phi = (p-1)*(q-1)

    e = 2
    while e < phi :
        if ( math.gcd(e, phi) == 1 and math.gcd(e, n) == 1):
            break
        else:
            e += 1

    d = 1
    while math.fmod(d*e , phi) != 1:
        d += 1

    print("\n\nOriginal Message >> " + str(m))

    encrypt = pow(m, e)
    encrypt = math.fmod(encrypt, n)

    print("\nEncrypted Message >> " + str(encrypt))

    decrypt = pow(encrypt, d)
    decrypt = math.fmod(decrypt, n)

    print("\nDecrypted Message >> " + str(int(decrypt)))

def main():
    m = int(input("Enter the message >> "))
    RSA(m)

if __name__ == '__main__':
    main()
