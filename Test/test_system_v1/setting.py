# Setting class for Operating configuration information
# MicroPython version: v1.19.1 on 2022-06-18
# Espressif ESP32-WROOM-32

class Setting:
    def __init__(self, json, filename):
        self.json = json
        self.filename = filename
        self.read()
    
    
    def read(self):
        try:
            with open(self.filename, "r") as file:
                self.info = self.json.load(file)
        except:
            self.default()
    
    
    def save(self):
        with open(self.filename, "w") as file:
            self.json.dump(self.info, file)
    
    
    def default(self):
        self.info = {
            "general":{
                "intensity":{
                    "screen":0,
                    "timer":0,
                    "scorer":0},
                "sound":1
                }
            }
        self.save()
    