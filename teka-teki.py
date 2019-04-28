#-*- coding: utf-8 -*-
#>>>baris ke 1 adalah kode agar ASCII dapat dieksekusi dalam program
#   Kode warna


'''
april
lion
the
two
bell
'''


W  = '\033[0m'  # white (default)
R  = '\033[1;31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[1;33m' # orange
B  = '\033[1;34m' # blue
P  = '\033[1;35m' # purple
C  = '\033[1;36m' # cyan
Y  = '\033[1;33m' # yellow
GR = '\033[1;37m' # gray
conor = '\033[25m' #colour normal
kedip = '\033[05m'
gelap = '\033[02m' #Dark

import datetime
tm = datetime.datetime.now()

import os
os.system('clear')

def love ():
    print (R + "\033[02m                    --......................         --.....................                              ")
    print ("                  -.000000000000000000000000.      -.00000000000000000000000.                             ")
    print ("                 -.00000000000000000000000000.    -.0000000000000000000000000.                           ")
    print ("                -.0000000000000000000000000000.  -.000000000000000000000000000. " + 10 * " " + C + "\033[05m----------------\033[25m" + R                        )
    print ("               -.000000000000000000000000000000.-.00000000000000000000000000000. "+ 10 * " " + C + "\033[05m----------------\033[25m" + R                             )
    print ("               -.000000000000000000000000000000..000000000000000000000000000000."+ 10 * " " + O + "\033[05m>>.Created By INU\033[25m" + R                                                )
    print ("               -.00000000000000000000000000000000000000000000000000000000000000."  + 10 * " " + G + "\033[05m * .  '  *  .  o\033[25m" + R                      )
    print ("                -.0000000000000000000000000local-heart000000000000000000000000."  + 10 * " " + G + "\033[05m * o . 0  ,  . , \033[25m" + R                     )
    print ("                 -.0000000000000000000000000000000000000000000000000000000000."                          )
    print ("                  -.00000000000000000000000000000000000000000000000000000000."                           )
    print ("                   -.000000000000000000000000000000000000000000000000000000."                            )
    print ("                    -.0000000000000000000000000000000000000000000000000000."                             )
    print ("                     -.00000000000000000000000000000000000000000000000000."                              )
    print ("                      -.000000000000000000000000000000000000000000000000."                               )
    print ("                       -.0000000000000000000000000000000000000000000000."                               )
    print ("                        -.00000000000000000000000000000000000000000000.") + W + 10 * " " + Y + (tm.strftime("\033[05m/////%A, %d-%b-%Y\033[25m\033[02m") + R)
    print ("                          0  0000 0000000000000000000000 0000000    000"                                  )
    print ("                           o  0o  oooooooo . 000000000000.000000000..oo."                                  )
    print ("                          .  . o . oooooo     .  . ,   oooooooo ., oo                                  ")
    print ("                             .  0   .    .  . .        , .     .    .,                                  ")
    print ("                            ,,    .  ,      . ,     ..      . .       ,.                                "   )
    print (W)
    print ("\033[25m")

love()

#.........latihan membuat game.............#

#masukkan nama pemain

def character():

    print (P + "\nNama telah tersedia")
    print ("------------------------------------------------------------------" + W)
    bp1 = raw_input(R + "\n(ulangi)Masukkan nama kamu : ") + W
    print (Y + "\033[05m>>>\033[25mHalo player 1 sebagai ") + R + bp1 + W
    bp2 = raw_input(B + "\n(ulangi)Masukkan nama kamu : ") + W
    print (Y + "\033[05m>>>\033[25mHalo player 2 sebagai ") + B + bp2 + W
    if bp1 == bp2:
        character()
    else:
        print (G + "\nYour name has been saved ")

################################################################################
playern1 = raw_input(R + "\nMasukkan nama kamu : ") + W
print (Y + "\033[05m>>>\033[25mHalo player 1 sebagai ") + R + playern1 + W
playern2 = raw_input(B + "\nMasukkan nama kamu : ") + W
print (Y + "\033[05m>>>\033[25mHalo player 2 sebagai ") + B + playern2 + W

if playern1 == playern2:
    character()
else:
    print (G + "\nYour name has been saved ")


#banner

