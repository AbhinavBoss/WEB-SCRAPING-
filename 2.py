from bs4 import BeautifulSoup 
import requests as requests
import pandas as pd
your_skill=input("Enter your skill for job: ")
ufs=input("Enter the skill you are not familiar with: ")
print(f"Filtering {ufs} out...\n searching for {your_skill}...")
company=[]
skill=[]
info=[]
for i in range(1,4):
    html_text = requests.get(f"https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords={your_skill}&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence={str(i)}&startPage=1")
    soup = BeautifulSoup(html_text.content, 'html5lib') 
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for job in jobs:       
        company_name = job.find("h3", class_ = "joblist-comp-name").text.replace(' ','')
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
        more_info=job.header.h2.a['href']
        if ufs not in skills:
            # print(f"Company name: {company_name}")
            # print(f"Required Skills: {skills}")
            # print(f"More Info : {more_info}")
            company.append(company_name)
            skill.append(skills)
            info.append(more_info)
df=pd.DataFrame({"Company":company , "Job-Skills":skill , "Info":info})
df.to_excel("C:/PROGRAMMING LANGUAGES/jobsearch.xlsx") 