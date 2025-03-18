from PIL import ImageTk, Image
import tkinter.ttk as ttk
import tkinter as tk
import datetime

class Button(ttk.Frame):
	# Recibe dos funciones, command1 para cuando está verde, y command2 para cuando está rojo.
	def __init__(self, master, ontext = "On", offtext = "Off", command1 = lambda : 1, command2 = lambda : 1, tema = "Claro", color = "Verde"):
		super().__init__(master, borderwidth = 0)

		self.config(width = 75, height = 27)

		self.label = ttk.Label(self)
		self.label.place(x = -2, y = -2)

		self.command1 = command1
		self.command2 = command2
		self.color = color
		self.ontext = ontext
		self.offtext = offtext
		self.tema = tema

		self.state = {
			"verde0": ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/boton_verde0.png")),
			"verde1": ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/boton_verde1.png")),
			"rojo0": ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/boton_rojo0.png")),
			"rojo1": ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/boton_rojo1.png")),
		}

		self.canvas_boton = tk.Canvas(self.label, cursor = "hand2", width = 75, height = 27, background = "#f0f0f0" if self.tema == "Claro" else "#292929")

		self.canvas_boton.bind('<Enter>', lambda event: self.resaltado("Verde", True, event = event))
		self.canvas_boton.bind('<1>', self.clic)
		self.canvas_boton.bind('<Leave>', lambda event: self.resaltado("Verde", False, event = event))
		self.canvas_boton.grid(row = 0, column = 0)
		self.canvas_boton.pack()

		self.resaltado("Verde", False)

	def clic(self, event):
		if self.color == "Verde":
			self.command1()

		if self.color == "Rojo":
			self.command2()

		self.resaltado("Clic", True)

	def resaltado(self, boton, estado, event = None):
		if boton == "Clic":
			self.color = "Verde" if not self.color == "Verde" else "Rojo"

		match self.color:
			case "Verde":
				try:
					self.canvas_boton.delete(self.rojo0)
				except:
					pass

				try:
					self.canvas_boton.delete(self.rojo1)
				except:
					pass

				if estado:
					try:
						self.canvas_boton.delete(self.verde0)
					except:
						pass

					self.verde1 = self.canvas_boton.create_image(39, 2, image = self.state["verde1"], anchor = tk.N)

				else:
					try:
						self.canvas_boton.delete(self.verde1)
					except:
						pass

					self.verde0 = self.canvas_boton.create_image(39, 2, image = self.state["verde0"], anchor = tk.N)

				try:
					self.canvas_boton.delete(self.rojo_texto)
				except:
					pass

				self.verde_texto = self.canvas_boton.create_text(39, 15, text = self.ontext, font = ("Kanit", 10), fill = "white")

			case "Rojo":
				try:
					self.canvas_boton.delete(self.verde0)
				except:
					pass

				try:
					self.canvas_boton.delete(self.verde1)
				except:
					pass

				if estado:
					try:
						self.canvas_boton.delete(self.rojo0)
					except:
						pass

					self.rojo1 = self.canvas_boton.create_image(39, 2, image = self.state["rojo1"], anchor = tk.N)
				else:
					try:
						self.canvas_boton.delete(self.rojo1)
					except:
						pass

					self.rojo0 = self.canvas_boton.create_image(39, 2, image = self.state["rojo0"], anchor = tk.N)

				try:
					self.canvas_boton.delete(self.verde_texto)
				except:
					pass

				self.rojo_texto = self.canvas_boton.create_text(39, 15, text = self.offtext, font = ("Kanit", 10), fill = "white")

	def toggle(self):
		self.resaltado("Clic", True)