print  (G + "\033[05m *************************************************************************************** \033[25m")
print  ("\n█▀▄ ▄▀▄ █▄░█ ▀█▀ █░█ ▄▀▄ █░▄▀ █░█ █▄░▄█ █▀▀ █▄░█ ▄▀ ▄▀▄ █▀▀▄ ▀ █▀▄ ▀ █▀▀▄ ▀ █░▄▀ █░█")
print  ("█▀█ █▀█ █░▀█ ░█░ █░█ █▀█ █▀▄░ █░█ █░█░█ █▀▀ █░▀█ █░ █▀█ █▐█▀ █ █░█ █ █▐█▀ █ █▀▄░ █░█")
print  ("▀▀░ ▀░▀ ▀░░▀ ░▀░ ░▀░ ▀░▀ ▀░▀▀ ░▀░ ▀░░░▀ ▀▀▀ ▀░░▀ ░▀ ▀░▀ ▀░▀▀ ▀ ▀▀░ ▀ ▀░▀▀ ▀ ▀░▀▀ ░▀░")
print  ("\033[05m *************************************************************************************** \033[25m\n")

#alur cerita

print (W + 15 * " " + "Hai " + playern1 + " dan " + playern2 + ", Maaf mengganggu waktu kalian. Maafkan aku wahai detektif,aku lupa bahwa siapa sebenarnya diriku\nyang aku ingat hanya kedua namamu dan beberapa petunjuk yang ada di benakku.Hal yang aku ingat dari kalian : ")

#histo player1
print (R + "\n" + playern1 + " = Seseorang yang mempunyai kelebihan pada otaknya(Intellegence), anda mempunyai penalaran dan logika yang sangat baik.\n" + 4 * " " + "Setiap ada masalah,anda lebih mempercayai pemikiran dan pendapat yang logis dan sering kali menemukan kebenaran,namun anda terlalu kaku saat menganalogikan sesuatu dan dampaknya.\n")
#histo player2
print (B + "\n" + playern2 + " = Seseorang yang mempunyai kelebihan dalam berintuisi(Emotional), anda mempuyai perasaan dan pemahaman yang kuat tentang sesuatu(walau anda tidak mengetahuinya secara pasti),bahkan anda terkesan sabar.\n" + 4 * " " + "Setiap ada masalah,anda lebih mempercayai apa kata hati dan berdasarkan imajinasi anda serta lebih memilih untuk melihat kejadian yang akan terjadi,namun anda sangat ceroboh.\n")


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#insctructions-dengan-dictionary

soal = {1:{'1) Soal1':'cobalah menatap'},
        2:{'2) Soal2':'sang raja nan menakutkan'},
        3:{'3) Soal3':'jembatan diantara 2 kota'},
        4:{'4) Soal4':'dia pun tak sendiri'},
        5:{'5) Soal5':'lelb?'}}

for this, value in soal.items():
    print ("------------>>>> : ", this)

    for this2 in value:
        print (this2 + ' = ', value[this2])

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def soal1():

    print (P + "-" * 50 + W)
    print (kedip + G + '\n*.o,^ *' +  C + ' Even he was bright in the fourth time ' + G + '* ^,o.*\n' + conor)
    print ("1)" + 10 * " " + "Pada malam hari aku berjuang bersama sang surya,menerangi pekatnya malam\nhingga tak terasa,pada saat itu adalah hari bumi." + W)
    print (gelap + "///sepertinya kita disini membutuhkan anda "+ conor + B + playern2 + W)

    def jawab():

        jaw1 = raw_input(G + "Jawaban   :" + W)

        if jaw1 == "april":
            lompat = raw_input("\nIngin pindah ke level selanjutnya ?(y/n) : ")
            if lompat == "y":
                soal2()
            else:
                aksii()
        elif jaw1 == "(ganti)":
            aksii()
        else:
            print (P + "Sepertinya saya ragu ... ")
            print (" Jika ingin mengganti soal,tulis (ganti)")
            jawab()

    jawab()


