from crewai import Agent
from dotenv import load_dotenv
load_dotenv()
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import tool

llm = ChatGoogleGenerativeAI(
    model = 'gemini-1.5-flash',
    verbose = True,
    temperature = 0.5,
    google_api_key = os.getenv("GOOGLE_API_KEY")
)

news_researcher = Agent(
    role = "Senior Researcher",
    goal = 'Uncover groundbreaking technologies in {topic}',
    verbose = True,
    memory = True,
    backstory = ("""You are curious and want to uncover news or technology that could change the future and make innvoations"""
    ),
    tools = [tool],
    llm = llm,
    allow_delegation = True
)

news_writer = Agent(
    role = 'Writer',
    goal = "Write stories about the {topic}",
    verbose = True,
    memory = True,
    backstory = (
        """You are expert and a professional agent in simplifying the complex topics are narrating them in a very menaingful and mannered way"""
    ),
    tools = [tool],
    llm = llm,
    allow_delegation = False
)