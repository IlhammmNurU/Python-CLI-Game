#Bismillahirrohmaanirrohiim

#write by ilham :)

'''

           D I C E
-------  -------  --------
Kubus yang mengubah segalanya

'''

#MODULUYANGDIBUTUHKAN
import random #<<< Untuk membuat bilangan acak
import os

#warna
W = '\033[0m' # white
R  = '\033[1;31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[1;33m' # orange
B  = '\033[1;34m' # blue
P  = '\033[1;35m' # purple
C  = '\033[1;36m' # cyan
Y  = '\033[1;33m' # yellow
GR = '\033[1;37m' # gray
conor = '\033[25m' #color normal
kedip = '\033[05m' #kedip-kedip ea:v
gelap = '\033[02m' #Dark

os.system('clear')

#-----------------              ALL CHARACTER            --------------------------------

dongtae = {"name":"\033[1;31mDongtae\033[0m", "skill":"Time Pause", "Attack":200, "HP":2000}

taebin = {"name":"\033[1;33mTaebin\033[0m", "skill":"Teleportation", "Attack":250, "HP":1500}

mio = {"name":"\033[1;32mMio\033[0m", "skill":"Clairvoyant", "Attack":200, "HP":1500}

eunjoo = {"name":"\033[1;34mEunjoo\033[0m", "skill":"Pyschokinesis", "Attack":500, "HP":1000}

#sprite
monster_1 = {"Name":"\033[1;31mMonster lvl 1", "Attack":50, "HP":200}
monster_2 = {"Name":"\033[1;33mMonster lvl 2", "Attack":100, "HP":500}
monster_3 = {"Name":"\033[1;35mBoss Monster", "Attack":300, "HP":2000}

monsterdb = {} #Database monster
player_select = {} # ini adalah tempat user memilih character

#------------------------ END --------------------------------------------------


