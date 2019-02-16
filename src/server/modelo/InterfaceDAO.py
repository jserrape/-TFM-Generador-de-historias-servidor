from abc import ABCMeta, abstractmethod

class InterfaceDAO:

    __metaclass__ = ABCMeta

    @abstractmethod
    def insertar(self, object):
        raise NotImplementedError

    @abstractmethod
    def actualizar(self, object):
        raise NotImplementedError

    @abstractmethod
    def leerTodo(self):
        raise NotImplementedError

    @abstractmethod
    def eliminar(self, object):
        raise NotImplementedError

    @abstractmethod
    def eliminarTodo(self):
        raise NotImplementedError

    @abstractmethod
    def buscar(self, object):
        raise NotImplementedError

    @abstractmethod
    def preparar_ddbb(self):
        raise NotImplementedError

    @abstractmethod
    def ejecutar_query(self):
        raise NotImplementedError
