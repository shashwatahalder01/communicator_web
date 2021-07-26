import os
from utils.uitlsfunction import readdate, readcounter, keepreports

reportFolderName = f"{readdate()}_{readcounter()}"

# For running testCases
command = f"pytest -s --alluredir=ReportAllure/{reportFolderName} --html=ReportHtml/report_{reportFolderName}.html --self-contained-html TestCase"
os.system(command)

# number of allure & html reports to keep
number = 2
keepreports(number)

# For generating report
command = f"allure serve ReportAllure/{reportFolderName}"
os.system(command)
