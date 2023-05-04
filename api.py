from flask import Flask, jsonify, request
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
driver = webdriver.Chrome(executable_path = "\Code\chromedriver.exe")
results = {"profile":{},"results":{}}

# functions to get results of each semester

def extract_eighth_sem_data(year,roll_number):
    try:
        driver.get("https://exam.bujhansi.ac.in/frmViewCampusResult.aspx?cd=MwA4ADAA")
        Session = driver.find_element("id","ddlSession")
        select = Select(Session)
        select.select_by_visible_text(year)
        course = driver.find_element("id","ddlCourse")
        select = Select(course)
        select.select_by_visible_text("B.Tech (Computer Science & Engg) VIII Semester")
        roll = driver.find_element("id","txtUniqueID")
        roll.clear()
        roll.send_keys(roll_number)
        ResultType = driver.find_element("id","ddlResultType")
        select = Select(ResultType)
        select.select_by_visible_text("Main")
        submit = driver.find_element("id","btnGetResult")
        submit.click()
        html = driver.page_source
        soup=BeautifulSoup(html,"html.parser")
        table=soup.find(id="tblMarksContent")
        temp = {"subjects":[],"total":[]}
        i=5
        row = table.find_all("tr")
        while i<17:
            col = row[i].find_all("td")
            if((i>=5 and i<8) or (i>=11 and i<=13)):
                subject=col[0].text
                max_min=col[9].text
                mark=col[10].text
                cgpa=col[11].text
                temp["subjects"].append([subject,max_min,mark,cgpa])
                i=i+1
            else:
                i=i+1
        col = row[15].find_all("th")
        max_score=col[2].text
        min_score=col[4].text
        marks_obtained=col[10].text
        cgpa_obtained=col[12].text
        temp["total"].append([max_score,min_score,marks_obtained,cgpa_obtained])
        results["results"][8]=temp 
        temp = {"subjects":[],"total":[]}
    except:
        return
    
def extract_seventh_sem_data(year,roll_number):
    try:
        driver.get("https://exam.bujhansi.ac.in/frmViewCampusResult.aspx?cd=MwA4ADAA")
        Session = driver.find_element("id","ddlSession")
        select = Select(Session)
        select.select_by_visible_text(year)
        course = driver.find_element("id","ddlCourse")
        select = Select(course)
        select.select_by_visible_text("B.Tech (Computer Science & Engg) VII Semester")
        roll = driver.find_element("id","txtUniqueID")
        roll.clear()
        roll.send_keys(roll_number)
        ResultType = driver.find_element("id","ddlResultType")
        select = Select(ResultType)
        select.select_by_visible_text("Main")
        submit = driver.find_element("id","btnGetResult")
        submit.click()
        html = driver.page_source
        soup=BeautifulSoup(html,"html.parser")
        table=soup.find(id="tblMarksContent")
        temp = {"subjects":[],"total":[]}
        i=5
        row = table.find_all("tr")
        while i<17:
            col = row[i].find_all("td")
            if((i>=5 and i<10) or (i>=13 and i<=15)):
                subject=col[0].text
                max_min=col[9].text
                mark=col[10].text
                cgpa=col[11].text
                temp["subjects"].append([subject,max_min,mark,cgpa])
                i=i+1
            else:
                i=i+1
        col = row[17].find_all("th")
        max_score=col[2].text
        min_score=col[4].text
        marks_obtained=col[10].text
        cgpa_obtained=col[12].text
        temp["total"].append([max_score,min_score,marks_obtained,cgpa_obtained])
        results["results"][7]=temp 
        temp = {"subjects":[],"total":[]}
    except:
        return
    
def extract_sixth_sem_data(year,roll_number):
    try:
        driver.get("https://exam.bujhansi.ac.in/frmViewCampusResult.aspx?cd=MwA4ADAA")
        Session = driver.find_element("id","ddlSession")
        select = Select(Session)
        select.select_by_visible_text(year)
        course = driver.find_element("id","ddlCourse")
        select = Select(course)
        select.select_by_visible_text("B.Tech (Computer Science & Engg) VI Semester")
        roll = driver.find_element("id","txtUniqueID")
        roll.clear()
        roll.send_keys(roll_number)
        ResultType = driver.find_element("id","ddlResultType")
        select = Select(ResultType)
        select.select_by_visible_text("Main")
        submit = driver.find_element("id","btnGetResult")
        submit.click()
        html = driver.page_source
        soup=BeautifulSoup(html,"html.parser")
        table=soup.find(id="tblMarksContent")
        temp = {"subjects":[],"total":[]}
        i=5
        row = table.find_all("tr")
        while i<17:
            col = row[i].find_all("td")
            if((i>=5 and i<10) or (i>=13 and i<=17)):
                subject=col[0].text
                max_min=col[9].text
                mark=col[10].text
                cgpa=col[11].text
                temp["subjects"].append([subject,max_min,mark,cgpa])
                i=i+1
            else:
                i=i+1
        col = row[18].find_all("th")
        max_score=col[2].text
        min_score=col[4].text
        marks_obtained=col[10].text
        cgpa_obtained=col[12].text
        temp["total"].append([max_score,min_score,marks_obtained,cgpa_obtained])
        results["results"][6]=temp 
        temp = {"subjects":[],"total":[]}
    except:
        return