#pemilihan karakter, ini awal
def select_player():
    os.system('clear')

    def options():
        #------- INI OPSI UNTUK MEMILIH -----------------------

        #---------------------------- 3] SERANG MINION --------------------------------------------------
        def launch_attack():
            os.system('clear')


            #-------------------------------------------------------

            def mons():
                print 'Sedang menyerang ... '
                monsterdb['HP'] -= player_select['Attack']
                print 'Memberikan damage ke ', monsterdb['Name'], W, ', sehingga HP nya menjadi ', R , monsterdb['HP'], W
                print P,'.    .   .   .   .   .   .   .   .   .\n',W

                def monsattack():
                    print 'Monster menyerang ...'
                    player_select['HP'] -= monsterdb['Attack']
                    print 'Anda telah menerima damage dari',monsterdb['Name'],R,'HP anda',player_select['HP'],W
                    print '>    >   >   >   >   >   >   >'

                    if player_select['HP'] <= 0:
                        print 'Anda telah kalah'
                        options()
                    else:
                        mons()

                if monsterdb['HP'] <= 0:
                    print W , 'Monster has dead', monsterdb['HP']
                    print 'Monster telah lumpuh oleh ' , player_select['name']
                    options()

                else:
                    monsattack()

                monsattack()


            #--------------------------------------------------------------

            print W ,'1] ' , monster_1['Name'] , '\n     HP = ' , monster_1['HP']
            print W ,'2] ' , monster_2['Name'] , '\n     HP = ' , monster_2['HP']
            print W ,'3] ' , monster_3['Name'] , '\n     HP = ' , monster_3['HP'] ,W

            #-----------------------------------------------------------
            def pilihan():
                #-----------------------()()()() -----------------
                def kondisi():

                    monselect = input("\nPilih yang mana    : ")
                    print'\n'

                    if monselect == 1:
                        monsterdb.update(monster_1)
                        mons()

                    elif monselect == 2:
                        monsterdb.update(monster_2)
                        mons()

                    elif monselect == 3:
                        monsterdb.update(monster_3)
                        mons()

                    else:
                        print P + "Maaf keyword yang anda masukkan salah " + W
                        launch_attack()

                #------------------------------()()()()() ---------------

                #-------------------------- <><><><><><>< ---------------
                def hpmin():
                    if player_select['HP'] == 0:
                        su = input('\n1]Ya\n2]Tidak\nHP anda telah habis, apakah anda ingin melanjutkan ?')
                        if su == 1:
                            kondisi()
                        elif su == 2:
                            options()
                        else:
                            print P,'Keyword yang anda masukkan salah',W
                            hpmin()

                    elif player_select['HP'] < 0:
                        options()
                    else:
                        kondisi()

                hpmin()
            #--------------------------------------------------------
            pilihan()
        #------------------- 4] LAWAN MOOYOUNG ------------------------------------------------------------
        def lawan_mooyoung():
            os.system('clear')

            #Mooyoung boss
            mooyoung = {'name':"\033[1;35mMooyoung\033[25m\033[0m", "Attack":1750, "HP":100000}

            print G,'=======================================================',W
            print " " * 15,'Nama     =',gelap,kedip,mooyoung['name'],W
            print " " * 15,'Serangan = ',Y, mooyoung['Attack'],W
            print " " * 15,'HP       = ',R, mooyoung['HP']
            print G,'=======================================================',W

            def attackloop():
                print '\nMencoba menyerang',mooyoung['name']
                mooyoung['HP'] -= player_select['Attack']
                print R,'HP',mooyoung['name'],'sekarang',R,mooyoung['HP']
                print '.    .   .   .   .   .   . \n'

                #-------------- beda haluan :v ------
                def countermooyoungloop():
                    print mooyoung['name'],'menyerang'
                    player_select['HP'] -= mooyoung['Attack']
                    print R,'HP',W,'anda sekarang',R,player_select['HP']

                    #------ beda haluan lagi -----
                    def again_co():

                        pilihan = input('\n1]Kembali ke options\n2]Keluar\nPilih yang mana      : ')
                        pilihan = int(pilihan)
                        if pilihan == 1:
                            options()
                        elif pilihan == 2:
                            os.system('exit')
                        else:
                            print P, 'Maaf keyword yang anda masukkan salah ',W
                            again_co()
                    #------ END -------

                    if player_select['HP'] <= 0:
                        print kedip, Y,'\n~~~~~~~~~~~~~~~'
                        print R,'Anda telah kalah ',W
                        print kedip, Y,'~~~~~~~~~~~~~~~', conor, W
                        again_co()

                    else:
                        attackloop()

                #------------- Awokowkkwowdwokd --------

                if mooyoung['HP'] <= 0:
                    print mooyoung['name'],'Telah mati'
                    print 'Selamat',player_select['name']

                    def again_co():

                        pilihan = input('\n1]Kembali ke options\n2]Keluar\nPilih yang mana      : ')

                        if pilihan == 1:
                            options()
                        elif pilhan == 2:
                            os.system('exit')
                        else:
                            print P, 'Maaf keyword yang anda masukkan salah ',W
                            again_co()

                    again_co()

                else:
                    countermooyoungloop()

                #------------- Awokowkkwowdwokd --------
            def yak():
                yakingan = raw_input('Anda yakin ingin menyerang mooyoung (y/n) ?        : ')
                if yakingan == 'y':
                    if player_select['HP'] <= 0:
                        print Y,"HP anda terlalu lemah, anda tidak akan bisa menyerang mooyoung",W
                        options()
                    else:
                        attackloop()
                elif yakingan == 'n':
                    options()
                else:
                    print P,"Keyword yang anda masukkan salah",W
                    yak()
                #--------------------------------------

            yak()

            attackloop()

        #-------------- ROLL THE DICE ---------------
        def roll():

            os.system('clear')

            #======== BEDA HALUAN =========
            def loopa():

                #-------------------------------------------INI BEDA GAN
                def terooz():
                    print G,'..............................................',W
                    qlagi = input('1]Gulir dadu lagi\n2]Kembali ke options\nPilih yang mana        : ')
                    qlagi = int(qlagi)
                    print G,'..............................................',W

                    if qlagi == 1:
                        roll()
                    elif qlagi == 2:
                        options()
                    else:
                        print P,"Keyword yang anda masukkan salah"
                        terooz()
                #------------------------------------------

                rdice = random.randint(1, 6)

                q = raw_input("\033[1;35mGulir Dadu    \033[0m(y/n)  : ")

                if q == 'y':
                    if rdice == 1:
                        print kedip,'Titik dadu yang keluar adalah 1',conor
                        player_select['HP'] += 50
                        print 'Sekarang', R, ' HP',W, 'anda menjadi', R,kedip, player_select['HP'], W,conor,'\n'
                        terooz()

                    elif rdice == 2:
                        print kedip,'Titik dadu yang keluar adalah 2',conor
                        player_select['Attack'] += 100
                        print 'Sekarang',Y, 'serangan',W, 'anda menjadi',Y,kedip, player_select['Attack'],W,conor,'\n'
                        terooz()

                    elif rdice == 3:
                        print kedip,'Titik dadu yang keluar adalah 3',conor
                        print 'Tidak ada efek apapun\n'
                        terooz()

                    elif rdice == 4:
                        print kedip,'Titik dadu yang keluar adalah 4',conor
                        player_select['HP'] += 200
                        print 'Sekarang', R, ' HP',W, 'anda menjadi', R,kedip, player_select['HP'], W,conor,'\n'
                        terooz()

                    elif rdice == 5:
                        print kedip,'Titik dadu yang keluar adalah 5',conor
                        print 'Tidak ada efek apapun\n'
                        terooz()

                    elif rdice == 6:
                        print '%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=' % (R, Y, G, B, R, Y, G, B, R, Y, G, B, R, Y, G, B, R, Y, G, B, R, Y, G, B, R, Y, G, B, R, Y, G, B),kedip
                        print " " * 5 ,'%s J %s A %s C %s K %s P %s O %s T' % (B, G, Y ,R, B, G, Y)
                        print P,'Titik dadu yang keluar adalah 6',conor
                        print '%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=%s=' % (R, Y, G, B, R, Y, G, B, R, Y, G, B, R, Y, G, B, R, Y, G, B, R, Y, G, B, R, Y, G, B, R, Y, G, B), W

                        player_select['HP'] += 1000
                        player_select['Attack'] += 500
                        print 'Sekarang',R, 'HP',W,'anda',R,kedip,player_select['HP'],conor,W,'dan',Y,'serangan',W,'anda',Y,kedip,player_select['Attack'],W,'\n'
                        terooz()

                    else:
                        print 'error reported'

                elif q == 'n':
                    options()

                else:
                    print P, "Maaf keyword yang anda masukkan salah ",W
                    loopa()


            loopa()


        # ------ END PROGRAM -------


        #----------------------------------------------------OPTIONS GAAAN     <<<<<<
        print W + '-----------------------------------------------OPTIONS-----'
        op = input("1]Gulir Dadu\n2]Lihat kemampuan karakter\n3]Serang Minion\n4]Lawan Mooyoung\n\n 5]Exit\n\nPilih yang mana      : ")
        print '-----------------------------------------------'

        #------------------------PEMILIHAN KONDISI------------------
        if op == 1:
            roll()

        #--------------------------2] Lihat kemampuan -------------------------

        elif op == 2:
            print " " * 10 , player_select['name']
            print 'Kemampuan kamu sekarang  : '
            print Y + 'Attack   = ' , player_select['Attack']
            print R + 'HP       = ' , player_select['HP'] , W
            options()

        # ------------------------- E N D --------------------------------------
        elif op == 3:
            launch_attack()

        elif op == 4:
            lawan_mooyoung()

        elif op == 5:
            select_player()

        else:
            print P + 'Maaf keyword yang anda masukkan salah ' + W
            os.system('clear')
            options()
    #------------------------------------------------------



    #---------------- HEADER -----------
    def rule_game():
        os.system('clear')
        print Y, "Hai Dicer " + player_select['name'] + Y + " Dice adalah alat yang mampu mengubah segalanya,\nSumber kekuatannya berada pada titik nya, semakin banyak titik\nyang keluar, Semakin banyak kekuatan yang bisa kau gunakan.\n" , W
        print kedip,G,'* . * . * . * . * . * . * . * . *'
        print R,' *          RULE GAME INI        *'
        print kedip,G,'* . * . * . * . * . * . * . * . *\n',W, conor

        print "1]Bermainlah secukupnya, ingat, jatuh di aspal tidak seindah jatuh cinta *hubungannya apa budjank :'v "
        print '2]Gulir dadu untuk mendapatkan Attack dan HP yang lebih besar,semakin besar angkanya, semakin bagus, namun ada yang zonk'
        print '3]Jika anda tidak bisa menyerang minion atau mooyoung, itu berarti HP anda kurang dari 0, gulir dadu dan dapatkan HP kembali'
        print '4]Mooyoung adalah musuh terkuat, Lawan dia selagi lemah 1!1!1!\n\n'

        print " " * 30 , kedip , G , 'Coded by ilham@localheart:~#' ,W , conor
        options()
    #---------------- END --------------

    #loop_chara_play
    player = {1:{R + '1) Dongtae' : 'Time Pause'},
              2:{Y + '2) Taebin' : 'Teleportation'},
              3:{G + '3) Mio' : 'Clairvoyant'},
              4:{B + '4) Eunjoo' : 'pyschokinesis'}}

    for loop, value in player.items():
        print ("<<<<<<<--------------------------->>>>>>>")
        for loop2 in value:
            print(loop2 + '\nSkillnya ' + value[loop2])

    print('\n' + W + kedip + '99) Keluar\n' + conor )

