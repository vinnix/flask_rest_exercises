import User
import psycopg2
from sqlalchemy import create_engine

db = SQLAlchemy()

# Used for checking connection
#
def check_connection():
    engine = create_engine("postgresql+psycopg2://image_app:im4g3_4pp@localhost/image'", echo=True)
    return engine


#
#
# MAIN BLOCK
#
#
if __name__ == '__main__':
        c = check_connection
        print( c);



