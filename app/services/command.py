from abc import ABC, abstractmethod

class TareaCommand:
    def __init__(self, tarea):
        pass

    @abstractmethod  
    def execute(self, model):
        pass

class Tarea(TareaCommand):
    def execute(self, model):
        for tarea in self._tarea:
            tarea.execute(model)

    def __init__(self):
        self._tarea = []

    def add_tarea(self, tarea):
        self._tarea.append(tarea)