def soal2():

    print (P + "-" * 50 + W)
    print (kedip + gelap + P + "\n</</</" + W + conor + O + "   A beautifull roar   "+ kedip + gelap + P + "\>\>\>" + W + conor)
    print (P + "2)" + 10 * " " + "Kamu tahu,bahwasanya komputer itu lebih menyukai angka daripada huruf ? \ncoba kita lihat apa yang tersembunyi dari angka ini :" + W)
    print (gelap + "///sepertinya kita membutuhkan anda "+ conor + R + playern1 + W + gelap + " cobalah sudut pandang yang lain " + conor + W)
    print ("\n41 kagna naknahatrep atres,3 igabid tapad gnay niales kagna nakgnalih\n" )
    print (" 1   4   12   8   7   100   68   25   ")
    print (" 2   5   50   89  43  215   9    86   ")
    print (" 10  98  71   15  53  19    691  38   ")
    print (" 11  13  14   16  61  41    31   11   ")
    #lion 12 9 15 14

    def jawab2():

        jaw2 = raw_input(gelap + "\n|||kode penulisan nya(1-2-3-4)" + conor + P + "\nJawaban   :" + W )

        if jaw2 == "12-9-15-14":
            print ("lanjutkan")
            last2 = raw_input(gelap + "\n|||kode penulisan nya(abcd)" + conor + W + "\nIngat kembali    : ")
            if last2 == "lion":
                lompat2 = raw_input("\nIngin pindah ke level selanjutnya ?(y/n) : ")
                if lompat2 == "y":
                    soal3()
                else:
                    aksii()
            elif last2 == "(ganti)":
                aksii()
            else:
                print (P + "Sepertinya saya ragu, dan kurasa hanya tinggal sedikit lagi.Ayo coba lagi " + R + playern1 + P + ' dan ' + B + playern2 + W)
                jawab2()
        elif jaw2 == "(ganti)":
            aksii()
        else:
            print (P + "Sepertinya saya ragu ... ")
            print (" Jika ingin mengganti soal,tulis (ganti)" + W)
            jawab2()

    jawab2()


def soal3():

    print (kedip + gelap + R + "\n                          Maaf,soal terkunci      ")
    print ("            Tapi percayalah pada hati,karena ia adalah kunci" + conor + W)
    print (gelap + "\n///Hmmmmm,sekarang apa lagi " + conor + W)


    def unlock():

        unlocked = raw_input("Buka kunci    :")

        if unlocked == "local-heart":
            print ("UNLOCKED!!!")
        elif unlocked =="(ganti)":
            aksii()
        else:
            print ("LOCKED")

            print (P + "\nSepertinya saya ragu ... ")
            print (" Jika ingin mengganti soal,tulis (ganti)" + W)
            unlock()
    unlock()

    print (P + "-" * 50 + W)
    print (kedip + C + " @@@@@ " + Y + "English is the " + P + "universal languange" + C + " @@@@@" + W)
    print (C + "\n3)" + 10 * " " + "Mana yang lebih masuk akal ?" + W)
    print (gelap + "///kurasa kalian mengetahuinya " + conor)
    print (gelap + C + "\n het \n eht \n the \n teh \n hte \n" + conor + W)


    def jawab3():

        jaw3 = raw_input(C + "Jawaban   :" + W)

        if jaw3 == "the":
            lompat3 = raw_input("\nIngin pindah ke level selanjutnya ?(y/n) : ")
            if lompat3 == "y":
                soal4()
            else:
                aksii()
        elif jaw3 == "(ganti)":
            aksii()
        else:
            print (P + "Sepertinya saya ragu ... ")
            print (" Jika ingin mengganti soal,tulis (ganti)" + W)
            jawab3()

    jawab3()


def soal4():

    print (P + "-" * 50 + W)
    print (kedip + gelap + R + "\n+++++" + W + conor + B + "   and even magnetism" + R +" is never alone   " + kedip + gelap + B + "-----" + W + conor)
    print (Y + "4)" + 10 * " " + "Dan di jalan ini,kukuatkan hatiku dan langkahku.Bahkan batang yang kuat tidak mampu berdiri sendiri tanpa bantuan akar.Kutub magnet yang memliki 2 sisi.\nBahkan semua yang ada disini memliki keterkaitan dan pasangan.sedarilah,aku 3 aksara dengan bahasa yang mendunia." + W)
    print (gelap + "///kurasa bahasa yang mendunia adalah bahasa inggris\n " + conor + W)

    def jawab4():

        jaw4 = raw_input(R + "Jawa" + B +"ban   :" + W)

        if jaw4 == "two":
            lompat4 = raw_input("\nIngin pindah ke level selanjutnya ?(y/n) : ")
            if lompat4 == "y":
                soal5()
            else:
                aksii()
        elif jaw4 == "(ganti)":
            aksii()
        else:
            print (P + "Sepertinya saya ragu ... ")
            print (" Jika ingin mengganti soal,tulis (ganti)" + W)
            jawab4()

    jawab4()



