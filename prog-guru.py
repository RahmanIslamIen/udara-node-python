print('=*90')
print('Program Perhitungan Honor Guru Honorer')

banyak_guru = int(input('Masukkan jumlah guru: '))

for i in range(banyak_guru):
    nama_guru = input('Masukkan nama guru: ')
    jurusan = input('Masukkan jurusan (ipa/ips/smk): ')
    jam_kerja = int(input('Masukkan jam kerja: '))

    pokok = 0
    bonus = 0

    if jurusan == 'ipa':
        pokok += 20000
        if jam_kerja < 100:
            bonus += 0
        elif 100 <= jam_kerja < 150:
            bonus += 3500
        else:
            bonus += 5500
    elif jurusan == 'ips':
        pokok += 15000
        if jam_kerja < 100:
            bonus += 0
        elif 100 <= jam_kerja < 150:
            bonus += 3500
        else:
            bonus += 5500
    elif jurusan == 'smk':
        pokok += 17500
        if jam_kerja < 100:
            bonus += 0
        elif 100 <= jam_kerja < 150:
            bonus += 3500
        else:
            bonus += 5500

    total = (pokok + bonus) * jam_kerja
    print(f'Honor yang diterima oleh {nama_guru} dalam sebulan sebanyak: {total}')

    print()
