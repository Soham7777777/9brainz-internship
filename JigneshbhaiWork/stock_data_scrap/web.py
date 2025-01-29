from flask import Flask, request, render_template
import tool
from tool import driver_context, print_warning, print_info


app = Flask(__name__)
driver = driver_context(True)


@app.get('/')
def home() -> str:
    url = request.args.get("url")
    print_info("URL: " + str(url))
    print_warning("="*20+"Getting the data"+"="*20)
    data = tool.main(url, driver)
    if not any(data):
        return "<h1>NO DATA</h1>"    
    return render_template("index.html", data=data)


def main() -> None:
    app.run(debug=True)


if __name__ == "__main__":
    main()
