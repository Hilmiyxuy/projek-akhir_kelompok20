import random

def tampilkan_papan(papan):
    print(f" {papan[0]} | {papan[1]} | {papan[2]} ")
    print("-----------")
    print(f" {papan[3]} | {papan[4]} | {papan[5]} ")
    print("-----------")
    print(f" {papan[6]} | {papan[7]} | {papan[8]} ")

def cek_menang(papan, pemain):
    # Cek baris
    for i in range(0, 9, 3):
        if papan[i] == papan[i+1] == papan[i+2] == pemain:
            return True
    # Cek kolom
    for i in range(3):
        if papan[i] == papan[i+3] == papan[i+6] == pemain:
            return True
    # Cek diagonal
    if papan[0] == papan[4] == papan[8] == pemain:
        return True
    if papan[2] == papan[4] == papan[6] == pemain:
        return True
    return False

def dapatkan_posisi_tersedia(papan):
    return [i for i, x in enumerate(papan) if x == ' ']

def dapatkan_langkah_komputer(papan, komputer):
    tersedia = dapatkan_posisi_tersedia(papan)
    
    # Cek apakah komputer bisa menang
    for pos in tersedia:
        papan[pos] = komputer
        if cek_menang(papan, komputer):
            papan[pos] = ' '
            return pos
        papan[pos] = ' '
    
    # Cek apakah pemain bisa menang, lalu blokir
    for pos in tersedia:
        papan[pos] = 'X'
        if cek_menang(papan, 'X'):
            papan[pos] = ' '
            return pos
        papan[pos] = ' '
    
    # Jika tidak ada menang atau blokir segera, pilih posisi tersedia secara acak
    return random.choice(tersedia)

def mainkan_game():
    print("=== Selamat Datang di Permainan Tic-Tac-Toe ===")
    
    # Pemilihan mode permainan
    while True:
        print("\nPilih Mode Permainan:")
        print("1. Bermain melawan teman")
        print("2. Bermain melawan komputer")
        pilihan = input("Masukkan pilihan Anda (1 atau 2): ")
        
        if pilihan in ['1', '2']:
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")
    
    # Inisialisasi papan permainan
    papan = [' '] * 9
    
    # Mulai permainan
    while True:
        tampilkan_papan(papan)
        
        # Giliran Pemain 1
        print("Giliran Pemain 1 (X):")
        try:
            posisi = int(input("Masukkan posisi (1-9): ")) - 1
            if posisi not in range(9) or papan[posisi] != ' ':
                print("Posisi tidak valid atau sudah diambil. Coba lagi.")
                continue
        except ValueError:
            print("Input tidak valid. Masukkan angka 1-9.")
            continue
        
        papan[posisi] = 'X'
        
        # Cek apakah Pemain 1 menang
        if cek_menang(papan, 'X'):
            tampilkan_papan(papan)
            print("Pemain 1 menang!")
            break
        
        # Cek apakah papan penuh (seri)
        if ' ' not in papan:
            tampilkan_papan(papan)
            print("Permainan seri!")
            break
        
        # Giliran Pemain 2
        if pilihan == '1':  # Bermain melawan teman
            print("Giliran Pemain 2 (O):")
            try:
                posisi = int(input("Masukkan posisi (1-9): ")) - 1
                if posisi not in range(9) or papan[posisi] != ' ':
                    print("Posisi tidak valid atau sudah diambil. Coba lagi.")
                    continue
            except ValueError:
                print("Input tidak valid. Masukkan angka 1-9.")
                continue
            papan[posisi] = 'O'
        else:  # Bermain melawan komputer
            posisi = dapatkan_langkah_komputer(papan, 'O')
            papan[posisi] = 'O'
            print(f"Komputer menempatkan O di posisi {posisi + 1}")
        
        # Cek apakah Pemain 2 menang
        if cek_menang(papan, 'O'):
            tampilkan_papan(papan)
            if pilihan == '1':
                print("Pemain 2 menang!")
            else:
                print("Komputer menang!")
            break
    
    # Tanyakan apakah ingin bermain lagi
    main_lagi = input("\nApakah Anda ingin bermain lagi? (ya/tidak): ").strip().lower()
    if main_lagi == 'ya':
        mainkan_game()
    else:
        print("Terima kasih telah bermain! Sampai jumpa.")

# Jalankan permainan
mainkan_game()