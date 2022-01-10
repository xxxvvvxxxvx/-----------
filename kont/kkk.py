import gramatina

def kontaktu_piev():
  vards= input('kont vards:')
  numurs= input('kont num:')
  
  print(f'pievieno{vards}"ar numuru -{numurs}')

  gramatina.piev_kontaktu(vards, numurs)

kontaktu_piev()

def kont_atrasana():
  vards=input('kont vards')
  numurs= gramatina.atrod_kontaktu(vards)
  if numurs:
    print(f"{vards} numurs ir {numurs}")
  else:
    print(f'izkatas, ka {vards} nav saraksta')