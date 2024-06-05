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
    goal='Unccover what is going around about the law in {topic} with source URL/Link',
    verbose=True,
    memory=True,
    backstory=(
        "Search on internet and collect information on surfacing highly tailored news, case law updates, and emerging trends"

    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True

)

## creating a write agent with custom tools responsible in writing news blog

news_writer = Agent(
  role='Writer',
  goal='Need report content with URL/links of {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "need to find insight from information on surfacing highly tailored news, case law updates, and emerging trends"
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=False
)

