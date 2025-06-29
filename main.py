import os
from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@app.route("/", methods=["GET", "POST"])
def index():
    reply = ""
    if request.method == "POST":
        fan_message = request.form["fanMessage"]
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{
                    "role":
                    "system",
                    "content":
                    "You are a flirty, emotionally intelligent chatbot who replies to OnlyFans fans in a playful, respectful tone."
                }, {
                    "role": "user",
                    "content": fan_message
                }])
            reply = response.choices[0].message.content
        except Exception as e:
            reply = f"Error: {e}"
    return render_template("index.html", reply=reply)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port, debug=True)
# import os
# from flask import Flask, render_template, request
# import openai

# app = Flask(__name__)
# openai.api_key = os.getenv("OPENAI_API_KEY")

# @app.route("/", methods=["GET", "POST"])
# def index():
#     reply = ""
#     if request.method == "POST":
#         fan_message = request.form["fanMessage"]
#         response = openai.ChatCompletion.create(
#             model="gpt-4",
#             messages=[{
#                 "role":
#                 "system",
#                 "content":
#                 "You are a flirty, emotionally intelligent chatbot who replies to OnlyFans fans in a playful, respectful tone."
#             }, {
#                 "role": "user",
#                 "content": fan_message
#             }])
#         reply = response["choices"][0]["message"]["content"]
#     return render_template("index.html", reply=reply)

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'Hello from Flask!'

# if __name__ == '__main__':
#   app.run(host='0.0.0.0', port=5000)
