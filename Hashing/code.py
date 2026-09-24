import hashlib
filename = input("Enter the file name:")

try:
    with open(filename,"rb") as file:
        data = file.read()

    md5_hash = hashlib.md5(data).hexdigest()
    sha256_hash = hashlib.sha256(data).hexdigest()

    print("\nMD5 Hash:",md5_hash)
    print("\nSHA-256 Hash:",sha256_hash,"\n")

except FileNotFoundError:
    print("File Not Found. Please Check the file name.")

    