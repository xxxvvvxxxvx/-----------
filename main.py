import xx



def kontaktu_piev():
  vards= input('kont vards:')
  numurs= input('kont num:')
  
  print(f'pievieno{vards}"ar numuru -{numurs}')

  xx.piev_kontaktu(vards, numurs)



def kont_atrasana():
  vards=input('kont vards:')
  numurs= xx.atrod_kontaktu(vards)
  if numurs:
    print(f"{vards} numurs ir {numurs}")
  else:
    sakrit=xx.kont_meklesana(vards)
    if sakrit:
      for k in sakrit:
        print(f"{k}numurs ir {sakrit[k]}")
    print(f"Izkstās, ka {vards} nav saraksta")

def kontaktu_red():
  iepr_v=input("Vārdu rediģēt:")
  iepr_numurs=xx.atrod_kontaktu()

  if iepr_numurs:
    jaunais_v =input(f"KOnt rediģēt:")
    jaunais_n=input(f"kont numuru red:")

  if not jaunais_v:
    xx.mainit_numuru{iepr_v, jaunais_n}
  
  if not jaunais_n:
    jaunais_n=iepr_numurs

  else:
    xx.mainit_kontaktu(iepr_v, jaunais_v, jaunais_n)
    

    
kont_atrasana()


def galvena_izv():
    print(sakums)
    izvele = input("Tava izvēlētā darbība:")

    if izvele =="1":
      kontaktu_piev()
    elif izvele == "2":
      kont_atrasana()
    else:
      print("meiģini velreiz")

while True:
  galvena_izv()
  input("\nNospied Enter\n\n")

    