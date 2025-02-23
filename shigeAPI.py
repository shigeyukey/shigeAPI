
# https://github.com/shigeyukey/shigeAPI

from aqt import mw

class ShigeAPI():
    def __init__(self, new_attr_name:str):
        self.attr_name = "shigeAPI_" + new_attr_name

    def run(self):
        try:
            if hasattr(mw, self.attr_name):
                mw_addon_func = getattr(mw, self.attr_name)
                if callable(mw_addon_func):
                    mw_addon_func()
        except Exception as e:
            print(f"shigeAPI {self.attr_name} Error: {e}")

    def add(self, func):
        setattr(mw, self.attr_name, func)


# BreakTimer https://ankiweb.net/shared/info/174058935
start_break_timer = ShigeAPI("start_break_timer")

# Leaserboard https://ankiweb.net/shared/info/175794613
open_leaderboard = ShigeAPI("open_leaderboard")

