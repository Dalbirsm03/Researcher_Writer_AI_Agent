from crewai import Task
from tools import tool
from agents import news_researcher , news_writer

researcher_task = Task(
  description=('Identufy next big thing in {topic} and your report should analyze all pros and cons and should also provide potential risk and opportunities'),
  expected_output='A long 3 paragraph research blogon latest AI trends',
  agent=news_researcher,
  tools=[tool]
)

writer_task = Task(
  description='Compose easy to understand article on {topic} , Focus on trend impacting the industry',
  expected_output='A 3 paragraph article on {topic}',
  agent=news_writer,
  async_execution = False,
  tools=[tool],
  output_file = 'example.mb'
)