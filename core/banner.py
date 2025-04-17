from pystyle import Colors, Colorate

def admin_banner():
    banner = f"""
{Colors.red}
███████╗ █████╗ ███╗   ███╗██████╗ ██╗███╗   ███╗███████╗
██╔════╝██╔══██╗████╗ ████║██╔══██╗██║████╗ ████║██╔════╝
█████╗  ███████║██╔████╔██║██████╔╝██║██╔████╔██║█████╗  
██╔══╝  ██╔══██║██║╚██╔╝██║██╔═══╝ ██║██║╚██╔╝██║██╔══╝  
███████╗██║  ██║██║ ╚═╝ ██║██║     ██║██║ ╚═╝ ██║███████╗
╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝

            {Colors.green}==> Vampire-Admin-Access
         Coded by Muhammad Shourov (VAMPIRE)
"""
    return Colorate.Horizontal(Colors.red_to_yellow, banner, 2)

def user_banner():
    banner = f"""
{Colors.blue}
██╗   ██╗███████╗███████╗██████╗     ██╗   ██╗███████╗
██║   ██║██╔════╝██╔════╝██╔══██╗    ██║   ██║██╔════╝
██║   ██║█████╗  █████╗  ██████╔╝    ██║   ██║█████╗  
██║   ██║██╔══╝  ██╔══╝  ██╔═══╝     ╚██╗ ██╔╝██╔══╝  
╚██████╔╝███████╗███████╗██║          ╚████╔╝ ███████╗
 ╚═════╝ ╚══════╝╚══════╝╚═╝           ╚═══╝  ╚══════╝

        {Colors.green}==> Free-User-Access
      Author: Muhammad Shourov
      GitHub: https://github.com/vampiresquad
"""
    return Colorate.Horizontal(Colors.blue_to_cyan, banner, 2)
