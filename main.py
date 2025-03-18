import tkinter.messagebox as msgbox
from resources.customWidgets import CusWidget
from Conf import WinConfig, config
import tkinter.ttk as ttk
from os import system
import tkinter as tk
import SubLabel
import datetime
import pygame

class Reloj(tk.Tk):
	def __init__(self):		
		super().__init__()
		self.title("Reloj Digital")
		self.geometry("438x259")
		self.resizable(False, False)
		self.iconbitmap("./resources/relojIco.ico")

		self.winconfig = None

		self.config_ = config()
		self.config(background = "#f0f0f0" if self.config_["Tema_Radio"] == "Claro" else "#292929")

		self.alarma_on = False

		self.estilo = ttk.Style()
		self.estilo.configure("TLabel", background = "#f0f0f0" if self.config_["Tema_Radio"] == "Claro" else "#292929")

		self.label = ttk.Label(self)
		self.label.pack(pady = 30)

		self.crearReloj()
		self.crearCombo()
		self.crearOpciones()

	def crearReloj(self):
		self.reloj = CusWidget.Reloj(self.label, tema = self.config_["Tema_Radio"], hora = self.config_["Formato_Radio"], mostrar_hora = (self.config_["Mostrar"]["Hora_Check"], self.config_["Mostrar"]["Minutos_Check"], self.config_["Mostrar"]["Segundos_Check"]))
		self.reloj.pack(pady = 10)

	def crearCombo(self):
		self.combo = SubLabel.Combo(self.label, command1 = self.onAlarma, command2 = self.offAlarma)
		self.combo.pack()

	def crearOpciones(self):
		self.opciones = SubLabel.Opciones(self, comconfig = self.openConfig, compregun = self.openInfo)
		self.opciones.place(x = 3, y = 2)

	def obtenerValores(self):
		self.hora = self.combo.get("Spinbox1")
		self.minuto = self.combo.get("Spinbox2")
		self.segundo = self.combo.get("Spinbox3")
		self.amorpm = self.combo.get("Slide")

	def prepararAlarma(self):
		self.obtenerValores()
		self.alarma()

	def alarma(self):
		self.config_ = config()

		if self.alarma_on:
			if self.amorpm == None:
				self.combo.texto.config(text = f"La alarma sonará a las {self.hora}:{self.minuto}:{self.segundo}.")
			else:
				self.combo.texto.config(text = f"La alarma sonará a las {self.hora}:{self.minuto}:{self.segundo} {self.amorpm}.")

			if self.hora == self.reloj.get("h") and self.minuto == self.reloj.get("m") and self.segundo == self.reloj.get("s") and (self.amorpm == self.reloj.get("amorpm") or self.amorpm == None):
				self.offAlarma()
				self.combo.boton.toggle()
				self.combo.toggleAll()
				self.hacer()

			evento = self.after(1000, self.alarma)

		else:
			self.combo.texto.config(text = "Ingrese la hora")

	def onAlarma(self):
		self.alarma_on = True
		self.prepararAlarma()

	def offAlarma(self):
		self.alarma_on = False

	def hacer(self):
		if self.config_["Sonido"]["Sonar_Check"]:
			pygame.init()
			sonido = self.config_["Sonido"]

			if sonido["Sonido_Radio"] == "Custom":
				pygame.mixer.music.load(sonido["Sonido_Ruta"])

			else:
				pygame.mixer.music.load("./resources/sonido_default.mp3")

			if sonido["Repetir_Check"]:
				pygame.mixer.music.play(-1, 0.0)

			else:
				pygame.mixer.music.play(1, 0.0)

		if self.config_["Mensaje"]["Mensaje_Check"]:
			mensaje = self.config_["Mensaje"]

			if mensaje["Mensaje_Radio"] == "Custom":
				msgbox.showinfo(mensaje["Titulo_Entry"], mensaje["Mensaje_Entry"])

			else:
				msgbox.showinfo("¡Ya es hora!", f"La alarma programada para las hora {self.hora}:{self.minuto}:{self.segundo} {self.amorpm} ha sonado.")

		if self.config_["Abrir"]["Abrir_Check"]:
			abrir = self.config_["Abrir"]
			system(abrir["Archivo_Ruta"])

	def openConfig(self):		
		if self.winconfig == None:
			self.winconfig = WinConfig(self)
			self.winconfig.protocol("WM_DELETE_WINDOW", lambda : (self.winconfig.guardarOpciones(), self.winconfig.withdraw()))

		if not self.winconfig.winfo_ismapped():
			self.winconfig.deiconify()

	def openInfo(self):
		msgbox.showinfo("Información del programa", "Este es un programa de Mau hecho con Tkinter. Sirve para programar alarmas, seleccionando la acción a realizar cuando llegue la hora.")

if __name__ == "__main__":
	root = Reloj()
	root.mainloop()