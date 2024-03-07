from misc.Info import ProgramInfo
import hashlib

def Hash(password: str, salt: str = "IceShell"):
    return hashlib.sha256((password + salt).encode("utf-8")).hexdigest()

class ConfigurationData:
    def __init__(self, userName="root", passwordHashed=Hash("root"), config={}):
        self.userName = userName
        self.passwordHashed = passwordHashed

        self.variables = []

        self.config = config
        self.phrase()
        if self.config is not {}:
            self.loadConfig(config)
        self.updateVarList()
    
    def phrase(self):
        # 设置config内容
        self.config = {
            "userName": self.userName,  # 设置用户名
            "passwordHashed": self.passwordHashed,  # 设置密码
            "lock": "0",
            "variables": self.variables,
        }
        self.updateVarList()

    def updateVarList(self):
        # self.variables设置为config的key
        self.variables = []
        for key in self.config.keys():
            self.variables.append(key)
        self.config["variables"] = self.variables
        
    
    def loadConfig(self, config):
        # 传入的config是configuration读取的key=value
        for key, value in config.items():
            self.config[key] = value
        return self.config
    
    def setKeyValue(self, key: str, value):
        # 设置key的值为value
        self.config[key] = value
    
    def __call__(self):
        return self.config
    
    def update_internal_attributes(self, key, value):
        if hasattr(self, key):
            setattr(self, key, value)

class Configuration:
    def __init__(self, configPath=ProgramInfo.basedir + "/tools/configure.conf", configurationData: ConfigurationData | None = None):
        self.__dict__['configPath'] = configPath
        if configurationData is None:
            self.readConfig(configPath)
        else:
            self.__dict__['config'] = configurationData
        self.save()
    
    def readConfig(self, configPath):
        # 数据格式：key=value
        # 读取配置文件，然后创建一个ConfigurationData数据，尝试填入数据
        try:
            with open(configPath, "r", encoding="utf-8") as f:
                config = f.read().split("\n")
                # 删除所有config为空或者没有等号在中间的行
                config = [line for line in config if "=" in line]
    
                config = {
                    key: value for key, value in [line.split("=") for line in config]
                }
                self.config = ConfigurationData(config=config)
        except FileNotFoundError as e:
            print(e)
            self.config = ConfigurationData()
        except Exception as e:
            print(e)
            self.config = ConfigurationData()
        
    
    def get(self, name):
        return self.config()[name]

    def __call__(self):
        return self.config()
    
    def __getattr__(self, name):
        if 'config' in self.__dict__:
            return self.__dict__['config']()[name]
        else:
            raise AttributeError(f"No such attribute: {name}")

    def __setattr__(self, name, value):
        if name in ['config', 'configPath'] or '_config' not in self.__dict__:
            self.__dict__[name] = value
        elif name in self.__dict__['config']():
            self.__dict__['config'].setKeyValue(name, value)
            self.__dict__['config'].update_internal_attributes(name, value)
        else:
            object.__setattr__(self, name, value)
    def save(self):
        with open(self.configPath, "w", encoding="utf-8") as f:
            for key, value in self.config().items():
                value = str(value)
                f.write(key + "=" + value + "\n")
                f.flush()

    def ifexist(self, configKey):
        if configKey in self.config():
            return True
        else:
            return False
        
    def set_value(self, key, value):
        if key in self.config():
            self.config.setKeyValue(key, value)
            self.config.update_internal_attributes(key, value)
        else:
            raise KeyError(f"No such configuration key: {key}")

