from crewai import Task
from tools import tool
from agents import news_researcher,news_writer

# Research task
research_task = Task(
  description=(
    "Identify the surfacing highly tailored news, case law updates, and emerging trends in {topic}."
  ),
  expected_output='A comprehensive 10 paragraphs long report source URL/Link on {topic}.',
  tools=[tool],
  agent=news_researcher,
)

# Writing task with language model configuration
write_task = Task(
  description=(
    "Compose an insightful report surfacing highly tailored news, case law updates, and emerging trends on {topic}."
  ),
  expected_output='A 10 paragraph report on {topic} with source URL/Link on with advancements formatted as markdown.',
  tools=[tool],
  agent=news_writer,
  async_execution=False,
  output_file='abc22.md'  # Example of output customization
)