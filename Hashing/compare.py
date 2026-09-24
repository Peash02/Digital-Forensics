import hashlib
filename = input("Enter the file name:")

try:
    with open(filename,"rb") as file:
        data = file.read()

    md5_hash = hashlib.md5(data).hexdigest()
    sha256_hash = hashlib.sha256(data).hexdigest()

    print("\nCurrent MD5 Hash:",md5_hash)
    print("\nCurrent SHA-256 Hash:",sha256_hash,"\n")

    original_hash = input("\nENter the original SHA-256 Hash:").strip()

    if sha256_hash == original_hash:
        print("\n Result : File is Unchanged.")
        print("Integrity Chechk Passed.")
    else:
        print("\n Result : File has been modified.")
        print("Integrity Check Failed.")

except FileNotFoundError:
    print("File Not Found. Please Check the file name.")

    