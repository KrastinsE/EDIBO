#! /usr/bin/python3.6

print("Ievadiet skaitli")
# a=2**2000000

#te ir trīs darbības - vērtības sagaidīšana, vērtības pārveidošana, piešķiršana
#argument  = input()
#int(argument)
#a = int(argument)

#pildot int(input()) "bez izmēģinājuma" programma var vienk. izlidot...
#tāpēc, lai "nelidotu", mēs izmantosim  try ... except ... finally konstrukciju
paziime = False
while not paziime:
#while paziime==False:     #visi trīs varianti ir derīgi
#while paziime!=True:
    try:
        a = int( input() )
        paziime = True
    except:
        print("Diemžēl cienījamais kāpost, to, kas ievadīts, nevar pārveidot par skaitli",\
          "par vesela tipa skaitli :(")
        print("Lūdzu, ievadi s_k_a_i_t_l_i vēlreiz")
#if (a ==int): print("a**100")
#ja jau ļoti gribās, tad var salīdzināt type(a) == int -> rezultāts būs True
if (a == 5):
    print(a**100)
    print("Aprēķins ir gatavs")
print("Šis teksts atrodas ārpus darbību bloka, tāpēc tas parādīsies jebkurā gad.")

#print ("Ievadāmai vērtībai jābūt skaitlim")
#b=a**100x
