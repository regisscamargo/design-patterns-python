from typing import Dict, Type, Union
from interfaces import DatabaseInterface

class UseCase:

    def __init__(self, repository: Type[DatabaseInterface]) -> None:
        self.__respository = repository

    def do_something(self, data: bool) -> Union[Dict, None]:
        return self.__respository.select_one() if data else None