class Spinbox(ttk.Frame):
	def __init__(self, master, rango = (0, 10), tema = "Claro", variable = None, state = 'normal'):
		super().__init__(master)

		self.config(width = 43, height = 24)
		self.min_value, self.max_value = rango[0], rango[1]
		self.tema = tema

		if variable == None:
			self.textovar = tk.IntVar()
		else:
			self.textovar = variable

		self.icons = {
			"entry_claro": ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/spinbox_entry_claro.png")),
			"entry_oscuro": ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/spinbox_entry_oscuro.png")),
			"flecha_arriba0": ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/spinbox_flechaarriba0.png")),
			"flecha_abajo0": ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/spinbox_flechaabajo0.png")),
			"flecha_arriba1": ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/spinbox_flechaarriba1.png")),
			"flecha_abajo1": ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/spinbox_flechaabajo1.png")),
			"flecha_arriba2": ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/spinbox_flechaarriba2.png")),
			"flecha_abajo2": ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/spinbox_flechaabajo2.png"))
		}

		self.label = ttk.Label(self)
		self.label.place(x = -2, y = -2)

		self.canvas = tk.Canvas(self.label, width = 43, height = 24, background = "#f0f0f0" if self.tema == "Claro" else "#292929")
		self.spinbox_entry = self.canvas.create_image(23, 14, image = self.icons["entry_claro"] if self.tema == "Claro" else self.icons["entry_oscuro"])
		self.canvas.pack()

		self.canvas.bind('<MouseWheel>', lambda event : (self.resaltado(event = event), self.motion("Arriba" if event.delta > 0 else "Abajo")))

		self.flecha_arriba0 = self.canvas.create_image(35, 9, image = self.icons["flecha_arriba0"])		
		self.flecha_abajo0 = self.canvas.create_image(35, 18, image = self.icons["flecha_abajo0"])
		self.flecha_arriba1 = self.canvas.create_image(35, 9, image = self.icons["flecha_arriba1"])
		self.flecha_abajo1 = self.canvas.create_image(35, 18, image = self.icons["flecha_abajo1"])
		self.flecha_arriba2 = self.canvas.create_image(35, 9, image = self.icons["flecha_arriba2"])
		self.flecha_abajo2 = self.canvas.create_image(35, 18, image = self.icons["flecha_abajo2"])

		self.canvas.tag_bind(self.flecha_arriba0, '<Enter>', lambda event : self.resaltado(boton = "Arriba", estado = True, event = event))
		self.canvas.tag_bind(self.flecha_arriba0, '<Leave>', lambda event : self.resaltado(boton = "Arriba", estado = False, event = event))

		self.canvas.tag_bind(self.flecha_abajo0, '<Enter>', lambda event : self.resaltado(boton = "Abajo", estado = True, event = event))
		self.canvas.tag_bind(self.flecha_abajo0, '<Leave>', lambda event : self.resaltado(boton = "Abajo", estado = False, event = event))

		self.canvas.tag_bind(self.flecha_arriba1, '<Enter>', lambda event : self.resaltado(boton = "Arriba", estado = True, event = event))
		self.canvas.tag_bind(self.flecha_arriba1, '<Leave>', lambda event : self.resaltado(boton = "Arriba", estado = False, event = event))
		self.canvas.tag_bind(self.flecha_arriba1, '<1>', lambda event : self.clic(boton = "Arriba", event = event))

		self.canvas.tag_bind(self.flecha_abajo1, '<Enter>', lambda event : self.resaltado(boton = "Abajo", estado = True, event = event))
		self.canvas.tag_bind(self.flecha_abajo1, '<Leave>', lambda event : self.resaltado(boton = "Abajo", estado = False, event = event))
		self.canvas.tag_bind(self.flecha_abajo1, '<1>', lambda event : self.clic(boton = "Abajo", event = event))

		for id_ in (self.flecha_arriba1, self.flecha_abajo1, self.flecha_arriba2, self.flecha_abajo2):
			self.canvas.itemconfig(id_, state = 'hidden')

		self.entry = tk.Entry(self.label, width = 2, font = ("Fira Code", 10), bd = 0, background = "#c5c5c5" if self.tema == "Claro" else "#181818", foreground = "#ffffff" if self.tema == "Oscuro" else "#000000", insertbackground = "#737373" if tema == "Oscuro" else "#ffffff", textvariable = self.textovar)
		self.canvas.create_window(14, 14, window = self.entry)
		self.entry.bind('<MouseWheel>', lambda event : (self.resaltado(event = event), self.motion("Arriba" if event.delta > 0 else "Abajo")))

		self.setState(state)

	def clic(self, boton = None, event = None):
		if boton == "Arriba":
			self.action(1)

		else:
			self.action(-1)
	
	def motion(self, boton = None, event = None):
		if boton == "Arriba":
			self.action(1)

		else:
			self.action(-1)

	def resaltado(self, boton = None, estado = None, event = None):
		if estado:
			match boton:
				case "Arriba":
					self.canvas.itemconfig(self.flecha_arriba1, state = 'normal')

				case "Abajo":
					self.canvas.itemconfig(self.flecha_abajo1, state = 'normal')

		else:
			match boton:
				case "Arriba":
					self.canvas.itemconfig(self.flecha_arriba1, state = 'hidden')

				case "Abajo":
					self.canvas.itemconfig(self.flecha_abajo1, state = 'hidden')
		
		if event.delta > 0:
			self.canvas.itemconfig(self.flecha_arriba1, state = 'normal')
			self.canvas.after(300, lambda : self.canvas.itemconfig(self.flecha_arriba1, state = 'hidden'))
		else:
			self.canvas.itemconfig(self.flecha_abajo1, state = 'normal')
			self.canvas.after(300, lambda : self.canvas.itemconfig(self.flecha_abajo1, state = 'hidden'))

	def action(self, numero):
		if (self.textovar.get() + numero) in range(self.min_value, self.max_value + 1):
			self.textovar.set(self.textovar.get() + numero)

	def get(self):
		if len(str(self.textovar.get())) < 2:
			formato = "0" + str(self.textovar.get())
		else:
			formato = str(self.textovar.get())

		return formato

	def setState(self, state):
		if state == 'disabled':
			self.entry.config(state = 'readonly', readonlybackground = "#c5c5c5" if self.tema == "Claro" else "#181818", foreground = "#aaaaaa" if self.tema == "Oscuro" else "#888888")

			for id_ in (self.flecha_arriba0, self.flecha_abajo0):
				self.canvas.itemconfig(id_, state = 'hidden')

			for id_ in (self.flecha_arriba2, self.flecha_abajo2):
				self.canvas.itemconfig(id_, state = 'normal')
			
			self.canvas.unbind('<MouseWheel>')
			self.entry.unbind('<MouseWheel>')
		
		else:
			self.entry.config(state = 'normal', readonlybackground = "#c5c5c5" if self.tema == "Claro" else "#181818", foreground = "#ffffff" if self.tema == "Oscuro" else "#000000")

			for id_ in (self.flecha_arriba0, self.flecha_abajo0):
				self.canvas.itemconfig(id_, state = 'normal')

			for id_ in (self.flecha_arriba2, self.flecha_abajo2):
				self.canvas.itemconfig(id_, state = 'hidden')

			self.canvas.bind('<MouseWheel>', lambda event : (self.resaltado(event = event), self.motion("Arriba" if event.delta > 0 else "Abajo")))
			self.entry.bind('<MouseWheel>', lambda event : (self.resaltado(event = event), self.motion("Arriba" if event.delta > 0 else "Abajo")))

