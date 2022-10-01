import random

# veľkosť n*n hracej plochy
n=int(input("Zadaj veľkosť hracej plochy: ")) 

# funkcia vygeneruje a vráti hraciu plochu, n musí byť nepárne a väčšie ako 3
# pre nedostatok predstavivosti vyzerá sachovnica rovnako ako na obrázku v zadaní
def gensachovnicu(n):  
    sachovnica=[]
    if n%2==0 or n<4:
        print('Treba zadať nepárne číslo väčšie ako 3')
    else:
        for riadok in range(n):
            sachovnicax=[]
            for stlpec in range(n):
                if riadok==((n-1)/2) and stlpec==((n-1)/2):
                    sachovnicax.append("X")
                elif riadok==0 and stlpec==((n-1)/2):
                    sachovnicax.append("*")
                elif riadok==((n-1)/2) and stlpec==0:
                    sachovnicax.append("*")
                elif riadok==((n-1)/2) and stlpec==n-1:
                    sachovnicax.append("*")
                elif riadok==n-1 and stlpec==((n-1)/2):
                    sachovnicax.append("*")
                elif riadok==((n-1)/2) :
                    sachovnicax.append("D")
                elif  stlpec==((n-1)/2):
                    sachovnicax.append("D")
                elif riadok==((n-1)/2)+1 or riadok==((n-1)/2)-1 or stlpec==((n-1)/2)+1 or stlpec==((n-1)/2)-1:
                    sachovnicax.append("*")
                else:
                    sachovnicax.append(" ")
            
            sachovnica.append(sachovnicax)
        return(sachovnica)


sachovnica=gensachovnicu(n)

# funkcia nakreslí hraciu plochu, každý zoznam vytlačí do samostatného riadku
def tlacsachovnicu(sachovnica): 
    for i in sachovnica:
        print(*i)

# hádzanie kockou pomocou knižnice random ktorú sme importovali na začiatku programu
# ak sa nám podarí hodiť šestku, hádžeme ešte raz
def hod_kockou():
    hod = random.randint(1,6)
    if hod%6==0:
        hod=hod+hod_kockou()
    return(hod)

# počiatočná pozícia panáčikov A a B
# vykreslíme ju na začiatku programu
sachovnica[0][int(n/2)+1]='A'
sachovnica[n-1][int(n/2)-1]='B'
tlacsachovnicu(sachovnica)


# pomocné premenné
stred = int((n-1)/2) 
riadok = 0 
stlpec = int(n/2)+1
x=0
riadokB = (n-1) 
stlpecB = int(n/2)-1
y=0

# pohyb panáčika A po šachovnici na základe našich hodov s kockou
# vždy keď sa panáčik dostane do domčeka automaticky sa posunie na jeho koniec
# panáčikovia budú chodiť až kým sa nezaplní domček
def kroky_panacika_A():
    global riadok
    global stlpec
    global x
    hodilsi=hod_kockou()
    print('Hráč A hodil číslo ',hodilsi)
    for i in range(hodilsi):
        if stlpec==n//2 and riadok==0 and sachovnica[riadok][stlpec]=='A':
            x=x+1
            sachovnica[riadok][stlpec] = "*"
            sachovnica[(n//2)-x][stlpec] = "A"
            break
        elif stlpec>=stred and riadok<(n-1) and sachovnica[riadok+1][stlpec]=='*' : #down  
            sachovnica[riadok+1][stlpec] = "A"
            riadok=riadok+1
            sachovnica[riadok-1][stlpec] = "*"
        elif stlpec<stred and riadok>0 and sachovnica[riadok-1][stlpec]=='*' : # up
            sachovnica[riadok-1][stlpec] = "A"
            riadok=riadok-1
            sachovnica[riadok+1][stlpec] = "*"
        elif riadok>=stred and sachovnica[riadok][stlpec-1]=='*': #left
            sachovnica[riadok][stlpec-1] = "A"
            stlpec=stlpec-1
            sachovnica[riadok][stlpec+1] = "*"
        elif riadok<stred and sachovnica[riadok][stlpec+1]=='*': #right
            sachovnica[riadok][stlpec+1] = "A"
            stlpec=stlpec+1
            sachovnica[riadok][stlpec-1] = "*"


    return tlacsachovnicu(sachovnica)                  
             
# Pohyb druhého panáčika
def kroky_panacika_B():
    global riadokB
    global stlpecB
    global y
    hodilsi=hod_kockou()
    print('Hráč B hodil číslo ',hodilsi)
    for i in range(hodilsi):
        if stlpecB==n//2 and riadokB==n-1 and sachovnica[riadokB][stlpecB]=='B':
            y=y+1
            sachovnica[riadokB][stlpecB] = "*"
            sachovnica[stred+y][stlpecB]='B'
            break
        if stlpecB<stred and riadokB<=n and riadokB!=0 and sachovnica[riadokB-1][stlpecB]=='*' : # up
            sachovnica[riadokB-1][stlpecB] = "B"
            riadokB=riadokB-1
            sachovnica[riadokB+1][stlpecB] = "*"
        elif stlpecB>=stred and riadokB<(n-1) and sachovnica[riadokB+1][stlpecB]=='*' : # down  
            sachovnica[riadokB+1][stlpecB] = "B"
            riadokB=riadokB+1
            sachovnica[riadokB-1][stlpecB] = "*"
        elif riadokB>=stred and sachovnica[riadokB][stlpecB-1]=='*': # left
            sachovnica[riadokB][stlpecB-1] = "B"
            stlpecB=stlpecB-1
            sachovnica[riadokB][stlpecB+1] = "*"
        elif riadokB<stred and sachovnica[riadokB][stlpecB+1]=='*': #right
            sachovnica[riadokB][stlpecB+1] = "B"
            stlpecB=stlpecB+1
            sachovnica[riadokB][stlpecB-1] = "*"
       
        
    return tlacsachovnicu(sachovnica)                                          



# funkcia pre pohyb všetkých panáčikov
# hra sa skončí keď bude jeden alebo druhý domček plný
def smer_domcek():
    print('______________________________________HRA______________________________________')
    while True:
        kroky_panacika_A()
        if sachovnica[1][n//2]=="A":
            print('Zvíťazil hráč A')
            break
        kroky_panacika_B()
        if sachovnica[n-2][n//2]=="B":
            print('Zvíťazil hráč B')
            break

smer_domcek()
