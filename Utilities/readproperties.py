import configparser

config = configparser.RawConfigParser()
config.read(".//Configurations/config.ini")

class readconfig:
    @staticmethod
    def ApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def Getusername():
        username=config.read('common info', 'username')
        return username

    @staticmethod
    def GetPassword():
        password=config.read('common info', 'password')
        return password
