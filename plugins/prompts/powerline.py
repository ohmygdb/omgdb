import gdb
from omgdb.ansi_color import color
unicode_triangle="\u25b6 "
powerline_triangle="\ue0b0"
ansi_quote="\xbb"
delimiter=">"

#There's a known issue where unicode strings do not render properly in tui.

# filename> thread ~> [pc:0xdeadbeef] > frame number > symbol

def prompt_fn(curr_prompt):
    delimiter=powerline_triangle
    return color.red+color.invert+"omgdb"+color.red+delimiter+color.reset
 
gdb.prompt_hook=prompt_fn
