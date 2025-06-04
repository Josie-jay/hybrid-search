from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from pgvector.sqlalchemy import Vector

Base = declarative_base()

class MagazineInfo(Base):
    __tablename__ = "magazine_info"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    publication_date = Column(Date)
    category = Column(String)

    content = relationship("MagazineContent", back_populates="magazine")

class MagazineContent(Base):
    __tablename__ = "magazine_content"
    id = Column(Integer, primary_key=True)
    magazine_id = Column(Integer, ForeignKey("magazine_info.id"))
    content = Column(Text)
    vector_representation = Column(Vector(1536))

    magazine = relationship("MagazineInfo", back_populates="content")