#-------------------------------------------------------------------------------

    global dongtae
    global taebin
    global mio
    global eunjoo

    #untukMenginputPilihanUserKeText


    select = input("Karakter apa yang akan kamu pilih ? : ")

    #Dongtae
    if select == 1 :
        print "\nKamu memilih" + R , dongtae['name'] , W
        print "Abilty : \n",Y + "Attack = " , dongtae['Attack'] , R ,"\nHP = " , dongtae['HP'] , W
        def again():
            go = raw_input("\nLanjut = y \nGanti = n \nJadi        : ")
            if go == "y":
                player_select.update(dongtae) #untuk mengupdate dictionary_a ke dictionary_b / yang telah ditentukan
                rule_game()
            elif go == "n":
                select_player()
            else:
                print(P + "Maaf keyword yang anda masukkan salah " + W)
                again()

        again()

    #Taebin
    elif select == 2 :
        print "\nKamu memilih" + Y , taebin['name'] , W
        print "Abilty : \n",P +"Attack = " , taebin['Attack'] , R , "\nHP = " , taebin['HP'] , W
        def again():
            go = raw_input("\nLanjut = y \nGanti = n \nJadi        : ")
            if go == "y":
                player_select.update(taebin)
                rule_game()
            elif go == "n":
                select_player()
            else:
                print(P + "Maaf keyword yang anda masukkan salah " + W)
                again()

        again()

    #Mio
    elif select == 3 :
        print "\nKamu memilih" + G , mio['name'] , W
        print "Abilty : \n",Y +"Attack = " , mio['Attack'] , R , "\nHP = " , mio['HP'] , W
        def again():
            go = raw_input("\nLanjut = y \nGanti = n \nJadi        : ")
            if go == "y":
                player_select.update(mio)
                rule_game()
            elif go == "n":
                select_player()
            else:
                print(P + "\nMaaf keyword yang anda masukkan salah " + W)
                again()

        again()

    #Eunjoo
    elif select == 4 :
        print "\nKamu memilih" + B , eunjoo['name'] , W
        print "Abilty : \n", Y +"Attack = " , eunjoo['Attack'] , R , "\nHP = " , eunjoo['HP'] , W
        def again():
            player_select.update(eunjoo)
            go = raw_input("\nLanjut = y \nGanti = n \nJadi        : ")
            if go == "y":
                rule_game()
            elif go == "n":
                select_player()
            else:
                print(P + "Maaf keyword yang anda masukkan salah " + W)
                again()

        again()

    elif select == 99:
        os.system('clear')
        os.system('exit')

    #etc
    else:
        print P , "Maaf keyword yang anda masukkan salah " , W
        select_player()

#RUN !!
def start():
    answer = raw_input("Mulai ?     (y/n) :  ")
    if answer == "y":
        select_player()
    elif answer == "n":
        os.system('exit')
        os.system('clear')
    else:
        print("Maaf Keyword yang anda masukkan salah ")
        start()

start()
