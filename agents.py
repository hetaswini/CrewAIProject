from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os


## call the gemini models
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

# Creating a senior researcher agent with memory and verbose mode
news_researcher=Agent(
    role="Senior Researcher",
    goal='Unccover what is going around on interest/topics related to law and practice area of law for this '"'{legalStatement}.'"' with source URL/Link',
    verbose=True,
    memory=True,
    backstory=(
        "Search on internet and collect information on interest/topics related to law and practice area of law for this '"'{legalStatement}.'"' surfacing highly tailored news, case law updates, and emerging trends on that"

    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True

)

## creating a write agent with custom tools responsible in writing news blog

news_writer = Agent(
  role='Writer',
  goal='Need report content with URL/links of interest/topics related to law and practice area of law for this '"'{legalStatement}.'"'',
  verbose=True,
  memory=True,
  backstory=(
    "need to find and write insight from information on interest/topics related to law and practice area of law for this '"'{legalStatement}.'"' and search surfacing highly tailored news, case law updates, and emerging trends on that"
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=False
)

