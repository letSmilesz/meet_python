import ui
import password

def start():
    n,m = ui.user_enter()
    ui.output_on_display('Your passwords: ', password.create_passwords(n, m))
    input()
