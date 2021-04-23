alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
key = 'fghijklmnopqrstuvwxyzabcdABCDEFGHIJKLMNOPQRSTUVWXYZ '

print("Kelompok 31")
print("Nama Anggota 1   : Michelia Vadilla Verdianto (21120120120020)")
print("Nama Anggota 2   : Donny Ridwan Setiawan (21120120130083)")
print("Nama Anggota 3   : Muhammad Ghulam Abdul Nashr Umar (21120120120029)")
print("Nama Anggota 4   : Daniel Andhika Yudistya (21120120140048)")

def encrypt():
    for i in kalimat:
        count=0
        for j in alphabet:
            if i == j:
                print(key[count], end = "")
            count+=1
class user:
    def decrypt(self):
        for i in kalimat:
            count=0
            for j in key:
                if i == j:
                    print(alphabet[count], end ="")
                count+=1

pil=int(input("1. Enkripsi\n2. Dekripsi\n"))
print("Masukkan Pilihan: ")

if pil == 1 :
    kalimat = input('Masukan nama: ')
    encrypt()
elif pil == 2 :
    kalimat = input('Masukan kode: ')
    name = user()
    name.decrypt()