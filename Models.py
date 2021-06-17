class Users:
    def __init__(self):
        pass
    ### Variables
    __username = ""
    __password = ""
    __fname = ""
    __lname = ""
    __id = None
    __msg = ""
    ###

    ### Setters
    def setUsername(self, username):
        self.__username = username

    def setPassword(self, password):
        self.__password = password

    def setFname(self, fname):
        self.__fname = fname

    def setLname(self, lname):
        self.__lname = lname

    def setId(self, id):
        self.__id = id

    def setMessage(self, msg):
        self.__msg = msg
    ###

    ### Getters
    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password

    def getFname(self):
        return self.__fname

    def getLname(self):
        return self.__lname

    def getId(self):
        return self.__id

    def getMessage(self):
        return self.__msg
    ###


class Products:
    def __init__(self):
        pass
    ### Variables
    __name = ""
    __brand = ""
    __release_date = ""
    __display_size = ""
    __display_type = ""
    __cpu = ""
    __ram = ""
    __nocameras = ""
    __msg = ""
    ###

    ### Setters
    def setName(self, name):
        self.__name = name

    def setBrand(self, brand):
        self.__brand = brand

    def setReleaseDate(self, release_date):
        self.__release_date = release_date

    def setDisplaySize(self, display_size):
        self.__display_size = display_size

    def setDisplayType(self, display_type):
        self.__display_type = display_type

    def setCPU(self, cpu):
        self.__cpu = cpu

    def setRAM(self, ram):
        self.__ram = ram

    def setNoCameras(self, nocameras):
        self.__nocameras = nocameras

    def setMessage(self, msg):
        self.__msg = msg
    ###

    ### Getters
    def getName(self):
        return self.__name

    def getBrand(self):
        return self.__brand

    def getReleaseDate(self):
        return self.__release_date

    def getDisplaySize(self):
        return self.__display_size

    def getDisplayType(self):
        return self.__display_type

    def getCPU(self):
        return self.__cpu

    def getRAM(self):
        return self.__ram

    def getNoCameras(self):
        return self.__nocameras

    def getMessage(self):
        return self.__msg
    ###
