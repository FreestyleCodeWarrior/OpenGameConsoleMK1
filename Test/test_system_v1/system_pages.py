import system_functions as funcs
import system_icons as icons


class SettingPages:
    def setting_intro(self):
        self._button(left=self.game_intro,
                     ok=self.setting_intensity)
        self._disp(screen_upside=icons.tool(),
                   screen_downside=icons.indicator(left=True),
                   timer="SEt ",
                   scorer="COnF")


    def setting_intensity(self):
        self._button(right=self.setting_sound,
                     ok=self.setting_intensity_screen,
                     back=self.setting_intro)
        self._disp(screen_upside=icons.diode(),
                  screen_downside=icons.indicator(right=True),
                  timer="COnF",
                  scorer="Int ")


    def setting_intensity_screen(self):
        self._button(up=(self.perl.screen.intensity, (1,)),
                     down=(self.perl.screen.intensity, (0,)),
                     right=self.setting_intensity_timer,
                     back=self.setting_intensity)
        self._disp(screen_upside=icons.fill(),
                   screen_downside=icons.indicator(up=True, down=True, right=True),
                   timer="    ",
                   scorer="    ")


    def setting_intensity_timer(self):
        self._button(up=(self.perl.timer.intensity, (1,)),
                     down=(self.perl.timer.intensity, (0,)),
                     right=self.setting_intensity_scorer,
                     left=self.setting_intensity_screen,
                     back=self.setting_intensity)
        self._disp(screen_upside=icons.empty(),
                   screen_downside=icons.indicator(up=True, down=True, left=True, right=True),
                   timer="8888",
                   scorer="    ")


    def setting_intensity_scorer(self):
        self._button(up=(self.perl.scorer.intensity, (1,)),
                     down=(self.perl.scorer.intensity, (0,)),
                     left=self.setting_intensity_timer,
                     back=self.setting_intensity)
        self._disp(screen_upside=icons.empty(),
                   screen_downside=icons.indicator(up=True, down=True, left=True),
                   timer="    ",
                   scorer="8888")


    def setting_sound(self):
        self._button(up=(funcs.update_buzzer, (self.perl, False)),
                     down=(funcs.update_buzzer, (self.perl, True)),
                     left=self.setting_intensity,
                     right=self.setting_save,
                     back=self.setting_intro)
        self._disp(screen_upside=icons.speaker(),
                   screen_downside=icons.indicator(up=True, down=True, left=True, right=True),
                   timer="bEEP",
                   scorer="OFF " if self.perl.buzzer.mute else "On  ")


    def setting_save(self):
        self._button(up=(funcs.save_perl_state, (self.perl,)),
                     down=(funcs.restore_perl_state, (self.perl,)),
                     left=self.setting_sound,
                     back=self.setting_intro)
        self._disp(screen_upside=icons.disk(),
                   screen_downside=icons.indicator(up=True, down=True, left=True),
                   timer="SAUE",
                   scorer="COnF")


class GamePages:
    def game_intro(self):
        self._button(right=self.setting_intro,
                     ok=self.game_select)
        self._disp(screen_upside=icons.monster(),
                   screen_downside=icons.indicator(right=True),
                   timer="PLAy",
                   scorer="GAME")


    def game_select(self):
        pass


class Pages(SettingPages, GamePages):
    def __init__(self, perl):
        self.perl = perl
        self.game_intro()


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
                funcs.flip_screen(self.perl.screen, rows, cs)
        for driver, characters in ((self.perl.timer, timer), (self.perl.scorer, scorer)):
            if characters:
                funcs.flip_led_tubes(driver, characters)
