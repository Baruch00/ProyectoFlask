class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config): #Configurar servidor en MODO DEBUG (Desarrollo)
    DEBUG = True