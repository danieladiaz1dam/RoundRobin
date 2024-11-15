from time import sleep
from typing import List
import os
from task import Task



def round_robin(quantum: int, tasks: List[Task]):
    while len(tasks) > 0:
        # Tomamos la primera tarea en la cola
        current_task = tasks[0]

        # Ejecutar la tarea durante los quantums dados y actualizar el progreso
        current_task.update(quantum)

        # Imprimir el estado actual de la tarea
        print(current_task)

        # Si la tarea está completa, la eliminamos de la lista
        if current_task.is_complete():
            tasks.pop(0)

        # Si no está completa, la movemos al final de la cola
        else:
            tasks.append(tasks.pop(0))

        sleep(1)


if __name__ == '__main__':
    tasks_list = [
        Task("Word", 30),
        Task("Firefox", 15),
        Task("Discord", 25),
        Task("Spotify", 10),
    ]

    round_robin(5, tasks_list)
