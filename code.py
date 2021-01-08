import utils
import random

NAMES = utils.getNames()
EMAILS = utils.getEmails()
CITY = utils.getCity()
STATE = utils.getState()
PHONE = utils.getPhone()

DATAS_USERS = []

def shuffleDatas():
    random.shuffle(NAMES)
    random.shuffle(EMAILS)
    random.shuffle(CITY)
    random.shuffle(STATE)
    random.shuffle(PHONE)

def controller():
    utils.showProgramName()
    utils.line()
    # ---------------
    stop = False
    while stop == False:
        utils.menuOptions()
        shuffleDatas()
        optionUser = str(input('Selecione uma ou mais opções:'))
        optionUser = optionUser.split(',')
        for option in optionUser:
            if option == '1':
                DATAS_USERS.append(NAMES[0])
            elif option == '2':
                DATAS_USERS.append(EMAILS[0])
            elif option == '3':
                DATAS_USERS.append(CITY[0])
            elif option == '4':
                DATAS_USERS.append(STATE[0])
            elif option == '5':
                DATAS_USERS.append(PHONE[0])
            elif option == 'parar':
                stop = True

            else:
                print('Comando inválido, tente novamente')
        # ---------------
        if len(DATAS_USERS) != 0:
            utils.line()
            for datas in DATAS_USERS:
                print(datas)
            utils.line()
            while True:
                makeTxt = str(input('Deseja salvar as informações em um arquivo txt? (s/n)')).lower()[0]
                if makeTxt == 's':
                    with open('dados.txt', 'a') as attach:
                        for datas in DATAS_USERS:
                            attach.write(datas + '\n')
                        attach.write('-'*10 + '\n')
                    break
                elif makeTxt == 'n':
                    break

            DATAS_USERS.clear()
            utils.line()


if __name__ == "__main__":
    controller()