class Reloj(ttk.Frame):
	def __init__(self, master, tema = "Claro", hora = "Corta", mostrar_hora = (True, True, True)):
		super().__init__(master)
		self.tema = tema
		self.hora = hora

		self.mostrar_hora = mostrar_hora
		self.config(width = 0, height = 70)

		self.style = ttk.Style()
		self.style.configure("TLabel", background = "#f0f0f0" if self.tema == "Claro" else "#292929")
		self.style.configure("Num.TLabel", foreground = "#1a6600" if tema == "Claro" else "#84c757", font = ("New Amsterdam", 48))
		self.style.configure("2P.TLabel", foreground = "#1a6600" if tema == "Claro" else "#527818", font = ("New Amsterdam", 30))
		self.style.configure("AMOrPM.TLabel", foreground = "#1a6600" if tema == "Claro" else "#84c757", font = ("New Amsterdam", 30))

		self.fondo = tk.Canvas(self, width = 240 if self.hora == "Corta" else 185, height = 70, background = "#f0f0f0" if self.tema == "Claro" else "#292929")
		self.fondo.config(width = 0)
		self.fondo.place(x = -2, y = -2)

		self.reloj = ttk.Label(self)
		self.reloj.place(x = 0, y = 0)

		self.mostrar(mostrar_hora[0], mostrar_hora[1], mostrar_hora[2])
		self.actualizar()

	def mostrar(self, hora, minutos, segundos):
		self.boolhora = hora
		self.boolminutos = minutos
		self.boolsegundos = segundos

		ancho = (0 if self.hora == "Larga" else 60) - 14
		n_x = 0
		n_9 = 0

		if self.boolhora:
			ancho += 56
			n_x += 1
			self.label_hora = ttk.Label(self.reloj, text = "00", style = "Num.TLabel")
			self.label_hora.pack(side = tk.LEFT)

		if self.boolhora and self.boolminutos:
			ancho += 9
			n_9 += 1
			self.label_doblepunto1 = ttk.Label(self.reloj, text = ":", style = "2P.TLabel")
			self.label_doblepunto1.pack(side = tk.LEFT)

		if self.boolminutos:
			ancho += 56
			n_x += 1
			self.label_minutos = ttk.Label(self.reloj, text = "00", style = "Num.TLabel")
			self.label_minutos.pack(side = tk.LEFT)

		if self.boolminutos and self.boolsegundos:
			ancho += 9
			n_9 += 1
			self.label_doblepunto2 = ttk.Label(self.reloj, text = ":", style = "2P.TLabel")
			self.label_doblepunto2.pack(side = tk.LEFT)

		if self.boolsegundos:
			ancho += 56
			n_x += 1
			self.label_segundos = ttk.Label(self.reloj, text = "00", style = "Num.TLabel")
			self.label_segundos.pack(side = tk.LEFT)

		if self.hora == "Corta":
			self.amorpm = ttk.Label(self)
			self.amorpm.place(x = (n_x * 56) + (n_9 * 9) + 4, y = 12)

			self.label_amorpm = ttk.Label(self.amorpm, text = "AA", style = "AMOrPM.TLabel")
			self.label_amorpm.pack()

		self.config(width = ancho + 10)
		self.fondo.config(width = ancho + 18)

	def obtenerHoraActual(self):
		hora_actual = datetime.datetime.now()

		match self.hora:
			case "Corta":
				if hora_actual.hour >= 0 and hora_actual.hour < 12:
					self.hora_actual = 12 if hora_actual.hour == 0 else hora_actual.hour
					self.amorpm_actual = "AM"

				else:
					self.hora_actual = 12 if hora_actual.hour == 12 else hora_actual.hour - 12
					self.amorpm_actual = "PM"

			case "Larga":
				self.hora_actual = hora_actual.hour

		self.minuto_actual = hora_actual.minute
		self.segundo_actual = hora_actual.second
	
	def formatearHora(self):
		if len(str(self.hora_actual)) < 2:
			self.hora_actual_formato = "0" + str(self.hora_actual)

		else:
			self.hora_actual_formato = self.hora_actual

		if len(str(self.minuto_actual)) < 2:
			self.minuto_actual_formato = "0" + str(self.minuto_actual)

		else:
			self.minuto_actual_formato = self.minuto_actual

		if len(str(self.segundo_actual)) < 2:
			self.segundo_actual_formato = "0" + str(self.segundo_actual)

		else:
			self.segundo_actual_formato = self.segundo_actual
	
	def actualizar(self):
		self.obtenerHoraActual()
		self.formatearHora()

		if self.boolhora:
			self.label_hora.config(text = self.hora_actual_formato)

		if self.boolminutos:
			self.label_minutos.config(text = self.minuto_actual_formato)

		if self.boolsegundos:
			self.label_segundos.config(text = self.segundo_actual_formato)

		if self.hora == "Corta":
			self.label_amorpm.config(text = self.amorpm_actual)

		self.after(1000, self.actualizar)

	def get(self, valor):
		match valor:
			case "h":
				formato = self.hora_actual

			case "m":
				formato = self.minuto_actual

			case "s":
				formato = self.segundo_actual

		if valor == "amorpm" and self.hora == "Corta":
			formato = self.amorpm_actual
		
		if valor == "amorpm" and self.hora == "Larga":
			formato = None
			return formato

		if len(str(formato)) < 2:
			formato = "0" + str(formato)
		else:
			formato = str(formato)
	
		return formato

