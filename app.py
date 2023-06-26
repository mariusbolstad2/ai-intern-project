import json
import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        input = request.form["chat-input"]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
             messages= [
                            {"role": "user", "content": generate_prompt(input=input)},
                        ],
            temperature=0.6
        )
        return redirect(url_for("index", result=response.choices[0].message.content))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(input):
    with open('dummy-data.json') as file:
        data = json.load(file)

    # Dump JSON data as a string
    json_string = json.dumps(data)
    prompt = "here is the relevant data structure for the question: " + '{"invoice_number": "KpoOqMlU", "customer_name": "GzzpuHvvYh", "amount": 372.71, "vat_percentage": 5, "konstnadskonto": 1758, "due_date": "2023-06-12"}' + " ---- Here is the data: " + json_string + "------ Here is the question: " + input
    print(prompt)
    return prompt