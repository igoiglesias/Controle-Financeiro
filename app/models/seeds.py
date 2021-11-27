from typing import Tuple, Dict, Iterable
from app.models.tables import Category, Type, Expense, Income, User


class Seed():

    def __init__(self, app: object, db: object) -> None:
        self.app = app
        self.db = db
        self.__seed()
    
    def __seed(self) -> None:

        env = self.app.config.get('ENV')
        seed = self.app.config.get('SEED')

        if env == 'development' and seed:
            print(' * Seed started')
            methods = [populate for populate in dir(self) if 'populate_' in populate]
            for method in methods:
                print(f' * Populating {method.split("populate_")[1].capitalize()}')
                callable_method = getattr(self, method)
                callable_method()
            print(' * Seed ended')

    def populate_users(self) -> None:
        users = (
            {
                'name': 'Igor Iglesias',
                'email':'teste@igoriglesias.com',
                'password': '1234'
            }
        )
        self.__execute(User, users)

    def populate_categories(self) -> None:
        categories = (
            {
                'name':'Salário',
                'description':'Salário'
            },
            {
                'name':'Extra',
                'description':'Serviçoes extras'
            },
            {
                'name':'Alimentação',
                'description':'Alimentação'
            },
            {
                'name':'Combustivel',
                'description':'Combustivel'
            },
            {
                'name':'Enegia',
                'description':'Enegia elétrica'
            },
            {
                'name':'Cursos',
                'description':'Cursos e treinamentos'
            },
            {
                'name':'Lazer',
                'description':'Lazer'
            },
        )
        self.__execute(Category, categories)
        
    def populate_types(self) -> None:
        users = (
            {
                'name': 'Fixas',
                'description':'Se repetem todo mês',
            },
            {
                'name': 'Váriaveis',
                'description':'Váriaveis',
            },
        )
        self.__execute(Type, users)

    def __execute(self, model: object, data: Iterable[Tuple[Dict]]) -> None:
        try:
            model.query.delete()
            for row in data:
                instance_model = model(**row)
                self.db.session.add(instance_model)
            
            self.db.session.commit()
        except:
            self.db.session.rollback()