# from config import db
# from sqlalchemy import Column, Integer, String, Text, ForeignKey, MetaData, LargeBinary
# from sqlalchemy import create_engine,text
#
# class Partido(db.Base):
#
#     __tablename__ = 'camara_teste'
#     __table_args__ = {"schema": "public"}
#
#     idpartido = Column(Integer, primary_key=True, autoincrement=True)
#     nome_partido = Column(String, nullable=False)
#     sigla_partido = Column(String, nullable=False)
#     deferimento= Column(String, nullable=False)
#     presidente_nacional = Column(String, nullable=False)
#     n_legenda= Column(Integer, nullable=False)