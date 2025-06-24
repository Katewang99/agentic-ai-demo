from flask import Flask, render_template, request
import google.generativeai as genai
import os

app = Flask(__name__)

# 设置 API KEY
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form
        prompt = f"""
以下是一位高中生的背景资料，请根据这些信息推荐美国大学，并按冲刺校、匹配校、保底校分类，附简要推荐理由。
请同时提供选校策略建议，以及文书写作结构建议：

🎯 人格测评结果:
- 学习风格: {data.get("learning_style")}
- 性格开放性: {data.get("openness")}
- 责任感: {data.get("responsibility")}
- 抗压程度: {data.get("stress")}
- 文化偏好: {data.get("culture_fit")}
- 动机驱动: {data.get("motivation")}
- 社交风格: {data.get("social")}

📘 学术背景:
- GPA: {data.get("gpa")} （课程体系: {data.get("system")}）
- 托福: {data.get("toefl")} | SAT: {data.get("sat")}

📌 经历: {data.get("experience")}
🌍 留学偏好: {data.get("country")} | 预算: {data.get("budget")} | 学位: {data.get("degree")} | 类型: {data.get("school_type")}
💼 未来规划: 工作国家: {data.get("career_country")} | 入学时间: {data.get("start_date")} | 职业方向: {data.get("career_direction")}
        """
        response = model.generate_content(prompt)
        return render_template("result.html", result=response.text)

    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
