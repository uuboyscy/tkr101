from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_test():
    return "Hello"

@app.route("/<name>")
def greet(name):
    return f"Hello {name} !"

# GET  /api/v1/get_empinfo/<bu>/<emp_id>
@app.route("/api/v1/get_empinfo/<bu>/<emp_id>")
def get_empinfo(bu, emp_id):
    sql = f"""
        select
            emp_name,
            emp_id,
            emp_bu,
            update_date
        from emp
        where bu = '{bu}'
        and emp_id = '{emp_id}';
    """
    # result = get_emp(sql)
    return {
        "emp_name": "Allen",
        "emp_id": "123",
        "emp_bu": "AAA",
        "update_date": "20250606",
    }

# /hello?username=Allen&age=22
@app.route("/hello")
def hello():
    username = request.args.get("username")
    age = request.args.get("age")
    if not username:
        return "Who are you?"
    if not age:
        return f"Hello {username}. How old are you?"
    return f"Hello {username}, you are {age} years old."


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
