import gdb
from omgdb.ansi_color import color
# A simple example of how to set a custom prompt in GDB
def prompt_fn(curr_prompt):
    return color.red+"omgdb> "+color.reset

gdb.prompt_hook=prompt_fn
