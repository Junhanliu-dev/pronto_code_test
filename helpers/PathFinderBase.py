import abc

from utils.Coordination import Coordination


class PathFinderBase(abc.ABC):

    @abc.abstractmethod
    def find_path(self, start_point: Coordination, current_point: Coordination) -> list:
        pass

    @abc.abstractmethod
    def find_minimum_path_cost(self, start_point: Coordination, current_point: Coordination) -> int:
        pass