class Config(ttk.Frame):
	def __init__(self, master, tema = "Claro", command = lambda : 1):
		super().__init__(master)

		self.config(width = 15, height = 15)

		self.tema = tema
		self.command = command

		self.icon = {
			"config_claro0" : ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/config_claro0.png")),
			"config_claro1" : ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/config_claro1.png")),
			"config_oscuro0" : ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/config_oscuro0.png")),
			"config_oscuro1" : ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/config_oscuro1.png"))
		}

		self.label = ttk.Label(self)
		self.label.place(x = -2, y = -2)

		self.canvas = tk.Canvas(self.label, width = 15, height = 15, background = "#f0f0f0" if self.tema == "Claro" else "#292929",  cursor = "hand2")
		self.canvas.pack()
		
		self.config0 = self.canvas.create_image(9, 9, image = self.icon["config_claro0"] if self.tema == "Claro" else self.icon["config_oscuro0"])
		self.config1 = self.canvas.create_image(9, 9, image = self.icon["config_claro1"] if self.tema == "Claro" else self.icon["config_oscuro1"])

		self.canvas.bind('<Enter>', lambda event: self.resaltado("Activo", event = event))
		self.canvas.bind('<1>', self.fun)
		self.canvas.bind('<Leave>', lambda event: self.resaltado("Inactivo", event = event))
		
		self.resaltado("Inactivo")

	def resaltado(self, estado, event = None):
		match estado:
			case "Activo":
				self.canvas.itemconfig(self.config0, state = 'hidden')
				self.canvas.itemconfig(self.config1, state = 'normal')

			case "Inactivo":
				self.canvas.itemconfig(self.config0, state = 'normal')
				self.canvas.itemconfig(self.config1, state = 'hidden')
	
	def fun(self, event):
		self.command()

