#!/usr/bin/python3
"""module contain class definition of new storage engine"""

from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker, Session
from sqlalchemy.orm import scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

classes = {'State': State, 'City': City, 'User': User,
           'Place': Place, 'Review': Review, 'Amenity': Amenity}


class DBStorage:
    """
    class definition of new storage engine in mySQL
    using Sqlalchemy

    attr:
    __engine: engine instance, set to None
    __session: session object set to None
    """
    __engine = None
    __session = None

    def __init__(self):
        """initialization of storage engine"""
        engine_url = "mysql+mysqldb://{}:{}@{}:3306/{}".format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB'))

        self.__engine = create_engine(engine_url, pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        queries the current database session depending on the cls arg
        if cls is None all objects will be queried, else just the Class
        cls

        Args:
        cls (obj): the object to query for, defualt value None

        Return: a dict representation of a object
                format: <class-name>.<object-id>: {obj}
        """
        inst_dict = {}

        if cls:
            for inst in self.__session.query(cls).all():
                inst_dict.update({"{}.{}".format(type(inst).__name__,
                                                 inst.id,): row})
        else:
            for k, v in classes.items():
                for inst in self.__session.query(v):
                    inst_dict.update({'{}.{}'.
                                      format(type(inst).__name__, inst.id,): inst})
        return (inst_dict)

    def new(self, obj):
        """
        add new object to current database session

        Args:
        obj (obj): object to add
        """
        self.__session.add(obj)

    def save(self):
        """commit changes of current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete an object from current database session

        Args:
        obj (object): object to delete
        """
        if obj:
            class_name = classes[type(obj).__name__]

            self.__session.query(class_name).filter(
                class_name.id == obj.id).delete()

    def reload(self):
        """creates the current database session
        and all tables in the database
        """
        Base.metadata.create_all(self.__engine)

        session = sessionmaker(bind=self.__engine, expire_on_commit=False)

        self.__session = scoped_session(session)

    def close(self):
        """close session"""
        self.__session.remove()