def extract_fifth_sem_data(year,roll_number):
    try:
        driver.get("https://exam.bujhansi.ac.in/frmViewCampusResult.aspx?cd=MwA4ADAA")
        Session = driver.find_element("id","ddlSession")
        select = Select(Session)
        select.select_by_visible_text(year)
        course = driver.find_element("id","ddlCourse")
        select = Select(course)
        select.select_by_visible_text("B.Tech (Computer Science & Engg) V Semester")
        roll = driver.find_element("id","txtUniqueID")
        roll.clear()
        roll.send_keys(roll_number)
        ResultType = driver.find_element("id","ddlResultType")
        select = Select(ResultType)
        select.select_by_visible_text("Main")
        submit = driver.find_element("id","btnGetResult")
        submit.click()
        html = driver.page_source
        soup=BeautifulSoup(html,"html.parser")
        table=soup.find(id="tblMarksContent")
        temp = {"subjects":[],"total":[]}
        i=5
        row = table.find_all("tr")
        while i<17:
            col = row[i].find_all("td")
            if((i>=5 and i<10) or (i>=13 and i<=17)):
                subject=col[0].text
                max_min=col[9].text
                mark=col[10].text
                cgpa=col[11].text
                temp["subjects"].append([subject,max_min,mark,cgpa])
                i=i+1
            else:
                i=i+1
        col = row[18].find_all("th")
        max_score=col[2].text
        min_score=col[4].text
        marks_obtained=col[10].text
        cgpa_obtained=col[12].text
        temp["total"].append([max_score,min_score,marks_obtained,cgpa_obtained])
        results["results"][5]=temp 
        temp = {"subjects":[],"total":[]}
    except:
        return
    
def extract_forth_sem_data(year,roll_number):
    try:
        driver.get("https://exam.bujhansi.ac.in/frmViewCampusResult.aspx?cd=MwA4ADAA")
        Session = driver.find_element("id","ddlSession")
        select = Select(Session)
        select.select_by_visible_text(year)
        course = driver.find_element("id","ddlCourse")
        select = Select(course)
        select.select_by_visible_text("B.Tech (Computer Science & Engg) IV Semester")
        roll = driver.find_element("id","txtUniqueID")
        roll.clear()
        roll.send_keys(roll_number)
        ResultType = driver.find_element("id","ddlResultType")
        select = Select(ResultType)
        select.select_by_visible_text("Main")
        submit = driver.find_element("id","btnGetResult")
        submit.click()
        html = driver.page_source
        soup=BeautifulSoup(html,"html.parser")
        table=soup.find(id="tblMarksContent")
        temp = {"subjects":[],"total":[]}
        i=5
        row = table.find_all("tr")
        while i<18:
            col = row[i].find_all("td")
            if((i>=5 and i<10) or (i>=13 and i<=17)):
                subject=col[0].text
                max_min=col[9].text
                mark=col[10].text
                cgpa=col[11].text
                temp["subjects"].append([subject,max_min,mark,cgpa])
                i=i+1
            else:
                i=i+1
        col = row[19].find_all("th")
        max_score=col[2].text
        min_score=col[4].text
        marks_obtained=col[10].text
        cgpa_obtained=col[12].text
        temp["total"].append([max_score,min_score,marks_obtained,cgpa_obtained])
        results["results"][4]=temp 
        temp = {"subjects":[],"total":[]}
    except:
        return
    
    
