class Logger:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Logger, cls).__new__(cls)
            cls._instancia.logs = []
        return cls._instancia

    def log(self, mensaje):
        self.logs.append(mensaje)

    def mostrar_logs(self):
        return self.logs
