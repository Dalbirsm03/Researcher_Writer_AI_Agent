from crewai import Crew, Agent, Task, Process
from agents import news_researcher , news_writer
from tasks import researcher_task ,writer_task

my_crew = Crew(
    agents=[news_researcher, news_writer],
    tasks=[researcher_task, writer_task],
    process=Process.sequential,
    verbose=True,
)

result = my_crew.kickoff(inputs={'topic' :'AI in Chatbot'})
print(result)
