from sqlalchemy import Column, Integer, Boolean, Text, Date
from database import Base
from datetime import date

class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    task = Column(Text)
    completed = Column(Boolean, default=False)
    due_date = Column(Date, default=date.today())
    
    def __repr__(self):
        return '<Todo %r' % (self.id)
    
    def extract_custom_date(self, custom_date_str):
        # Assuming custom_date_str is in the format 'YYYY-MM-DD'
        year, month, day = map(int, custom_date_str.split('-'))
        custom_date = date(year, month, day)
        self.due_date = custom_date