
from app import app
from datetime import datetime

class Filters():
    
    @app.template_filter()
    def date(date: str) -> None:
        new_date = datetime.fromisoformat(date)
        return new_date.strftime("%d/%m")