def extract_third_sem_data(year,roll_number):
    try:
        driver.get("https://exam.bujhansi.ac.in/frmViewCampusResult.aspx?cd=MwA4ADAA")
        Session = driver.find_element("id","ddlSession")
        select = Select(Session)
        select.select_by_visible_text(year)
        course = driver.find_element("id","ddlCourse")
        select = Select(course)
        select.select_by_visible_text("B.Tech (Computer Science & Engg) III Semester")
        roll = driver.find_element("id","txtUniqueID")
        roll.clear()
        roll.send_keys(roll_number)
        ResultType = driver.find_element("id","ddlResultType")
        select = Select(ResultType)
        select.select_by_visible_text("Main")
        submit = driver.find_element("id","btnGetResult")
        submit.click()
        html = driver.page_source
        soup=BeautifulSoup(html,"html.parser")
        table=soup.find(id="tblMarksContent")
        temp = {"subjects":[],"total":[]}
        i=5
        row = table.find_all("tr")
        while i<18:
            col = row[i].find_all("td")
            if((i>=5 and i<10) or (i>=13 and i<=17)):
                subject=col[0].text
                max_min=col[9].text
                mark=col[10].text
                cgpa=col[11].text
                temp["subjects"].append([subject,max_min,mark,cgpa])
                i=i+1
            else:
                i=i+1
        col = row[19].find_all("th")
        max_score=col[2].text
        min_score=col[4].text
        marks_obtained=col[10].text
        cgpa_obtained=col[12].text
        temp["total"].append([max_score,min_score,marks_obtained,cgpa_obtained])
        results["results"][3]=temp 
        temp = {"subjects":[],"total":[]}
    except:
        return
    
def extract_second_sem_data(year,roll_number):
    try:
        driver.get("https://exam.bujhansi.ac.in/frmViewCampusResult.aspx?cd=MwA4ADAA")
        Session = driver.find_element("id","ddlSession")
        select = Select(Session)
        select.select_by_visible_text(year)
        course = driver.find_element("id","ddlCourse")
        select = Select(course)
        select.select_by_visible_text("B.Tech (Computer Science & Engg) II Semester")
        roll = driver.find_element("id","txtUniqueID")
        roll.clear()
        roll.send_keys(roll_number)
        ResultType = driver.find_element("id","ddlResultType")
        select = Select(ResultType)
        select.select_by_visible_text("Main")
        submit = driver.find_element("id","btnGetResult")
        submit.click()
        html = driver.page_source
        soup=BeautifulSoup(html,"html.parser")
        table=soup.find(id="tblMarksContent")
        temp = {"subjects":[],"total":[]}
        i=5
        row = table.find_all("tr")
        while i<18:
            col = row[i].find_all("td")
            if((i>=5 and i<11) or (i>=14 and i<=18)):
                subject=col[0].text
                max_min=col[9].text
                mark=col[10].text
                cgpa=col[11].text
                temp["subjects"].append([subject,max_min,mark,cgpa])
                i=i+1
            else:
                i=i+1
        col = row[20].find_all("th")
        max_score=col[2].text
        min_score=col[4].text
        marks_obtained=col[10].text
        cgpa_obtained=col[12].text
        temp["total"].append([max_score,min_score,marks_obtained,cgpa_obtained])
        results["results"][2]=temp 
        temp = {"subjects":[],"total":[]}
    except:
        return 

    
def extract_first_sem_data(year,roll_number,branch):
    try:
        driver.get("https://exam.bujhansi.ac.in/frmViewCampusResult.aspx?cd=MwA4ADAA")
        Session = driver.find_element("id","ddlSession")
        select = Select(Session)
        select.select_by_visible_text(year)
        course = driver.find_element("id","ddlCourse")
        select = Select(course)
        select.select_by_visible_text("B.Tech (Computer Science & Engg) I Semester")
        roll = driver.find_element("id","txtUniqueID")
        roll.clear()
        roll.send_keys(roll_number)
        ResultType = driver.find_element("id","ddlResultType")
        select = Select(ResultType)
        select.select_by_visible_text("Main")
        submit = driver.find_element("id","btnGetResult")
        submit.click()
        html = driver.page_source
        soup=BeautifulSoup(html,"html.parser")
        enrolment_number = soup.find(id="lblenrollNo").text
        father_name = soup.find(id="lblFatherName").text
        mother_name = soup.find(id="lblMotherName").text
        student_name = soup.find(id="lblCandidateName").text
        profile_photo = soup.find(id="imgStudentPic")["src"]
        results["profile"]["profile"]=[roll_number,year,enrolment_number,father_name,mother_name,student_name,profile_photo,branch] 
        table=soup.find(id="tblMarksContent")
        temp = {"subjects":[],"total":[]}
        i=5
        row = table.find_all("tr")
        while i<18:
            col = row[i].find_all("td")
            if((i>=5 and i<10) or (i>=13 and i<=18)):
                subject=col[0].text
                max_min=col[9].text
                mark=col[10].text
                cgpa=col[11].text
                temp["subjects"].append([subject,max_min,mark,cgpa])
                i=i+1
            else:
                i=i+1
        col = row[20].find_all("th")
        max_score=col[2].text
        min_score=col[4].text
        marks_obtained=col[10].text
        cgpa_obtained=col[12].text
        temp["total"].append([max_score,min_score,marks_obtained,cgpa_obtained])
        results["results"][1]=temp 
        temp = {"subjects":[],"total":[]}
    except:
        return

