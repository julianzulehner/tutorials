import sqlalchemy as sa 
import sqlalchemy.orm as so 




class Base(so.DeclarativeBase):
    pass

class User(Base): 
    __tablename__ = "user"

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(unique=True, nullable=False)

class Vocable(Base):
    __tablename__ = "vocable"

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    de: so.Mapped[str] = so.mapped_column(nullable=True)
    en: so.Mapped[str] = so.mapped_column(nullable=True)
