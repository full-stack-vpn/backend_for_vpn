from sqlalchemy import create_engine, Column,String,Integer,BIGINT
from sqlalchemy.orm import declarative_base, sessionmaker
import json

class work_with_bd:
    @staticmethod
    def bd_create(data):
        try:
            data_base_url = 'postgresql://postgres:11111@db:5432/test_vpn'
            engine = create_engine(data_base_url)
            Base = declarative_base()

            class user_data(Base):
                __tablename__ = "vpn_users"
                user_name = Column(String, primary_key=True)
                paid_or_free = Column(String)
                over_day = Column(String)

            Session = sessionmaker(bind=engine)
            session = Session()
            user = user_data(user_name=data.get("user_name"), paid_or_free = data.get("paid_or_free"),over_day = data.get("over_day"))
            #user = user_data(user_name="artem",paid_or_free="yes",over_day="0.2")
            session.add(user)

            session.commit()
            session.close()
            return True

        except:
            return "Пользователь не создан,введите коректные данные"

    @staticmethod
    def bd_read():
        data_base_url = 'postgresql://postgres:11111@db:5432/test_vpn'
        engine = create_engine(data_base_url)
        Base = declarative_base()

        class user_data(Base):
            __tablename__ = "vpn_users"
            user_name = Column(String, primary_key=True)
            paid_or_free = Column(String)
            over_day = Column(String)


        Session = sessionmaker(bind=engine)
        session = Session()
        users = session.query(user_data).all()
        session.close()
        users_list = [
            {
                "user_name": user.user_name,
                "paid_or_free": user.paid_or_free,
                "over_day": user.over_day
            }
            for user in users
        ]

        users_json = json.dumps(users_list, indent=4)

        # Отладочный вывод
        print(f"вот данные: {users_json}")
        users_list = json.loads(users_json)

        return users_list