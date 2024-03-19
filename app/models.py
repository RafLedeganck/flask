"""
Dit zijn de klasses die we definiëren maar nu maken we geen instances want het is een databank (?)
"""

from typing import Optional   # type hinting zodat kolommen in db van het juiste data type zijn
from app import db
import sqlalchemy as sa
import sqlalchemy.orm as so   # Object Relational Mapper

class Houses(db.Model):
    """
    Definitie van de kolommen in de db tabel
    """
    id: so.Mapped[int] = so.mapped_column(primary_key=True)   # 'id' = kolomnaam ; type = integer
    longitude: so.Mapped[float] = so.mapped_column(sa.Float, default=0.0, nullable=True)
    latitude: so.Mapped[float] = so.mapped_column(sa.Float, default=0.0, nullable=True)
    housing_median_age: so.Mapped[float] = so.mapped_column(sa.Float, default=0.0, nullable=True)
    total_rooms: so.Mapped[float] = so.mapped_column(sa.Float, default=0.0, nullable=True)
    total_bedrooms: so.Mapped[float] = so.mapped_column(sa.Float, default=0.0, nullable=True)
    population: so.Mapped[float] = so.mapped_column(sa.Float, default=0.0, nullable=True)
    households: so.Mapped[float] = so.mapped_column(sa.Float, default=0.0, nullable=True)
    median_income: so.Mapped[float] = so.mapped_column(sa.Float, default=0.0, nullable=True)
    median_house_value: so.Mapped[float] = so.mapped_column(sa.Float, default=0.0, nullable=True)
    ocean_proximity: so.Mapped[float] = so.mapped_column(sa.String(256))

    def __repr__(self) -> str:
        return f"<Houses {self.id}>"   # indien error geeft hij  het ID van het huis in error
