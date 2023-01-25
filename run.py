from flask import Flask, render_template

# create a flask instance
app = Flask(__name__)



# Routes




# Home Page
@app.route('/')
def index():
    return render_template('/index.html')




if __name__ == "__main__":
    app.run(debug=True)