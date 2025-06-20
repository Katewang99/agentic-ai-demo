from flask import Flask, render_template, request
import google.generativeai as genai
import os

app = Flask(__name__)

# Gemini API key
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        gpa = request.form["gpa"]
        toefl = request.form["toefl"]
        sat = request.form["sat"]
        major = request.form["major"]
        intern = request.form["intern"]
        extra = request.form["extra"]

        prompt = f"""
以下是一位高中生的背景资料，请根据这些信息推荐美国大学，并按冲刺校、匹配校、保底校分类，附简要推荐理由。
并请给出选校策略建议，以及文书写作结构建议（列出各段主题及可用中文表达）。

学生背景：
GPA：{gpa}
托福：{toefl}
SAT：{sat}
意向专业：{major}
实习经历：{intern}
其他补充信息：{extra}
"""

        response = model.generate_content(prompt)
        result = response.text

    return render_template("index.html", result=result)
