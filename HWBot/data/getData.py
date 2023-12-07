def getData(chatId: int)->str:
    #костыль(кусок говна)
    with open("./data/subjects.txt", "r") as subjects:
        #print(subjects.read().split())
        return subjects.read().split()

getData(4)