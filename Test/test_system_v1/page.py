# Page class for user-device interaction
# MicroPython version: v1.19.1 on 2022-06-18
# Espressif ESP32-WROOM-32

class Page:
    def __init__(self, icon, perl):
        self.icon = icon
        self.perl = perl
        self._dispinfoloader()
        self._buttonassigner()
    
    def _button(self, up=None, down=None, left=None, right=None, ok=None, back=None):
        self.button_up = up
        self.button_down = down
        self.button_left = left
        self.button_right = right
        self.button_ok = ok
        self.button_back = back
    
    def _disp(self, screen_upside=None, screen_downside=None, timer=None, scorer=None):
        self.screen_upside = screen_upside
        self.screen_downside = screen_downside
        self.timer = timer
        self.scorer = scorer
    
    def play(self):
        self._button(right=self.config,
                     ok=None)
        self._disp(screen_upside=self.icon.monster,
                   screen_downside=self.icon.right_ind,
                   timer="PLAy",
                   scorer="GAME")
    
    def config(self):
        self._button(left=self.play,
                     ok=self.config_intensity)
        self._disp(screen_upside=self.icon.tool,
                   screen_downside=elf.icon.left_ind,
                   timer="SEt ",
                   scorer="COnF")
    
    def config_intensity(self):
        self._button(right=self.config_sound,
                     ok=self.config_intensity_screen,
                     back=self.config)
        self._disp(screen_upside=self.icon.sun,
                  screen_downside=self.icon.right_ind,
                  timer="COnF",
                  scorer="Int ")
    
    def config_intensity_screen(self):
        self._button(right=self.config_intensity_timer,
                     up=)
    
    
        



