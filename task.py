class Task:
    def __init__(self, name: str, tiempo: int):
        self.name = name
        self.tiempo_total = tiempo
        self.tiempo_restante = tiempo
        self.executed = 0

    def update(self, quantum: int):
        """Actualiza el progreso de la tarea."""
        execution = min(quantum, self.tiempo_restante)
        self.executed += execution
        self.tiempo_restante -= execution

    def is_complete(self) -> bool:
        """Devuelve True si la tarea está completa, False en caso contrario."""
        return self.tiempo_restante <= 0

    def progress_bar(self):
        """Devuelve una cadena de texto que contiene la barra de progreso de la tarea."""
        porcentaje = (self.executed / self.tiempo_total) * 100
        barras = int(porcentaje // 2)  # Convertir el porcentaje en barras
        return f"\r{self.name:<10} [{barras * '#':<50}]"

    def __str__(self):
        """Devuelve el estado actual de la tarea."""
        return f"{self.progress_bar()} [{self.executed}/{self.tiempo_total}]"
