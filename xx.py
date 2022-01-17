from replit import db

def piev_kontaktu(vards, tel_nr):
  if vards in db:
    print('Kontakts ji pievienots')
  else:
    db[vards]=tel_nr
    print(f'Pievienots:{vards}:{tel_nr}')

def atrod_kontaktu(vards):
  numurs =db.get(vards)
  return numurs

def kont_meklesana(simbols):

  meklet =db.prefix(simbols)
  return {k: db[k]for k in meklet}

def mainit_numuru (iepr_v, jaunais_n):
  db[iepr_v]=jaunais_n



def mainit_kontaktu(iepr_v, jaunais_v, jaunais_n):
  db[jaunais_v] = jaunais_n

  del db[iepr_v]

  
