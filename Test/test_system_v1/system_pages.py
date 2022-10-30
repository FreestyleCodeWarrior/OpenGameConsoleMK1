import system_functions as funcs
import system_icons as icons
import game_covers as covers

from game_pixelsnake_run import run as pixelsnake_run


class SettingPages:
    def setting_intro(self):
        funcs.roll_led_tubes(start=False)
        self._button(left=self.game_run,
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
    def game_run(self):
        if self.game_list.index(self.game_selected) == 0:
            ind_left = False
        else:
            ind_left = True
        
        self._button(up=self.game_records_intro,
                     down=self.game_clear_data,
                     left=(self.game_select, (-1,)),
                     right=(self.game_select, (1,)),
                     ok=self.game_selected[1])
        self._disp(screen_upside=self.game_selected[2](),
                   screen_downside=icons.indicator(up=True, down=True, left=ind_left, right=True),
                   timer="PLAy",
                   scorer=self.game_selected[3][:4])
        funcs.roll_led_tubes(self.perl.scorer, self.game_selected[3])
    
    
    def game_select(self, dirc):
        if self.game_list.index(self.game_selected) == 0 and dirc == -1:
            pass
        elif self.game_list.index(self.game_selected) == len(self.game_list) - 1 and dirc == 1:
            self.setting_intro()
        else:
            game_index = self.game_list.index(self.game_selected)
            self.game_selected = self.game_list[game_index + dirc]
            self.game_run()
    
    
    def game_clear_data(self):
        funcs.roll_led_tubes(start=False)
        self._button(up=self.game_run,
                     ok=(funcs.clear_game_data, (self.perl, self.game_selected[0])),
                     back=self.game_run)
        self._disp(screen_upside=icons.dustbin(),
                   screen_downside=icons.indicator(up=True),
                   timer="CLr ",
                   scorer="dAtA")
    
    
    def game_records_intro(self):
        funcs.roll_led_tubes(start=False)
        self._button(up=None,
                     down=self.game_run,
                     ok=(self.game_records_view, ("enter",)))
        self._disp(screen_upside=icons.histogram(),
                   screen_downside=icons.indicator(up=True, down=True),
                   timer="SEE ",
                   scorer="rECS")
    
    
    def game_records_view(self, i):
        if i == "enter":
            self.game_records = funcs.get_game_data(self.game_selected[0], "score records")
            self.perl.timer.segmode("7")
            i = 0
        elif i == "quit":
            del self.game_records
            self.perl.timer.segmode("8")
            self.game_records_intro()
            return None
        

        if not self.game_records:
            s_up = icons.numbers(i)
            s_down = icons.empty()
            timer = "no  "
            scorer = "rECS"
            b_up = b_down = None
            self.perl.timer.segmode("8")
        else:
            ind_up = ind_down = True
            b_up = (self.game_records_view, (i-1,))
            b_down = (self.game_records_view, (i+1,))
            if i == 0:
                ind_up = None
                b_up = None
            if i == len(self.game_records) - 1:
                ind_down = None
                b_down = None
            s_up = icons.numbers(i+1)
            s_down = icons.indicator(up=ind_up, down=ind_down)
            timer = self.game_records[i][0]
            scorer = self.game_records[i][1]
            
        self._button(up=b_up,
                     down=b_down,
                     back=(self.game_records_view, ("quit",)))
        self._disp(screen_upside=s_up,
                   screen_downside=s_down,
                   timer=timer,
                   scorer=scorer)
    


class Pages(SettingPages, GamePages):
    def __init__(self, perl):
        self.perl = perl
        self.game_list = (
            ("Pixel Snake",
             pixelsnake_run,
             covers.pixel_snake,
             "PIXEL SnAKE   "),
            )
        self.game_selected = self.game_list[0]
        self.game_run()


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
