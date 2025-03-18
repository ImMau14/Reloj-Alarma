from resources.customWidgets import CusWidget
import tkinter.ttk as ttk
import tkinter as tk
from Conf import config

formato_hora_ = None
tema_ = None

def cargarConfig():
	global formato_hora_
	global tema_

	dict_conf = config()

	formato_hora_ = dict_conf["Formato_Radio"]
	tema_ = dict_conf["Tema_Radio"]

cargarConfig()

class Combo(ttk.Frame):
	def __init__(self, master, tema = tema_, formato_hora = formato_hora_, command1 = lambda : 1, command2 = lambda : 1):
		super().__init__(master)

		self.tema = tema
		self.formato_hora = formato_hora
		self.command1 = command1
		self.command2 = command2
		self.enabled = 1

		self.estilos = ttk.Style()
		self.estilos.configure("Sub.TLabel", background = "#f0f0f0" if self.tema == "Claro" else "#292929", foreground = "#000000" if self.tema == "Claro" else "#ffffff", font = ("Kanit", 10))

		self.label = ttk.Label(self, style = "Sub.TLabel")
		self.label.pack()

		self.label2 = ttk.Label(self.label, style = "Sub.TLabel")
		self.label2.pack()

		self.texto = ttk.Label(self.label2, text = "Ingrese la hora", style = "Sub.TLabel")
		self.texto.pack()

		self.label1 = ttk.Label(self.label2, style = "Sub.TLabel")
		self.label1.pack(pady = 10)

		self.spin1 = CusWidget.Spinbox(self.label1, rango = (1, 12) if self.formato_hora == "Corta" else (0, 23), tema = self.tema)
		self.spin1.grid(column = 0, row = 0, padx = 10)

		self.spin2 = CusWidget.Spinbox(self.label1, rango = (0, 59), tema = self.tema)
		self.spin2.grid(column = 1, row = 0, padx = 10)

		self.spin3 = CusWidget.Spinbox(self.label1, rango = (0, 59) if self.formato_hora == "Corta" else (0, 24), tema = self.tema)
		self.spin3.grid(column = 2, row = 0, padx = 10)

		if self.formato_hora == "Corta":
			self.slide = CusWidget.Slide(self.label1, tema = self.tema)
			self.slide.grid(column = 3, row = 0, padx = 10)

		self.boton = CusWidget.Button(self.label, ontext = "Iniciar", offtext = "Detener", command1 = lambda :(self.command1(), self.toggleAll()), command2 = lambda : (self.command2(), self.toggleAll()), tema = self.tema)
		self.boton.pack(pady = 5)

	def toggleAll(self):
		if self.enabled:
			self.spin1.setState('disabled')
			self.spin2.setState('disabled')
			self.spin3.setState('disabled')

			if self.formato_hora == "Corta":
				self.slide.setState('disabled')

		else:
			self.spin1.setState('normal')
			self.spin2.setState('normal')
			self.spin3.setState('normal')

			if self.formato_hora == "Corta":
				self.slide.setState('normal')

		self.enabled = True if not self.enabled else False

	def get(self, opcion):
		match opcion:
			case "Spinbox1":
				return self.spin1.get()

			case "Spinbox2":
				return self.spin2.get()

			case "Spinbox3":
				return self.spin3.get()

			case "Slide":
				return self.slide.get() if self.formato_hora == "Corta" else None
			
			case "State":
				return self.enabled

class Opciones(ttk.Frame):
	def __init__(self, master, tema = tema_, comconfig = lambda : 1, compregun = lambda : 1):
		super().__init__(master)

		self.tema = tema
		self.comconfig = comconfig
		self.compregun = compregun

		self.estilos = ttk.Style()
		self.estilos.configure("Sub2.TLabel", background = "#f0f0f0" if self.tema == "Claro" else "#292929")

		self.label = ttk.Label(self, style = "Sub2.TLabel")
		self.label.pack()

		self.config = CusWidget.Config(self.label, tema = self.tema, command = self.comconfig)
		self.config.pack(pady = 2)

		self.pregun = CusWidget.Pregun(self.label, tema = self.tema, command = self.compregun)
		self.pregun.pack(pady = 2)