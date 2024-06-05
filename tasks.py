from crewai import Task
from tools import tool
from agents import news_researcher,news_writer #,news_law_expert,news_analyst

# Research task
research_task = Task(
  description=(
    "'"'{legalStatement}.'"' Identify what practice area of law does the above case statement belong to and what interests/topics is being discussed in above statement and search surfacing highly tailored news, case law updates, and emerging trends"
  ),
  expected_output='A comprehensive 10 paragraphs long report source URL/Link on interest and practice area of law in this '"'{legalStatement}.'"'',
  tools=[tool],
  agent=news_researcher,
)

# Writing task with language model configuration
write_task = Task(
  description=(
    "Compose an insightful report interest/topics related to law and practice area of law for this '"'{legalStatement}.'"' case statement and write surfacing highly tailored news, case law updates, and emerging trends."
  ),
  expected_output='A 10 paragraph report on interest and practice area of law in this '"'{legalStatement}.'"' with source URL/Link on with advancements formatted as markdown.',
  tools=[tool],
  agent=news_writer,
  async_execution=False,
  output_file='abc22.md'  # Example of output customization
)