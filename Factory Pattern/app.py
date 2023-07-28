from factory import MysqlFactory
from usecase import UseCase


usecase = MysqlFactory.create()
response = usecase.do_something(True)

print(response)