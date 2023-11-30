# from config import db
# from sqlalchemy import Column, Integer, String, Text, ForeignKey, MetaData, LargeBinary,Date,Boolean
# from sqlalchemy import create_engine,text
#
# class Sessao(db.Base):
#
#     __tablename__ = 'sessao_teste'
#     __table_args__ = {"schema": "public"}
#
#     idsessao = Column(Integer, primary_key=True, autoincrement=True)
#     nome_sessao = Column(LargeBinary, nullable=False)
#     idusuario = Column(Integer, ForeignKey('usuario_teste.idusuario'), nullable=True)
#     data_sessao = Column(Date, nullable=False)
#     status_sessao = Column(Boolean, nullable=False)
#
#
#
#