class Pregun(ttk.Frame):
	def __init__(self, master, tema = "Claro", command = lambda : 1):
		super().__init__(master)

		self.config(width = 15, height = 15)

		self.tema = tema
		self.command = command

		self.icon = {
			"pregun_claro0" : ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/pregun_claro0.png")),
			"pregun_claro1" : ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/pregun_claro1.png")),
			"pregun_oscuro0" : ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/pregun_oscuro0.png")),
			"pregun_oscuro1" : ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/pregun_oscuro1.png"))
		}

		self.label = ttk.Label(self)
		self.label.place(x = -2, y = -2)

		self.canvas = tk.Canvas(self.label, width = 15, height = 15, background = "#f0f0f0" if self.tema == "Claro" else "#292929",  cursor = "hand2")
		self.canvas.pack()
		
		self.pregun0 = self.canvas.create_image(9, 9, image = self.icon["pregun_claro0"] if self.tema == "Claro" else self.icon["pregun_oscuro0"])
		self.pregun1 = self.canvas.create_image(9, 9, image = self.icon["pregun_claro1"] if self.tema == "Claro" else self.icon["pregun_oscuro1"])

		self.canvas.bind('<Enter>', lambda event: self.resaltado("Activo", event = event))
		self.canvas.bind('<1>', self.fun)
		self.canvas.bind('<Leave>', lambda event: self.resaltado("Inactivo", event = event))
		
		self.resaltado("Inactivo")

	def resaltado(self, estado, event = None):
		match estado:
			case "Activo":
				self.canvas.itemconfig(self.pregun0, state = 'hidden')
				self.canvas.itemconfig(self.pregun1, state = 'normal')

			case "Inactivo":
				self.canvas.itemconfig(self.pregun0, state = 'normal')
				self.canvas.itemconfig(self.pregun1, state = 'hidden')
	
	def fun(self, event):
		self.command()

