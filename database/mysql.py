from typing import Dict
from interfaces import DatabaseInterface

class Mysqlrepository(DatabaseInterface):

    def select_one(self) -> Dict:
        return {
            'success': True,
            'data': 'Olá mundo'
        }