from typing import Tuple, Dict, Iterable
from app.models.tables import Category, Type, Expense, Income, User
from datetime import datetime, date

class Seed():

    # dd/mm/YY
    today= date.today().strftime("%d/%m/%Y")

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
        users = [
            {
                'name': 'Igor Iglesias',
                'email':'teste2@igoriglesias.com',
                'password': '1234'
            }
        ]
        self.__execute(User, users)

    def populate_categories(self) -> None:
        categories = [
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
        ]
        self.__execute(Category, categories)
        
    def populate_types(self) -> None:
        types = [
            {
                'name': 'Fixas',
                'description':'Se repetem todo mês',
            },
            {
                'name': 'Váriaveis',
                'description':'Váriaveis',
            },
        ]
        self.__execute(Type, types)

    def populate_expenses(self) -> None:
        expenses = [
            {
                'name': 'Cinema',
                'description':'Filme de zumbi',
                'value':'27,87',
                'date':datetime.now(),
                'type_id': 2,
                'category_id': 7,
            },
            {
                'name': 'Enel',
                'description':'Consumo de energia do mês',
                'value':'475,87',
                'date':datetime.now(),
                'type_id': 1,
                'category_id': 5,
            },
            
        ]
        self.__execute(Expense, expenses)

    def populate_incomes(self) -> None:
        incomes = [
            {
                'name': 'Visie',
                'description':'CLT',
                'value':'5000,00',
                'date':datetime.now(),
                'category_id': 1,
            },
            {
                'name': 'Consultoria',
                'description':'Sistema de ordens de serviço para xpto',
                'value':'1000,00',
                'date':datetime.now(),
                'category_id': 2,
            },
            
        ]
        self.__execute(Income, incomes)

    def __execute(self, model: object, data: Iterable[Tuple[Dict]]) -> None:
        try:
            model.query.delete()
            for row in data:
                instance_model = model(**row)
                self.db.session.add(instance_model)
            
            self.db.session.commit()
        except Exception as e:
            print(f'Ocorreu um erro: {e}')
            self.db.session.rollback()