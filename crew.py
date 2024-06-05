from crewai import Crew,Process
from tasks import research_task,write_task
from agents import news_researcher,news_writer


## Forming the tech focused crew with some enhanced configuration
crew=Crew(
     agents=[news_researcher,news_writer],
     tasks=[research_task,write_task],
     process=Process.sequential,

 )
result=crew.kickoff(inputs={'legalStatement':"costs whether costs should follow the event reserved costs questionable success of motion where applicants did not pursue application for interlocutory relief in favour of early trial where affidavits contained unnecessary detail and inaccuracies and were given low weight costs of senior and junior counsel contested order 62 rule 36a(1)"})
print(result)   
## starting the task execution process wiht enhanced feedback
# def get_geminiresponse(query):
#     result=crew.kickoff(inputs={'legalStatement':"costs whether costs should follow the event reserved costs questionable success of motion where applicants did not pursue application for interlocutory relief in favour of early trial where affidavits contained unnecessary detail and inaccuracies and were given low weight costs of senior and junior counsel contested order 62 rule 36a(1)"})
#     print(result)






