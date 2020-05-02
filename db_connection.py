from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnection:
    def __init__(self):
        self.engine = create_engine("mysql+pymysql://root:pwd@localhost/jjuina?host=localhost?port=3306")
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def get_session(self):
        return self.session

    def add(self, object):
        try:
            self.session.add(object)
            self.session.commit()
        except:
            session.rollback()
            raise
        finally:
            self.session.close()

    def add_all(self, object_list):
        try:
            self.session.add_all(object_list)
            self.session.commit()
        except:
            session.rollback()
            raise
        finally:
            self.session.close()

    def execute(self, sql):
        try:
            self.session.execute(sql)
            self.session.commit()
        except:
            session.rollback()
            raise
        finally:
            self.session.close()

    def close(self):
        self.session.close()