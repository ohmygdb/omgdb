import sys
import pathlib
# This makes sure we can import omgdb
thispath=pathlib.Path(__file__).parent.parent.resolve()
sys.path.append(str(thispath))
import omgdb
from omgdb.ansi_color import color

if(omgdb.print_motd):
    print(
''.join(
[color.green+"   __                 "+color.brwhite+"     /)/)"+  color.green+"  __   __ \n"+color.reset,
 color.green+"  / ')/               "+color.brwhite+"    ('.')"+  color.green+" /  ) /  )\n"+color.reset,
 color.green+" /  //_   .___   __  ,"+color.brwhite+"    / ><|"+  color.green+"/  / /--< \n"+color.reset,
 color.green+"(__// /   / / |_/ (_/ "+color.brwhite+"   C_(\"\")"+color.green+"__/_/___/ \n"+color.reset,
 color.green+"                  _/_ "+color.brwhite+"         "+  color.green+"          \n"+color.reset,
 color.green+"                 '/   "+color.brwhite+"         "+  color.green+"          \n"+color.reset]
    
))