def soal5():

    print (P + "-" * 50 + W)
    print (kedip + gelap + G + "\n-_-_- " + W + conor + R + ' t' + Y + 'h' + G + 'e ' + C + 'b' + P + 'r' + R  + 'a' + Y + 'i' + G + 'n ' + C + 'o' + P + 'f ' + R + 't' + Y + 'h' + G + 'e ' + C + 'h' + P + 'e' + R + 'a' + Y + 'r' + G + 't ' + kedip + gelap + B + " -_-_-\n" + conor)
    print (R + "5)" + 10 * " " + "Aku memikirkan angka,antara 3 sampai 21,bisakah kamu menebak angka yang aku pikirkan  ? " + W)
    print (gelap + "\n///kuharap kalian bekerja sama pada level ini " + W + conor)


    def whoami():

        print (gelap + "///kode penulisan adalah jawaban dari (soal1soal2 soal3 soal4 soal5\ndan seingatku namaku 4 kata ) " + conor +  W)
        me = raw_input("\nJadi,siapakah aku   : ")

        if me == "aprillion the two bell":
            print ("Successed\n")

            #print (kedip + G + 20 * " " +"╔═╗╔═╗╔═╦╗║╬║╔╦╗╔═╗─║╚╗╔╦╗╔╗─╔═╗─║╚╗╠╣╔═╗╔═╦╗║═╣
            #║═╣║╬║║║║║╠╗║║╔╝║╬╚╗║╔╣║║║║╚╗║╬╚╗║╔╣║║║╬║║║║║╠═║
            #╚═╝╚═╝╚╩═╝╚═╝╚╝─╚══╝╚═╝╚═╝╚═╝╚══╝╚═╝╚╝╚═╝╚╩═╝╚═╝" + conor + W )

        elif me == "(ganti)":
            aksii()
        else:
            print (P + "\nSepertinya saya ragu ... ")
            print (" Jika ingin mengganti soal,tulis (ganti)" + W)
            whoami()



    def jawab52():

        print ("\n                    " + Y + "         o                                 ")
        print ("           0             _ /___\ _       " + R + kedip + "!!!                     " + conor)
        print ("          /          " + Y + "   /         \                                ")
        print ("         /             /           \                              ")
        print ("        /             /             \                             ")
        print ("       /             /_______________\                            ")
        print ("      /                      |                                   ")
        print ("                             @                                    ")
        print (W + gelap + "\n///sepertinya ini banyak di sekolah,namun kuyakin,pasti jawabannya berbahasa inggris" + conor + W)

        def jaw52():

            input52 = raw_input(R + 'J' + Y + 'a' + G + 'w' + C + 'a' + P + 'b' + R + 'a' + Y + 'n ' + G + 'u' + C + 't' + P + 'a' + R + 'm' + Y + 'a   : ' + W)

            if input52 == "bell":
                print ("That's right")

                end = raw_input("\nSudah menemukan semua jawabannya ?(y/n)  : ")

                if end == 'y':
                    whoami()

                else:
                    aksii()

            elif input52 == "(ganti)":
                aksii()
            else:
                print (P + "Sepertinya saya ragu ... ")
                print (" Jika ingin mengganti soal,tulis (ganti)" + W)
                jaw52()

        jaw52()

    def jawab5():

        jaw5 = raw_input(R + 'J' + Y + 'a' + G + 'w' + C + 'a' + P + 'b' + R + 'a' + Y + 'n'    ': ' + W)

        if jaw5 == '18':
            print ("next >>>  ")
            jawab52()
        elif jaw5 == "(ganti)":
            aksii()
        else:
            print (P + "Sepertinya saya ragu ... ")
            print (" Jika ingin mengganti soal,tulis (ganti)" + W)
            jawab5()

    jawab5()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#inputan user

def aksii():
    aksi = raw_input(Y + "\nBaik detektif, kita ingin ke petunjuk yang mana dulu ?\n(1,2,3,4,5)                             :  " + W)

    if aksi == '1':
        print ("OK, baiklah kita akan ke petunjuk " + aksi )
        soal1()
    elif aksi == '2':
        print ("OK, baiklah kita akan ke petunjuk " + aksi )
        soal2()
    elif aksi == '3':
        print ("OK, baiklah kita akan ke petunjuk " + aksi )
        soal3()
    elif aksi == '4':
        print ("OK, baiklah kita akan ke petunjuk " + aksi )
        soal4()
    elif aksi == '5':
        print ("OK, baiklah kita akan ke petunjuk " + aksi )
        soal5()
    else:
        print (P + "Maaf keyword yang anda masukkan salah " + W)
        aksii()

aksii()
