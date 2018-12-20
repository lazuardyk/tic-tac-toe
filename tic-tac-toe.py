def papan(n, data):
    x=0
    for a in range(n):
      for q in range(n):
        print('+'+'-'*7, end='')
      print('+')
      for e in range(3):
        for w in range(n):
          if e==1:
            if len(str(data[x]))>1:
              print('|'+' '*2+str(data[x])+' '*3, end='')
              x +=1
            else:
              print('|'+' '*3+str(data[x])+' '*3, end='')
              x += 1
          else:
            print('|'+' '*7, end='')
        print('|')
    for r in range(n):
      print('+'+'-'*7, end='')
    print('+')

def welcome():
    print('Selamat datang di Tic Tac Toe!')
    n = 0
    while (n < 3):
        n = int(input('Ukuran yang diinginkan? (Contoh 3x3 ketik 3):'))
        
    return n

def cek_menang(papan, capx, n):
    if baris(papan, capx, n):
        return True
    if kolom(papan, capx, n):
        return True
    if diagonal_1(papan, capx, n):
        return True
    if diagonal_2(papan, capx, n):
        return True
    
def baris(data, capx, n):
    p = len(data)
    a = 0
    b = n
    c = n
    while a < p:
        if data[a:b] == list(capx*n):
            return True
        else:
            a+=c
            b+=c

def kolom(data, capx, n):
    p = len(data)
    a = 0
    while a < n:
        b = []
        for x in range(a,p,n):
            b.append(data[x])
        if b == list(capx*n):
            return True
        else:
            a+=1

def diagonal_1(data, capx, n):
    p = len(data)
    a = 0
    b = []
    for x in range(a, p, n+1):
        b.append(data[x])
    if b == list(capx*n):
        return True

def diagonal_2(data, capx, n):
    p = len(data)
    a = 0
    b = []
    for x in range(n-1, p-(n-1), n-1):
        b.append(data[x])
    if b == list(capx*n):
        return True

def cek_isi(papan, posisi):
    return (papan[posisi] != 'X') or (papan[posisi] != 'O')

def cek_full(papan):
    for i in range(1,10):
        if cek_isi(papan, i):
            return False
    return True

def main():
    n = welcome()
    data = [str(x+1) for x in range(n*n)]
    pemain1, pemain2 = ('X', 'O')
    mulai = True
    giliran = 'Pemain 1'
    while mulai:
        if giliran =='Pemain 1':
            papan(n,data)
            while True:
                posisi = int(input('Pemain 1 [X] Pilih Posisi:'))
                if str(posisi) not in data:
                    print('Posisi sudah direbut atau diluar dari angka permainan!')
                else:
                    data[posisi-1] = pemain1
                    break
            if cek_menang(data, pemain1, n):
                papan(n,data)
                print('Selamat! Pemain 1 Menang!')
                break
            else:
                if cek_full(data):
                    papan(n,data)
                    print('Permainan Seri!')
                    break
                else:
                    giliran = 'Pemain 2'
        else:
            papan(n,data)
            while True:
                posisi = int(input('Pemain 2 [O] Pilih Posisi:'))
                if str(posisi) not in data:
                    print('Posisi sudah direbut atau diluar dari angka permainan!')
                else:
                    data[posisi-1] = pemain2
                    break
            if cek_menang(data, pemain2, n):
                papan(n,data)
                print('Selamat! Pemain 2 Menang!')
                break
            else:
                if cek_full(data):
                    papan(n,data)
                    print('Permainan Seri!')
                    break
                else:
                    giliran = 'Pemain 1'           

do = True
while do:
    main()
    ul=input('Main lagi?(ya/tidak)')
    if ul.startswith('y'):
        do = True
    else:
        do = False
