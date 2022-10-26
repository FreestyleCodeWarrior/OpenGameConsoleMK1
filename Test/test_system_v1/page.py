# Page class for user-device interaction
# MicroPython version: v1.19.1 on 2022-06-18
# Espressif ESP32-WROOM-32

class Page:
    def __init__(self, icons, perl, funcs, config, dump, load, sleep_ms, randint):
        self.icons = icons
        self.perl = perl
        self.funcs = funcs
        self.config = config
        self.dump = dump
        self.load = load
        self.sleep_ms = sleep_ms
        self.randint = randint
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
        self._button(right=self.setting)
        self._disp(screen_upside=self.icons.monster(),
                   screen_downside=self.icons.indicator(right=True),
                   timer="PLAy",
                   scorer="GAME")
    
    def setting(self):
        self._button(left=self.play,
                     ok=self.setting_intensity)
        self._disp(screen_upside=self.icons.tool(),
                   screen_downside=self.icons.indicator(left=True),
                   timer="SEt ",
                   scorer="COnF")
    
    def setting_intensity(self):
        self._button(right=self.setting_sound,
                     ok=self.setting_intensity_screen,
                     back=self.setting)
        self._disp(screen_upside=self.icons.diode(),
                  screen_downside=self.icons.indicator(right=True),
                  timer="COnF",
                  scorer="Int ")
    
    def setting_intensity_screen(self):
        self._button(up=(self.perl.screen.intensity, (1,)),
                     down=(self.perl.screen.intensity, (0,)),
                     right=self.setting_intensity_timer,
                     back=self.setting_intensity)
        self._disp(screen_upside=self.icons.fill(),
                   screen_downside=self.icons.indicator(up=True, down=True, right=True),
                   timer="    ",
                   scorer="    ")
    
    def setting_intensity_timer(self):
        self._button(up=(self.perl.timer.intensity, (1,)),
                     down=(self.perl.timer.intensity, (0,)),
                     right=self.setting_intensity_scorer,
                     left=self.setting_intensity_screen,
                     back=self.setting_intensity)
        self._disp(screen_upside=self.icons.empty(),
                   screen_downside=self.icons.indicator(up=True, down=True, left=True, right=True),
                   timer="8888",
                   scorer="    ")
    
    def setting_intensity_scorer(self):
        self._button(up=(self.perl.scorer.intensity, (1,)),
                     down=(self.perl.scorer.intensity, (0,)),
                     left=self.setting_intensity_timer,
                     back=self.setting_intensity)
        self._disp(screen_upside=self.icons.empty(),
                   screen_downside=self.icons.indicator(up=True, down=True, left=True),
                   timer="    ",
                   scorer="8888")
    
    def setting_sound(self):
        self._button(up=(self.funcs.update_buzzer, (self.perl, False, self.sleep_ms, self.randint)),
                     down=(self.funcs.update_buzzer, (self.perl, True, self.sleep_ms, self.randint)),
                     left=self.setting_intensity,
                     right=self.setting_save,
                     back=self.setting)
        self._disp(screen_upside=self.icons.speaker(),
                   screen_downside=self.icons.indicator(up=True, down=True, left=True, right=True),
                   timer="bEEP",
                   scorer="OFF " if self.perl.buzzer.mute else "On  ")
    
    
    def setting_save(self):
        self._button(up=(self.funcs.save_perl_state, (self.config, self.perl, self.dump, self.sleep_ms, self.randint)),
                     down=(self.funcs.restore_perl_state, (self.config, self.perl, self.dump, self.load, self.sleep_ms, self.randint)),
                     left=self.setting_sound,
                     back=self.setting)
        self._disp(screen_upside=self.icons.disk(),
                   screen_downside=self.icons.indicator(up=True, down=True, left=True),
                   timer="SAUE",
                   scorer="COnF")
    
    
        




