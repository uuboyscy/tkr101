from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
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

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
