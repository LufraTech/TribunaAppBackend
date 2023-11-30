# # from config import db
# # from sqlalchemy import Column, Integer, String, Text, ForeignKey, MetaData, LargeBinary,Boolean,Text
# # from sqlalchemy import create_engine,text
# #
# class User(db.Base):
#
#     __tablename__ = 'usuario_teste'
#     __table_args__ = {"schema": "public"}
#
#
#     idusuario = Column(Integer, primary_key=True, autoincrement=True)
#     nome_usuario = Column(String, nullable=False)
#     senha_usuario = Column(Text, nullable=True)
#     foto_perfil = Column(Text, nullable=True)
#     idpartido = Column(Integer, ForeignKey('partido_teste.idpartido'), nullable=True)
#     email_usuario = Column(String, nullable=False)
#     usuario_admin = Column(Boolean, nullable=False)
#     idcamara = Column(Integer, ForeignKey('camara_teste.idcamara'), nullable=True)
#
