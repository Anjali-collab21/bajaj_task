import requests

user_data = {
    "name": "John Doe",
    "regNo": "REG12347",
    "email": "john@example.com"
}


generate_url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
response = requests.post(generate_url, json=user_data)

if response.status_code == 200:
    data = response.json()
    webhook_url = data.get("webhook")
    access_token = data.get("accessToken")

    print("Webhook URL:", webhook_url)
    print("Access Token:", access_token)

SQL_Query = """
 SELECT 
 p.AMOUNT AS SALARY,
 CONCAT(e.FIRST_NAME, ' ', e.LAST_NAME) AS NAME,
 TIMESTAMPDIFF(YEAR, e.DOB, CURDATE()) AS AGE,
 d.DEPARTMENT_NAME
 FROM PAYMENTS p
 JOIN EMPLOYEE e ON p.EMP_ID = e.EMP_ID
 JOIN DEPARTMENT d ON e.DEPARTMENT = d.DEPARTMENT_ID
 WHERE DAY(p.PAYMENT_TIME) != 1
 ORDER BY p.AMOUNT DESC
 LIMIT 1;
 """

headers = {
    "Authorization": "eyJhbGciOiJIUzI1NiJ9.eyJyZWdObyI6IlJFRzEyMzQ3IiwibmFtZSI6IkpvaG4gRG9lIiwiZW1haWwiOiJqb2huQGV4YW1wbGUuY29tIiwic3ViIjoid2ViaG9vay11c2VyIiwiaWF0IjoxNzQ2OTYwMzIyLCJleHAiOjE3NDY5NjEyMjJ9.YatQ7QZhxPPXbanbeVl_rWGI5izvj0BKFLBe1URBSew" ,
    "Content-Type": "application/json"
    }

submission_response = requests.post(
        webhook_url,
        headers=headers,
        json={"FinalQuery": SQL_Query})

if submission_response.status_code == 200:
    print("Query submitted successfully")
else:
    print("Error submitting query:", submission_response.status_code)
    print(submission_response.text)
