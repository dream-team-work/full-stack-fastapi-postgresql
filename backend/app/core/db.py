from sqlmodel import Session, create_engine, SQLModel, select
from app import crud
from app.core.config import settings
from app.models import User, UserCreate

# Criação da engine de conexão com o banco de dados
engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))

# Função para criar as tabelas no banco de dados
def create_db_and_tables():
    # Certificando-se de que todos os modelos foram importados corretamente
    # SQLModel.metadata.create_all(engine) cria as tabelas
    SQLModel.metadata.create_all(engine)

# Função para inicializar o banco de dados e criar o superusuário
def init_db(session: Session) -> None:
    user = session.exec(
        select(User).where(User.email == settings.FIRST_SUPERUSER)
    ).first()
    
    # Se o usuário não existir, cria o primeiro superusuário
    if not user:
        user_in = UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.create_user(session=session, user_create=user_in)
