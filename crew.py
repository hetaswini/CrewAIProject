from crewai import Crew,Process
from tasks import research_task,write_task
from agents import news_researcher,news_writer


## Forming the tech focused crew with some enhanced configuration
crew=Crew(
     agents=[news_researcher,news_writer],
     tasks=[research_task,write_task],
     process=Process.sequential,

 )
## starting the task execution process wiht enhanced feedback
result=crew.kickoff(inputs={'legalStatement':"personal insolvency agreements where debtor signed authority to have his affairs dealt with under part x where debtor required to give proposal for dealing with his affairs where proposal required to include draft personal insolvency agreement where agreement required to identify debtor's property to be available to pay creditors' claims whether provisions of draft agreement made such identification impossible whether authority effective whether authority an abuse of process bankruptcy"})
print(result)   





