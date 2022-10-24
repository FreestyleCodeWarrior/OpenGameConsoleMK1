# Page class for user-device interaction
# MicroPython version: v1.19.1 on 2022-06-18
# Espressif ESP32-WROOM-32

class Page:
    def __init__(self, icon, perl, funcs, json, sleep_ms, randint, Setting):
        self.icon = icon
        self.perl = perl
        self.funcs = funcs
        self.json = json
        self.sleep_ms = sleep_ms
        self.randint = randint
        self.Setting = Setting
        self.play()
    
    def _button(self, up=None, down=None, left=None, right=None, ok=None, back=None):
        for button, handler in (("up", up), ("down", down), ("left", left),
                           ("right", right), ("ok", ok), ("back", back)):
            if isinstance(handler, tuple):
                self.perl.buttons.assign(button, handler[0], handler[1])
            elif handler:
                self.perl.buttons.assign(button, handler)
            else:
                try:
                    del self.perl.buttons.handlers[button]
                except:
                    pass

    
    def _disp(self, screen_upside=None, screen_downside=None, timer=None, scorer=None):
        for rows, cs in ((screen_upside, 0), (screen_downside, 1)):
            if rows:
                self.funcs.flip_screen(self.perl.screen, rows, cs, self.sleep_ms)
        for driver, characters in ((self.perl.timer, timer), (self.perl.scorer, scorer)):
            if characters:
                self.funcs.flip_led_tubes(driver, characters, self.sleep_ms, self.randint)
        
    
    def play(self):
        self._button(right=self.config)
        self._disp(screen_upside=self.icon.monster(),
                   screen_downside=self.icon.indicator(right=True),
                   timer="PLAy",
                   scorer="GAME")
    
    def config(self):
        self._button(left=self.play,
                     ok=self.config_intensity)
        self._disp(screen_upside=self.icon.tool(),
                   screen_downside=self.icon.indicator(left=True),
                   timer="SEt ",
                   scorer="COnF")
    
    def config_intensity(self):
        self._button(right=self.config_sound,
                     ok=self.config_intensity_screen,
                     back=self.config)
        self._disp(screen_upside=self.icon.diode(),
                  screen_downside=self.icon.indicator(right=True),
                  timer="COnF",
                  scorer="Int ")
    
    def config_intensity_screen(self):
        self._button(up=(self.perl.screen.intensity, (1,)),
                     down=(self.perl.screen.intensity, (0,)),
                     right=self.config_intensity_timer,
                     back=self.config_intensity)
        self._disp(screen_upside=self.icon.fill(),
                   screen_downside=self.icon.indicator(up=True, down=True, right=True),
                   timer="    ",
                   scorer="    ")
    
    def config_intensity_timer(self):
        self._button(up=(self.perl.timer.intensity, (1,)),
                     down=(self.perl.timer.intensity, (0,)),
                     right=self.config_intensity_scorer,
                     left=self.config_intensity_screen,
                     back=self.config_intensity)
        self._disp(screen_upside=self.icon.empty(),
                   screen_downside=self.icon.indicator(up=True, down=True, left=True, right=True),
                   timer="8888",
                   scorer="    ")
    
    def config_intensity_scorer(self):
        self._button(up=(self.perl.scorer.intensity, (1,)),
                     down=(self.perl.scorer.intensity, (0,)),
                     left=self.config_intensity_timer,
                     back=self.config_intensity)
        self._disp(screen_upside=self.icon.empty(),
                   screen_downside=self.icon.indicator(up=True, down=True, left=True),
                   timer="    ",
                   scorer="8888")
    
    def config_sound(self):
        self._button(up=(self.funcs.update_buzzer, (self.perl, 1, self.sleep_ms, self.randint)),
                     down=(self.funcs.update_buzzer, (self.perl, 0, self.sleep_ms, self.randint)),
                     left=self.config_intensity,
                     right=self.config_save,
                     back=self.config)
        self._disp(screen_upside=self.icon.speaker(),
                   screen_downside=self.icon.indicator(up=True, down=True, left=True, right=True),
                   timer="bEEP",
                   scorer="OFF " if self.perl.buzzer.mute else "On  ")
    
    
    def config_save(self):
        self._button(up=(self.funcs.save_perl_state, (self.Setting, self.perl, self.json, self.sleep_ms, self.randint)),
                     down=(self.funcs.default_perl_state, (self.Setting, self.perl, self.json, self.sleep_ms, self.randint)),
                     left=self.config_sound,
                     back=self.config)
        self._disp(screen_upside=self.icon.disk(),
                   screen_downside=self.icon.indicator(up=True, down=True, left=True),
                   timer="SAUE",
                   scorer="COnF")
    
    
        



