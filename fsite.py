from cgitb import text
from flask import Flask, render_template
from flask import request


app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def screen():
    if request.method == "POST":
        # gets sec end video and tier gold ore
        secs = request.form.get('secs')
        tier = request.form.get('size')
        print(secs, tier)
        pass    
    f = open("static/css/text.txt")
    txt = [x.replace("\n", "") for x in f]
    f.close()
    return render_template("index.html", text1=txt[0], text2=txt[1], text3=txt[2], text4=txt[3])

# @app.route("/", methods=["POST"])
# def display_video():
# 	#print('display_video filename: ' + filename)
# 	return redirect(url_for('static', filename="video.mp4"))

if __name__ == "__main__":
    app.run(debug=True)