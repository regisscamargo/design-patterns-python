from usecase import UseCase
from database import Mysqlrepository


class MysqlFactory:

    @staticmethod
    def create() -> UseCase:
        return UseCase(Mysqlrepository())