# паттерн Команда (Указание)

from abc import ABC, abstractmethod

class Computer:

    def __init__(self, model: str):
        self.model = model

    def run_code(self, language: str):
        print(f'PC {self.model} is runnng program in {language} programming language')

    def stop(self):
        print('PK stopped running program')
    
class Command(ABC):
    def __init__(self, pc: Computer):
        self.pc = pc

    @abstractmethod
    def execute(self) -> None:
        pass

    def unexecute(self) -> None:
        pass

class PythonCommand(Command):
    def execute(self) -> None:
        self.pc.run_code('Python')

    def unexecute(self) -> None:
        self.pc.stop()

class OcamlCommand(Command):
    def execute(self) -> None:
        self.pc.run_code('Ocaml')

class ComputerInterface:
    def __init__(self, python_cmd: OcamlCommand, ocaml_cmd: JavaCommand) -> None:
        self.ocaml_cmd = ocaml_cmd
        self.python_cmd = python_cmd
        self.current_cmd = None

    #вынесение логики в один метод

    def run(self, cmd):
        if self.current_cmd:
            self.current_cmd.unexecute()            
        self.current_cmd = cmd
        cmd.execute()


    def run_python(self):
        self.run()



    def run_ocaml(self):
        self.current_cmd = self.ocaml_cmd
        self.current_cmd

    def stop(self):
        if self.current_cmd:
            self.current_cmd.unexecute()
            self.current_cmd = None

        else:
            print('PC is idle now')

pc = Computer('Acer')
interface = ComputerInterface(PythonCommand(pc), OcamlCommand(pc))
interface.run_python()
interface.run_ocaml()
interface.stop()
interface.
