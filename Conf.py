from tkinter import filedialog
import tkinter.ttk as ttk
import tkinter as tk
import json

class WinConfig(tk.Toplevel):
	def __init__(self, parent):
		super().__init__(parent)

		self.initDict()

		self.estilos = ttk.Style()
		self.estilos.configure("Sub1.TLabel", background = "#f0f0f0")
		self.iconbitmap("./resources/configIco.ico")

		self.title("Configuración")
		self.resizable(False, False)
		self.protocol("WM_DELETE_WINDOW", self.guardarOpciones)

		self.frame = ttk.Frame(self)
		self.frame.pack(pady = 10, padx = 5)

		self.label = ttk.Label(self.frame, text = "Debe reiniciar el programa para los cambios de formato, mostrar y tema.", style = "Sub1.TLabel")
		self.label.pack(pady = 10)

		self.frame_general = ttk.Frame(self.frame)
		self.frame_general.pack(padx = 5)

		self.genHacer()
		self.genAjustes()

		self.apagadoWidgets()

	def genHacer(self):
		self.labelframe_hacer = ttk.LabelFrame(self.frame_general, text = "Hacer")
		self.labelframe_hacer.grid(row = 0, column = 0, padx = 5)

		self.genSonido()
		self.genMensaje()
		self.genAbrir()

	def genSonido(self):
		self.checkbutton_sonar_opcion = tk.IntVar()
		self.checkbutton_sonar_opcion.set(self.config_dict["Sonido"]["Sonar_Check"])

		self.radiobutton_sonido_opcion = tk.StringVar()
		self.radiobutton_sonido_opcion.set(self.config_dict["Sonido"]["Sonido_Radio"])

		self.checkbutton_loop_opcion = tk.IntVar()
		self.checkbutton_loop_opcion.set(self.config_dict["Sonido"]["Repetir_Check"])

		self.frame_sonar = ttk.Frame(self.labelframe_hacer, width = 270, height = 110)
		self.frame_sonar.pack()

		self.checkbutton_sonar = ttk.Checkbutton(self.frame_sonar, text = "Sonido", variable = self.checkbutton_sonar_opcion)
		self.checkbutton_sonar.place(x = 15, y = 5)
		self.checkbutton_sonar.bind('<1>', lambda event : self.eventoApagar("Sonido_Check", event = event))

		self.frame_checkbutton_sonar = ttk.Frame(self.frame_sonar, width = 222, height = 75)
		self.frame_checkbutton_sonar.place(x = 35, y = 30)

		self.checkbutton_loop = ttk.Checkbutton(self.frame_checkbutton_sonar, text = "Repetir sonido", variable = self.checkbutton_loop_opcion)
		self.checkbutton_loop.place(x = 0, y = 0)

		self.radiobutton_sonido_default = ttk.Radiobutton(self.frame_checkbutton_sonar, text = "Sonido por defecto", variable = self.radiobutton_sonido_opcion, value = "Default")
		self.radiobutton_sonido_default.place(x = 0, y = 26)
		self.radiobutton_sonido_default.bind('<1>', lambda event : self.eventoApagar("Sonido_Radio_Default", event = event))

		self.frame_sonido_custom = ttk.Frame(self.frame_checkbutton_sonar)
		self.frame_sonido_custom.place(x = 0, y = 50)

		self.radiobutton_sonido_custom = ttk.Radiobutton(self.frame_sonido_custom, text = "Sonido personalizado", variable = self.radiobutton_sonido_opcion, value = "Custom")
		self.radiobutton_sonido_custom.pack(side = tk.LEFT)
		self.radiobutton_sonido_custom.bind('<1>', lambda event : self.eventoApagar("Sonido_Radio_Custom", event = event))

		self.button_sonido_custom = ttk.Button(self.frame_sonido_custom, text = "Examinar", command = lambda : self.obtenerRuta("Sonido.Examinar"))
		self.button_sonido_custom.pack(padx = 5)

	def genMensaje(self):
		self.entry_mensaje_titulo_texto = tk.StringVar()
		self.entry_mensaje_titulo_texto.set(self.config_dict["Mensaje"]["Titulo_Entry"])
		
		self.entry_mensaje_mensaje_texto = tk.StringVar()
		self.entry_mensaje_mensaje_texto.set(self.config_dict["Mensaje"]["Mensaje_Entry"])
		
		self.radiobutton_mensaje_opcion = tk.StringVar()
		self.radiobutton_mensaje_opcion.set(self.config_dict["Mensaje"]["Mensaje_Radio"])

		self.checkbutton_mensaje_opcion = tk.IntVar()
		self.checkbutton_mensaje_opcion.set(self.config_dict["Mensaje"]["Mensaje_Check"])

		self.frame_mensaje = ttk.Frame(self.labelframe_hacer, width = 270, height = 146)
		self.frame_mensaje.pack(pady = 5)

		self.checkbutton_mensaje = ttk.Checkbutton(self.frame_mensaje, text = "Mensaje", variable = self.checkbutton_mensaje_opcion)
		self.checkbutton_mensaje.place(x = 15, y = 5)
		self.checkbutton_mensaje.bind('<1>', lambda event : self.eventoApagar("Mensaje_Check", event = event))

		self.frame_checkbutton_mensaje = ttk.Frame(self.frame_mensaje, width = 222, height = 111)
		self.frame_checkbutton_mensaje.place(x = 35, y = 30)

		self.radiobutton_mensaje_default = ttk.Radiobutton(self.frame_checkbutton_mensaje, text = "Mensaje por defecto", variable = self.radiobutton_mensaje_opcion, value = "Default")
		self.radiobutton_mensaje_default.place(x = 0, y = 0)
		self.radiobutton_mensaje_default.bind('<1>', lambda event : self.eventoApagar("Mensaje_Radio_Default", event = event))

		self.radiobutton_mensaje_custom = ttk.Radiobutton(self.frame_checkbutton_mensaje, text = "Mensaje personalizado", variable = self.radiobutton_mensaje_opcion, value = "Custom")
		self.radiobutton_mensaje_custom.place(x = 0, y = 25)
		self.radiobutton_mensaje_custom.bind('<1>', lambda event : self.eventoApagar("Mensaje_Radio_Custom", event = event))

		self.frame_mensaje_custom = ttk.Frame(self.frame_checkbutton_mensaje)
		self.frame_mensaje_custom.place(x = 22, y = 50)

		self.frame_mensaje_custom_titulo = ttk.Frame(self.frame_mensaje_custom)
		self.frame_mensaje_custom_titulo.grid(row = 0, column = 0, sticky = tk.E, pady = 5)

		self.entry_mensaje_custom_titulo = ttk.Entry(self.frame_mensaje_custom_titulo, textvariable = self.entry_mensaje_titulo_texto)
		self.entry_mensaje_custom_titulo.pack(side = tk.RIGHT)

		self.label_mensaje_custom_titulo = ttk.Label(self.frame_mensaje_custom_titulo, text = "Titulo", style = "Sub1.TLabel")
		self.label_mensaje_custom_titulo.pack(padx = 10)

		self.frame_mensaje_custom_mensaje = ttk.Frame(self.frame_mensaje_custom)
		self.frame_mensaje_custom_mensaje.grid(row = 1, column = 0, sticky = tk.E, pady = 5)

		self.entry_mensaje_custom_mensaje = ttk.Entry(self.frame_mensaje_custom_mensaje, textvariable = self.entry_mensaje_mensaje_texto)
		self.entry_mensaje_custom_mensaje.pack(side = tk.RIGHT)

		self.label_mensaje_custom_mensaje = ttk.Label(self.frame_mensaje_custom_mensaje, text = "Mensaje", style = "Sub1.TLabel")
		self.label_mensaje_custom_mensaje.pack(padx = 10)

	def genAbrir(self):
		self.checkbutton_abrir_opcion = tk.IntVar()
		self.checkbutton_abrir_opcion.set(self.config_dict["Abrir"]["Abrir_Check"])
		
		self.frame_abrir = ttk.Frame(self.labelframe_hacer, width = 270, height = 35)
		self.frame_abrir.pack(pady = 10)

		self.frame2_abrir = ttk.Frame(self.frame_abrir)
		self.frame2_abrir.place(x = 15, y = 5)

		self.checkbutton_abrir = ttk.Checkbutton(self.frame2_abrir, text = "Abrir", variable = self.checkbutton_abrir_opcion)
		self.checkbutton_abrir.pack(side = tk.LEFT)
		self.checkbutton_abrir.bind('<1>', lambda event : self.eventoApagar("Abrir_Check", event = event))

		self.button_abrir = ttk.Button(self.frame2_abrir, text = "Examinar", command = lambda : self.obtenerRuta("Abrir.Examinar"))
		self.button_abrir.pack(padx = 5)

	def genAjustes(self):
		self.frame_ajustes = ttk.Frame(self.frame_general)
		self.frame_ajustes.grid(row = 0, column = 1, pady = 5)

		self.genFormato()
		self.genMostrar()
		self.genTema()

	def genFormato(self):
		self.radiobutton_formato_opcion = tk.StringVar()
		self.radiobutton_formato_opcion.set(self.config_dict["Formato_Radio"])
		
		self.labelframe_formato = ttk.LabelFrame(self.frame_ajustes, text = "Formato de hora")
		self.labelframe_formato.grid(row = 0, column = 0, padx = 5)

		self.frame_radiobuttons_formato = ttk.Frame(self.labelframe_formato)
		self.frame_radiobuttons_formato.pack(side = tk.LEFT, padx = 7)

		self.radiobutton_larga = ttk.Radiobutton(self.frame_radiobuttons_formato, text = "Hora larga", variable = self.radiobutton_formato_opcion, value = "Larga")
		self.radiobutton_larga.grid(row = 0, column = 0, sticky = tk.W)

		self.radiobutton_corto = ttk.Radiobutton(self.frame_radiobuttons_formato, text = "Hora corta", variable = self.radiobutton_formato_opcion, value = "Corta")
		self.radiobutton_corto.grid(row = 1, column = 0, pady = 5, sticky = tk.W)

	def genMostrar(self):
		self.checkbutton_horas_opcion = tk.IntVar()
		self.checkbutton_horas_opcion.set(self.config_dict["Mostrar"]["Hora_Check"])
		
		self.checkbutton_minutos_opcion = tk.IntVar()
		self.checkbutton_minutos_opcion.set(self.config_dict["Mostrar"]["Minutos_Check"])
		
		self.checkbutton_segundos_opcion = tk.IntVar()
		self.checkbutton_segundos_opcion.set(self.config_dict["Mostrar"]["Segundos_Check"])

		self.labelframe_mostrar = ttk.LabelFrame(self.frame_ajustes, text = "Mostrar", width = 108, height = 99)
		self.labelframe_mostrar.grid(row = 1, column = 0, padx = 5, pady = 50)

		self.frame_checkbuttons_mostrar = ttk.Frame(self.labelframe_mostrar)
		self.frame_checkbuttons_mostrar.place(x = 7, y = 0)

		self.checkbutton_horas = ttk.Checkbutton(self.frame_checkbuttons_mostrar, text = "Horas", variable = self.checkbutton_horas_opcion)
		self.checkbutton_horas.grid(row = 0, column = 0, sticky = tk.W)

		self.checkbutton_minutos = ttk.Checkbutton(self.frame_checkbuttons_mostrar, text = "Minutos", variable = self.checkbutton_minutos_opcion)
		self.checkbutton_minutos.grid(row = 1, column = 0, pady = 5, sticky = tk.W)

		self.checkbutton_segundos = ttk.Checkbutton(self.frame_checkbuttons_mostrar, text = "Segundos", variable = self.checkbutton_segundos_opcion)
		self.checkbutton_segundos.grid(row = 2, column = 0, sticky = tk.W)

	def genTema(self):
		self.tema_opcion = tk.StringVar()
		self.tema_opcion.set(self.config_dict["Tema_Radio"])
		
		self.labelframe_tema = ttk.LabelFrame(self.frame_ajustes, text = "Tema", width = 108, height = 71)
		self.labelframe_tema.grid(row = 3, column = 0, padx = 5)

		self.frame_radiobuttons_tema = ttk.Frame(self.labelframe_tema)
		self.frame_radiobuttons_tema.place(x = 7, y = 0)

		self.radiobutton_claro = ttk.Radiobutton(self.frame_radiobuttons_tema, text = "Claro", variable = self.tema_opcion, value = "Claro")
		self.radiobutton_claro.grid(row = 0, column = 0, sticky = tk.W)

		self.radiobutton_oscuro = ttk.Radiobutton(self.frame_radiobuttons_tema, text = "Oscuro", variable = self.tema_opcion, value = "Oscuro")
		self.radiobutton_oscuro.grid(row = 1, column = 0, pady = 5, sticky = tk.W)

	def obtenerRuta(self, opcion):
		match opcion:
			case "Sonido.Examinar":
				self.sonido_path = filedialog.askopenfilename(
					title = "Selecciona un archivo de audio",
					filetypes = [("Audio Files", "*.mp3 *.wav")]
				)

			case "Abrir.Examinar":
				self.archivo_path = filedialog.askopenfilename(
					title = "Selecciona un archivo",
					filetypes = [("All files", "*.exe *.py *.xspf")]
				)

		if self.sonido_path == None:
			self.sonido_path = self.config_dict["Sonido"]["Sonido_Ruta"]

		if self.archivo_path == None:
			self.archivo_path = self.config_dict["Abrir"]["Archivo_Ruta"]

	def guardarOpciones(self):
		self.config_dict = {
			"Sonido": {
				"Sonar_Check": self.checkbutton_sonar_opcion.get(),
				"Repetir_Check": self.checkbutton_loop_opcion.get(),
				"Sonido_Radio": self.radiobutton_sonido_opcion.get(),
				"Sonido_Ruta": self.sonido_path
			},

			"Mensaje": {
				"Mensaje_Check": self.checkbutton_mensaje_opcion.get(),
				"Mensaje_Radio": self.radiobutton_mensaje_opcion.get(),
				"Titulo_Entry": self.entry_mensaje_titulo_texto.get(),
				"Mensaje_Entry": self.entry_mensaje_mensaje_texto.get()
			},

			"Abrir": {
				"Abrir_Check": self.checkbutton_abrir_opcion.get(),
				"Archivo_Ruta": self.archivo_path
			},

			"Mostrar": {
				"Hora_Check": self.checkbutton_horas_opcion.get(),
				"Minutos_Check": self.checkbutton_minutos_opcion.get(),
				"Segundos_Check": self.checkbutton_segundos_opcion.get()
			},

			"Formato_Radio": self.radiobutton_formato_opcion.get(),
			"Tema_Radio": self.tema_opcion.get()
		}

		with open("./resources/config.json", "w") as f:
			json.dump(self.config_dict, f, indent = 4)

		self.withdraw()

	def eventoApagar(self, opcion, event = None):
		match opcion:
			case "Sonido_Check":
				if not self.checkbutton_sonar_opcion.get():
					if len(self.button_sonido_custom.state()) != 0 and self.radiobutton_sonido_opcion.get() == "Custom":
						self.button_sonido_custom.config(state = "normal")

					self.checkbutton_loop.config(state = "normal")
					self.radiobutton_sonido_default.config(state = "normal")
					self.radiobutton_sonido_custom.config(state = "normal")

				else:
					self.button_sonido_custom.config(state = "disabled")
					self.checkbutton_loop.config(state = "disabled")
					self.radiobutton_sonido_default.config(state = "disabled")
					self.radiobutton_sonido_custom.config(state = "disabled")

			case "Sonido_Radio_Default":
				if self.radiobutton_sonido_default.state()[0] != 'disabled':
					self.button_sonido_custom.config(state = "disabled")

			case "Sonido_Radio_Custom":
				if self.radiobutton_sonido_custom.state()[0] != 'disabled':
					self.button_sonido_custom.config(state = "normal")
					
					
			case "Mensaje_Check":
				if not self.checkbutton_mensaje_opcion.get():
					if self.radiobutton_mensaje_opcion.get() == "Custom":
						self.entry_mensaje_custom_mensaje.config(state = "normal")
						self.entry_mensaje_custom_titulo.config(state = "normal")

					self.radiobutton_mensaje_default.config(state = "normal")
					self.radiobutton_mensaje_custom.config(state = "normal")

				else:
					self.entry_mensaje_custom_mensaje.config(state = "disabled")
					self.entry_mensaje_custom_titulo.config(state = "disabled")
					self.radiobutton_mensaje_default.config(state = "disabled")
					self.radiobutton_mensaje_custom.config(state = "disabled")

			case "Mensaje_Radio_Default":
				if self.radiobutton_mensaje_default.state()[0] != 'disabled':
					self.entry_mensaje_custom_titulo.config(state = "disabled")
					self.entry_mensaje_custom_mensaje.config(state = "disabled")

			case "Mensaje_Radio_Custom":
				if self.radiobutton_mensaje_custom.state()[0] != 'disabled':
					self.entry_mensaje_custom_titulo.config(state = "normal")
					self.entry_mensaje_custom_mensaje.config(state = "normal")

			case "Abrir_Check":
				if not self.checkbutton_abrir_opcion.get() == 1:
					self.button_abrir.config(state = "normal")

				else:
					self.button_abrir.config(state = "disabled")

	def apagadoWidgets(self):
		if self.checkbutton_sonar_opcion.get():
			if self.radiobutton_sonido_opcion.get() == "Custom":
				self.button_sonido_custom.config(state = "normal")

			else:
				self.button_sonido_custom.config(state = "disabled")

			self.checkbutton_loop.config(state = "normal")
			self.radiobutton_sonido_default.config(state = "normal")
			self.radiobutton_sonido_custom.config(state = "normal")

		else:
			self.button_sonido_custom.config(state = "disabled")
			self.checkbutton_loop.config(state = "disabled")
			self.radiobutton_sonido_default.config(state = "disabled")
			self.radiobutton_sonido_custom.config(state = "disabled")

		if self.config_dict["Mensaje"]["Mensaje_Check"]:
			if self.radiobutton_mensaje_opcion.get() != "Custom":
				self.entry_mensaje_custom_mensaje.config(state = "disabled")
				self.entry_mensaje_custom_titulo.config(state = "disabled")

			else:
				self.entry_mensaje_custom_mensaje.config(state = "enabled")
				self.entry_mensaje_custom_titulo.config(state = "enabled")

			self.radiobutton_mensaje_default.config(state = "normal")
			self.radiobutton_mensaje_custom.config(state = "normal")

		else:
			self.entry_mensaje_custom_mensaje.config(state = "disabled")
			self.entry_mensaje_custom_titulo.config(state = "disabled")
			self.radiobutton_mensaje_default.config(state = "disabled")
			self.radiobutton_mensaje_custom.config(state = "disabled")

		if self.checkbutton_abrir_opcion.get() == 1:
			self.button_abrir.config(state = "normal")

		else:
			self.button_abrir.config(state = "disabled")

	def initDict(self):
		self.config_dict = {}

		with open("./resources/config.json", "r") as f:
			self.config_dict = json.load(f)

		self.sonido_path = None if self.config_dict["Sonido"]["Sonido_Ruta"] == None else self.config_dict["Sonido"]["Sonido_Ruta"]
		self.archivo_path = None if self.config_dict["Abrir"]["Archivo_Ruta"] == None else self.config_dict["Abrir"]["Archivo_Ruta"]

def config():
	with open("./resources/config.json", "r") as f:
		configuracion = json.load(f)

	return configuracion

if __name__ == "__main__":
	def main():
		root = tk.Tk()
		root.withdraw()

		ventana = WinConfig(root)
		ventana.protocol("WM_DELETE_WINDOW", lambda : (ventana.guardarOpciones(), ventana.destroy(), root.destroy()))

		ventana.mainloop()
	
	main()