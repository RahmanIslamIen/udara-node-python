class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Menambahkan data ke queue
def enqueue(queue, data):
    new_node = Node(data)
    if not queue.head:
        queue.head = new_node
    else:
        current = queue.head
        while current.next:
            current = current.next
        current.next = new_node

# Menghapus data dari queue
def dequeue(queue):
    if not queue.head:
        return None
    else:
        data = queue.head.data
        queue.head = queue.head.next
        return data

# Konversi karakter ke indeks yang sesuai (0-25) untuk 'a' sampai 'z'
def to_array(s):
    arr = []
    for c in s:
        if 'a' <= c <= 'z':
            arr.append(ord(c) - ord('a'))
        elif 'A' <= c <= 'Z':
            arr.append(ord(c) - ord('A'))
    return arr

# Enkripsi
def vigenere_cipher(teks_plaintext, kunci):
    linked_list = LinkedList()
    antrian = LinkedList()
    array_plaintext = to_array(teks_plaintext)
    array_kunci = to_array(kunci)
    i = 0
    for _ in array_plaintext:
        enqueue(antrian, array_plaintext[i])
        linked_list.append(array_plaintext[i])
        i += 1
        if i == len(array_plaintext):
            i = 0
    j = 0
    while not antrian.head is None:
        data = dequeue(antrian)
        # Melakukan enkripsi Vigenere
        if data + array_kunci[j] > 25:
            data += array_kunci[j] - 26
        else:
            data += array_kunci[j]
        print(chr(data + ord('a')), end="")
        j += 1
        if j == len(array_kunci):
            j = 0

# Dekripsi r
def vigenere_decipher(teks_ciphertext, kunci):
    linked_list = LinkedList()
    antrian = LinkedList()
    array_ciphertext = to_array(teks_ciphertext)
    array_kunci = to_array(kunci)
    i = 0
    for _ in array_ciphertext:
        enqueue(antrian, array_ciphertext[i])
        linked_list.append(array_ciphertext[i])
        i += 1
        if i == len(array_ciphertext):
            i = 0
    j = 0
    while not antrian.head is None:
        data = dequeue(antrian)
        # Melakukan dekripsi Vigenere
        if data - array_kunci[j] < 0:
            data = 26 + (data - array_kunci[j])
        else:
            data -= array_kunci[j]
        print(chr(data + ord('a')), end="")
        j += 1
        if j == len(array_kunci):
            j = 0

# Kode utama
print()
print('NB: Kode ini hanya mendukung cipher huruf; tidak mendukung cipher angka.')
print()
while True:
    print('Vigenere Cipher')
    print('=================================')
    print('1. Enkripsi')
    print('2. Dekripsi')
    print('3. Keluar')
    pilihan_menu = input('Pilih fitur yang ingin digunakan (1-3): ')
    if pilihan_menu == '1':
        teks_plaintext = input("Masukkan kata yang ingin dienkripsi: ")
        kunci = input("Masukkan kunci enkripsi: ")
        print(f'Hasil enkripsi dari kata "{teks_plaintext}" dengan kunci "{kunci}" adalah: ', end="")
        vigenere_cipher(teks_plaintext, kunci)
        print()
    elif pilihan_menu == '2':
        teks_ciphertext = input("Masukkan kata yang ingin didekripsi: ")
        kunci = input("Masukkan kunci dekripsi: ")
        print(f'Hasil dekripsi dari kata "{teks_ciphertext}" dengan kunci "{kunci}" adalah: ', end="")
        vigenere_decipher(teks_ciphertext, kunci)
        print()
    elif pilihan_menu == '3':
        print('Terima kasih telah menggunakan program Vigenere Cipher ini!')
        print()
        break
    else:
        print('Kode fitur yang anda input salah.')
    print()