class Slide(ttk.Frame):
	def __init__(self, master, ytext = "AM", btext = "PM", tema = "Claro", color = "Amarillo"):
		super().__init__(master)

		self.config(width = 43, height = 25)

		self.tema = tema
		self.ytext = ytext
		self.btext = btext
		self.color = color

		self.valor_ = None
		self.icons = {
			"slide_claro0": ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/slide_claro0.png")),
			"slide_claro1": ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/slide_claro1.png")),
			"slide_claro2": ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/slide_claro2.png")),
			"slide_claro3": ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/slide_claro3.png")),
			"slide_claro4": ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/slide_claro4.png")),
			"slide_claro5": ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/slide_claro5.png")),
			"slide_oscuro0": ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/slide_oscuro0.png")),
			"slide_oscuro1": ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/slide_oscuro1.png")),
			"slide_oscuro2": ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/slide_oscuro2.png")),
			"slide_oscuro3": ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/slide_oscuro3.png")),
			"slide_oscuro4": ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/slide_oscuro4.png")),
			"slide_oscuro5": ImageTk.PhotoImage(Image.open("./resources/customWidgets/fotos/slide_oscuro5.png")),
		}

		self.label = ttk.Label(self)
		self.label.place(x = -2, y = -2)

		self.canvas = tk.Canvas(self.label, width = 43, height = 25, background = "#f0f0f0" if self.tema == "Claro" else "#292929")

		self.slide0 = self.canvas.create_image(23, 14, image = self.icons["slide_claro0"] if self.tema == "Claro" else self.icons["slide_oscuro0"])
		self.slide2 = self.canvas.create_image(23, 14, image = self.icons["slide_claro2"] if self.tema == "Claro" else self.icons["slide_oscuro2"])
		self.slide4 = self.canvas.create_image(23, 14, image = self.icons["slide_claro4"] if self.tema == "Claro" else self.icons["slide_oscuro4"])
		self.amarillo_texto = self.canvas.create_text(34, 14, text = self.ytext, font = ("Kanit", 9), fill = "#000000")

		self.slide1 = self.canvas.create_image(23, 14, image = self.icons["slide_claro1"] if self.tema == "Claro" else self.icons["slide_oscuro1"])
		self.slide3 = self.canvas.create_image(23, 14, image = self.icons["slide_claro3"] if self.tema == "Claro" else self.icons["slide_oscuro3"])
		self.slide5 = self.canvas.create_image(23, 14, image = self.icons["slide_claro5"] if self.tema == "Claro" else self.icons["slide_oscuro5"])
		self.azul_texto = self.canvas.create_text(12, 14, text = self.btext, font = ("Kanit", 9), fill = "#000000")

		for id_ in (self.slide0, self.slide1, self.slide2, self.slide3, self.slide4, self.slide5, self.amarillo_texto, self.azul_texto):
			self.canvas.itemconfig(id_, state = 'hidden')

		self.resaltado(color = self.color, estado = 'normal', init = "Si")
		self.setState('normal')

	def resaltado(self, color = None, estado = None, clic = None, event = None, init = None):
		match color:
			case "Amarillo":
				match estado:
					case 'mouse':
						self.canvas.itemconfig(self.slide0, state = 'hidden')
						self.canvas.itemconfig(self.slide4, state = 'hidden')

						self.canvas.itemconfig(self.slide2, state = 'normal')

					case 'normal':
						self.canvas.itemconfig(self.slide2, state = 'hidden')
						self.canvas.itemconfig(self.slide4, state = 'hidden')

						self.canvas.itemconfig(self.slide0, state = 'normal')
						self.canvas.itemconfig(self.amarillo_texto, fill = "#000000")
					
					case 'disabled':
						self.canvas.itemconfig(self.slide0, state = 'hidden')
						self.canvas.itemconfig(self.slide2, state = 'hidden')

						self.canvas.itemconfig(self.slide4, state = 'normal')
						self.canvas.itemconfig(self.amarillo_texto, fill = "#676700")

			case "Azul":
				match estado:
					case 'mouse':
						self.canvas.itemconfig(self.slide1, state = 'hidden')
						self.canvas.itemconfig(self.slide5, state = 'hidden')

						self.canvas.itemconfig(self.slide3, state = 'normal')

					case 'normal':
						self.canvas.itemconfig(self.slide3, state = 'hidden')
						self.canvas.itemconfig(self.slide5, state = 'hidden')

						self.canvas.itemconfig(self.slide1, state = 'normal')
						self.canvas.itemconfig(self.azul_texto, fill = "#000000")

					case 'disabled':
						self.canvas.itemconfig(self.slide1, state = 'hidden')
						self.canvas.itemconfig(self.slide3, state = 'hidden')

						self.canvas.itemconfig(self.slide5, state = 'normal')
						self.canvas.itemconfig(self.azul_texto, fill = "#1a2559")

		if color == "Amarillo" and init != None:
			self.canvas.itemconfig(self.amarillo_texto, state = 'normal')
			self.valor_ = "AM"

		if color == "Azul" and init != None:
			self.canvas.itemconfig(self.azul_texto, state = 'normal')
			self.valor_ = "PM"

		if clic:
			if self.color == "Amarillo":
				self.color = "Azul"
				self.canvas.itemconfig(self.slide0, state = 'hidden')
				self.canvas.itemconfig(self.slide2, state = 'hidden')
				self.canvas.itemconfig(self.slide4, state = 'hidden')

				self.canvas.itemconfig(self.amarillo_texto, state = 'hidden')
				self.canvas.itemconfig(self.azul_texto, state = 'normal')

				self.canvas.itemconfig(self.slide3, state = 'normal')

				self.valor_ = "PM"

			else:
				self.color = "Amarillo"
				self.canvas.itemconfig(self.slide1, state = 'hidden')
				self.canvas.itemconfig(self.slide3, state = 'hidden')
				self.canvas.itemconfig(self.slide5, state = 'hidden')

				self.canvas.itemconfig(self.azul_texto, state = 'hidden')
				self.canvas.itemconfig(self.amarillo_texto, state = 'normal')

				self.canvas.itemconfig(self.slide2, state = 'normal')

				self.valor_ = "AM"

		self.canvas.pack()

	def get(self):
		return self.valor_

	def setState(self, opcion):
		match opcion:
			case 'disabled':
				self.resaltado(color = self.color, estado = 'disabled')

				try:
					self.canvas.unbind('<Enter>')
					self.canvas.unbind('<Leave>')
					self.canvas.unbind('<1>')
				except:
					pass

			case 'normal':
				self.resaltado(color = self.color, estado = 'normal')

				self.canvas.bind('<Enter>', lambda event : self.resaltado(color = self.color, estado = 'mouse', event = event))
				self.canvas.bind('<Leave>', lambda event : self.resaltado(color = self.color, estado = 'normal', event = event))
				self.canvas.bind('<1>', lambda event : self.resaltado(clic = True, event = event))