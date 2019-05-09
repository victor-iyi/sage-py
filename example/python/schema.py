import secrets
from sqlalchemy import Column, ForeignKey, Integer, Text, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class Vertex(Base):
    __tablename__ = 'vertex'

    id = Column(String(8), primary_key=True, unique=True,
                default=lambda: secrets.token_hex(8))
    label = Column(Text, nullable=False)
    schema = Column(String(250))

    def __repr__(self):
        return f"<Vertex(label='{self.label}', schema='{self.schema}')>"


class Graph(Base):
    __tablename__ = 'graph'
    id = Column(Integer, primary_key=True)
    vertex_id = Column(Integer, ForeignKey('vertex.id'))
    vertex = relationship(Vertex)


if __name__ == '__main__':
    engine = create_engine('sqlite:///graph.db')
    Base.metadata.create_all(engine)
