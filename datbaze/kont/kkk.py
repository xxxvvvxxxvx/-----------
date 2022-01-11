import gramatina

def kontaktu_piev():
  vards= input('kont vards:')
  numurs= input('kont num:')
  
  print(f'pievieno{vards}"ar numuru -{numurs}')

  gramatina.piev_kontaktu(vards, numurs)



def kont_atrasana():
  vards=input('kont vards')
  numurs= gramatina.atrod_kontaktu(vards)
  if numurs:
    print(f"{vards} numurs ir {numurs}")
  else:
    print(f"Izkstās, ka {vards} nav saraksta")

kont_atrasana()


def galvena_izv()
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
