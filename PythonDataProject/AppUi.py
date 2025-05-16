from tkinter import *

janela = Tk()

window_width = 500
window_height = 500

widgets_width = 100
widgets_height = 100

container_width = 300
container_heigth = 300

entry_width = 15

entry_relative_x = (window_width/entry_width)/100

janela.geometry("{width}x{height}".format(width=window_width, height=window_height))

janela.update()

#widget container

container = Frame(janela)
container.pack(anchor=CENTER)
container.place(relx= 0.5, rely=0.5, anchor=CENTER)
#container.configure(bg = "#111111")

container_enter_button = Frame(janela)
container_enter_button.pack()
container_enter_button.place(relx=0.5, rely=0.65, anchor=CENTER)
enter_button = Button(container_enter_button, text="Sign In")
enter_button.pack(side=LEFT)

sign_up_button = Button(container_enter_button, text="Sign Up")
sign_up_button.pack(side=RIGHT)

example_label = Label(container, text="Bom dia! \n Digite suas credenciais\n")
example_label.pack(side=TOP)

#widget de login

login_widget = Frame(container)
login_widget.pack(anchor=CENTER)
Label(login_widget, text="Login:").pack(side=LEFT)
login_widget.config(width= 20, height= 20)

#entrada do widget de login

entry_login = Entry(login_widget)
entry_login.pack()
entry_login.config(width=15)
entry_login.config(font=("calibri",))
entry_login.config(justify=LEFT)

login_cred = entry_login.get()

#widget de senha

password_widget = Frame(container)
enter_button = Button(password_widget, text="Entrar")
password_widget.pack()
Label(password_widget, text="Senha:").pack(side=LEFT)
password_widget.config(width= 20, height= 20)
# password_widget.place(relx= 0.5, rely=0.5, anchor=CENTER)


#entrada do widget de senha

entry_password = Entry(password_widget)
entry_password.pack()
entry_password.config(font=("calibri",), justify=LEFT, width=15, show="*")

password_cred = entry_password.get()

janela.mainloop()