app = Flask(__name__)
CORS(app)
# endpiont at which we get results of students
# http://localhost:5000/results
@app.route('/results', methods=['POST'])
def find_results():
    data = request.get_json()
    year = data.get("year")
    roll = data.get('roll')
    branch = data.get('branch')
    current_sem = (data.get("current_sem")/2)
    num = int(year[2:4])
    driver.maximize_window()
    if current_sem ==0:
        return jsonify({'results': "You are in first year , try when you are in second year"}), 201
    elif current_sem ==1:
        extract_first_sem_data(year[:2]+ str(num) +year[4:5]+str(num+1),roll,branch)
        extract_second_sem_data(year[:2]+ str(num) +year[4:5]+str(num+1),roll)
        driver.minimize_window()
        return jsonify({'results': results}), 201
    elif current_sem ==2:
        extract_first_sem_data(year[:2]+ str(num) +year[4:5]+str(num+1),roll,branch)
        extract_second_sem_data(year[:2]+ str(num) +year[4:5]+str(num+1),roll)
        num=num+1
        extract_third_sem_data(year[:2]+ str(num) +year[4:5]+str(num+1),roll)
        extract_forth_sem_data(year[:2]+ str(num) +year[4:5]+str(num+1),roll)
        driver.minimize_window()
        return jsonify({'results': results}), 201
    elif current_sem ==3:
        extract_first_sem_data(year[:2]+ str(num) +year[4:5]+str(num+1),roll,branch)
        extract_second_sem_data(year[:2]+ str(num) +year[4:5]+str(num+1),roll)
        num=num+1
        extract_third_sem_data(year[:2]+ str(num) +year[4:5]+str(num+1),roll)
        extract_forth_sem_data(year[:2]+ str(num) +year[4:5]+str(num+1),roll)
        num=num+1
        extract_fifth_sem_data(year[:2]+ str(num) +year[4:5]+str(num+1),roll)
        extract_sixth_sem_data(year[:2]+ str(num) +year[4:5]+str(num+1),roll)
        driver.minimize_window()
        return jsonify({'results': results}), 201
    elif current_sem ==4:
        extract_first_sem_data(year[:2]+ str(num) +year[4:5]+str(num+1),roll,branch)
        extract_second_sem_data(year[:2]+ str(num) +year[4:5]+str(num+1),roll)
        num=num+1
        extract_third_sem_data(year[:2]+ str(num) +year[4:5]+str(num+1),roll)
        extract_forth_sem_data(year[:2]+ str(num) +year[4:5]+str(num+1),roll)
        num=num+1
        extract_fifth_sem_data(year[:2]+ str(num) +year[4:5]+str(num+1),roll)
        extract_sixth_sem_data(year[:2]+ str(num) +year[4:5]+str(num+1),roll)
        num=num+1
        extract_seventh_sem_data(year[:2]+ str(num) +year[4:5]+str(num+1),roll)
        extract_eighth_sem_data(year[:2]+ str(num) +year[4:5]+str(num+1),roll)
        driver.minimize_window()
        return jsonify({'results': results}), 201
    elif current_sem ==5:
        extract_first_sem_data(year[:2]+ str(num) +year[4:5]+str(num+1),roll,branch)
        extract_second_sem_data(year[:2]+ str(num) +year[4:5]+str(num+1),roll)
        num=num+1
        extract_third_sem_data(year[:2]+ str(num) +year[4:5]+str(num+1),roll)
        extract_forth_sem_data(year[:2]+ str(num) +year[4:5]+str(num+1),roll)
        num=num+1
        extract_fifth_sem_data(year[:2]+ str(num) +year[4:5]+str(num+1),roll)
        extract_sixth_sem_data(year[:2]+ str(num) +year[4:5]+str(num+1),roll)
        num=num+1
        extract_seventh_sem_data(year[:2]+ str(num) +year[4:5]+str(num+1),roll)
        extract_eighth_sem_data(year[:2]+ str(num) +year[4:5]+str(num+1),roll)
        driver.minimize_window()
        return jsonify({'results': results}), 201
    return jsonify({'results': results}), 201





if __name__ == '__main__':
    app.run(debug=True)


