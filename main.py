from fastapi import FastAPI, Request
from sqlalchemy import Column, String, Integer
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from databases import Database
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

DATABASE_URL = "sqlite+aiosqlite:///./database.db"
database = Database(DATABASE_URL)
Base = declarative_base()
engine = create_async_engine(DATABASE_URL, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
templates = Jinja2Templates(directory="templates")


app = FastAPI()


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    league = Column(String)

class SelectedTeamsData(BaseModel):
    selected_teams: dict


@app.on_event("startup")
async def startup_db():
    await database.connect()
    async with database.transaction():
        create_table_query = """
            CREATE TABLE IF NOT EXISTS teams (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) UNIQUE,
                league VARCHAR(100)
            )
        """
        await database.execute(create_table_query)
        teams = [
            {"id": 1,"name": "Arsenal", "league": "Premier_League"},
            {"id": 2,"name": "Aston Villa", "league": "Premier_League"},
            {"id": 3,"name": "Burnley", "league": "Premier_League"},
            {"id": 4,"name": "Chelsea", "league": "Premier_League"},
            {"id": 5,"name": "Everton", "league": "Premier_League"},
            {"id": 6,"name": "Fulham", "league": "Premier_League"},
            {"id": 7,"name": "Liverpool", "league": "Premier_League"},
            {"id": 8,"name": "Manchester_City", "league": "Premier_League"},
            {"id": 9,"name": "Manchester_United", "league": "Premier_League"},
            {"id": 10,"name": "Newcastle", "league": "Premier_League"},
            {"id": 11,"name": "Tottenham", "league": "Premier_League"},
            {"id": 12,"name": "West_Ham", "league": "Premier_League"},
            {"id": 13,"name": "Crystal_Palace", "league": "Premier_League"},
            {"id": 14,"name": "Sheffield_United", "league": "Premier_League"},
            {"id": 15,"name": "Wolves", "league": "Premier_League"},
            {"id": 16,"name": "Bournemouth", "league": "Premier_League"},
            {"id": 17,"name": "Brighton", "league": "Premier_League"},
            {"id": 18,"name": "Luton", "league": "Premier_League"},
            {"id": 19,"name": "Nottingham", "league": "Premier_League"},
            {"id": 20,"name": "Brentford", "league": "Premier_League"},
            {"id": 21,"name": "Lille", "league": "Ligue_1"},
            {"id": 22,"name": "Nice", "league": "Ligue_1"},
            {"id": 23,"name": "Le_Havre", "league": "Ligue_1"},
            {"id": 24,"name": "Lorient", "league": "Ligue_1"},
            {"id": 25,"name": "Metz", "league": "Ligue_1"},
            {"id": 26,"name": "Monaco", "league": "Ligue_1"},
            {"id": 27,"name": "Nantes", "league": "Ligue_1"},
            {"id": 28,"name": "PSG", "league": "Ligue_1"},
            {"id": 29,"name": "Strasbourg", "league": "Ligue_1"},
            {"id": 30,"name": "Brest", "league": "Ligue_1"},
            {"id": 31,"name": "Clermont", "league": "Ligue_1"},
            {"id": 32,"name": "Montpellier", "league": "Ligue_1"},
            {"id": 33,"name": "Reims", "league": "Ligue_1"},
            {"id": 34,"name": "Marsylia", "league": "Ligue_1"},
            {"id": 35,"name": "Toulouse", "league": "Ligue_1"},
            {"id": 36,"name": "Lens", "league": "Ligue_1"},
            {"id": 37,"name": "Rennes", "league": "Ligue_1"},
            {"id": 38,"name": "Lyon", "league": "Ligue_1"},
            {"id": 39,"name": "Vallecano", "league": "La_Liga"},
            {"id": 40,"name": "Valencia", "league": "La_Liga"},
            {"id": 41,"name": "Real_Sociedad", "league": "La_Liga"},
            {"id": 42,"name": "Las_Palmas", "league": "La_Liga"},
            {"id": 43,"name": "Alaves", "league": "La_Liga"},
            {"id": 44,"name": "Celta_Vigo", "league": "La_Liga"},
            {"id": 45,"name": "Cadiz", "league": "La_Liga"},
            {"id": 46,"name": "Real_Madryt", "league": "La_Liga"},
            {"id": 47,"name": "Barcelona", "league": "La_Liga"},
            {"id": 48,"name": "Atletico_Madryt", "league": "La_Liga"},
            {"id": 49,"name": "Mallorca", "league": "La_Liga"},
            {"id": 50,"name": "Athletic_Bilbao", "league": "La_Liga"},
            {"id": 51,"name": "Betis", "league": "La_Liga"},
            {"id": 52,"name": "Getafe", "league": "La_Liga"},
            {"id": 53,"name": "Osasuna", "league": "La_Liga"},
            {"id": 54,"name": "Girona", "league": "La_Liga"},
            {"id": 55,"name": "Granada", "league": "La_Liga"},
            {"id": 56,"name": "Sevilla", "league": "La_Liga"},
            {"id": 57,"name": "Almeria", "league": "La_Liga"},
            {"id": 58,"name": "FC_Union_Berlin", "league": "Bundesliga"},
            {"id": 59,"name": "Eintracht_Frankfurt", "league": "Bundesliga"},
            {"id": 60,"name": "Bayern_Monachium", "league": "Bundesliga"},
            {"id": 61,"name": "Bayer_Leverkusen", "league": "Bundesliga"},
            {"id": 62,"name": "Werder_Brema", "league": "Bundesliga"},
            {"id": 63,"name": "VfL_Wolfsburg", "league": "Bundesliga"},
            {"id": 64,"name": "Bochum", "league": "Bundesliga"},
            {"id": 65,"name": "Borussia_Dortmund", "league": "Bundesliga"},
            {"id": 66,"name": "Borussia_Moenchengladbach", "league": "Bundesliga"},
            {"id": 67,"name": "TSG_Hoffenheim", "league": "Bundesliga"},
            {"id": 68,"name": "FC_Koeln", "league": "Bundesliga"},
            {"id": 69,"name": "FSV_Mainz_05", "league": "Bundesliga"},
            {"id": 70,"name": "SC_Freiburg", "league": "Bundesliga"},
            {"id": 71,"name": "FC_Augsburg", "league": "Bundesliga"},
            {"id": 72,"name": "VfB_Stuttgart", "league": "Bundesliga"},
            {"id": 73,"name": "Darmstadt", "league": "Bundesliga"},
            {"id": 74,"name": "Heidenheim", "league": "Bundesliga"},
            {"id": 75,"name": "RB_Lipsk", "league": "Bundesliga"},
            {"id": 76,"name": "Lecce", "league": "Serie_A"},
            {"id": 77,"name": "Bologna", "league": "Serie_A"},
            {"id": 78,"name": "Genoa", "league": "Serie_A"},
            {"id": 79,"name": "Napoli", "league": "Serie_A"},
            {"id": 80,"name": "Udinese", "league": "Serie_A"},
            {"id": 81,"name": "Monza", "league": "Serie_A"},
            {"id": 82,"name": "Sassuolo", "league": "Serie_A"},
            {"id": 83,"name": "Salernitana", "league": "Serie_A"},
            {"id": 84,"name": "AS_Roma", "league": "Serie_A"},
            {"id": 85,"name": "Inter", "league": "Serie_A"},
            {"id": 86,"name": "Juventus", "league": "Serie_A"},
            {"id": 87,"name": "Fiorentina", "league": "Serie_A"},
            {"id": 88,"name": "AC_Milan", "league": "Serie_A"},
            {"id": 89,"name": "Atalanta", "league": "Serie_A"},
            {"id": 90,"name": "Lazio", "league": "Serie_A"},
            {"id": 91,"name": "Cagliari", "league": "Serie_A"},
            {"id": 92,"name": "Torino", "league": "Serie_A"},
            {"id": 93,"name": "Empoli", "league": "Serie_A"},
            {"id": 94,"name": "Verona", "league": "Serie_A"},
        ]
        for team_data in teams:
            insert_query = """
                INSERT INTO teams (id, name, league) VALUES (:id, :name, :league)
            """
            await database.execute(insert_query, values=team_data)

@app.on_event("shutdown")
async def shutdown_db():
    drop_table_query = """DROP TABLE teams;"""
    await database.execute(drop_table_query)
    await database.disconnect()

async def get_db():
    db = database
    try:
        yield db
    finally:
        db.disconnect()


@app.get("/", response_class=HTMLResponse)
async def get_home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/teams/")
async def get_teams(request: Request):
    async with SessionLocal() as session:
        team_query = select(Team.name)
        team_result = await session.execute(team_query)
        teams = [row[0] for row in team_result]
    return templates.TemplateResponse("teams.html", {"request": request, "teams": teams})

@app.get("/leagues/")
async def get_leagues(request: Request):
    async with SessionLocal() as session:
        league_query = select(Team.league).distinct()
        league_result = await session.execute(league_query)
        leagues = [row[0] for row in league_result]
    return templates.TemplateResponse("leagues.html", {"request": request, "leagues": leagues})

@app.get("/leagues/{league}/teams/")
async def get_teams(request: Request, league: str):
    async with SessionLocal() as session:
        team_query = select(Team.name).where(Team.league == league)
        team_result = await session.execute(team_query)
        teams = [row[0] for row in team_result]
    
    return templates.TemplateResponse("teams.html", {"request": request, "teams": teams})

@app.get("/select_teams/")
async def select_teams(request: Request):
    async with SessionLocal() as session:
        leagues_query = select(Team.league).distinct()
        leagues_result = await session.execute(leagues_query)
        leagues = [row[0] for row in leagues_result]
        teams_by_league = {}
        for league in leagues:
            teams_query = select(Team).where(Team.league == league)
            teams_result = await session.execute(teams_query)
            teams = [team[0] for team in teams_result]
            teams_by_league[league] = teams
    return templates.TemplateResponse("team_selection_form.html", {"request": request, "leagues": leagues, "teams_by_league": teams_by_league})

@app.post("/save_selection/")
async def save_selection(request: Request):
    selected_teams = await request.form()
    teams_dict = {}

    for key, value in selected_teams.items():
        league, team_id = key.split("[")[1].split("]")[0], value
        teams_dict[league] = team_id

    selected_teams_info = []

    async with SessionLocal() as session:
        for league, team_id in teams_dict.items():
            team_query = select(Team).where(Team.id == int(team_id))
            team_result = await session.execute(team_query)
            team = team_result.scalar()
            selected_teams_info.append({"league": league, "team": team})

    return templates.TemplateResponse(
        "selected_teams.html", {"request": request, "selected_teams_info": selected_teams_info}
    )

