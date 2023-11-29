from flask import Flask, render_template
from static import forumsContent

app = Flask(__name__)
allForums = forumsContent.getKeys()
@app.route('/')
def index():
    print(forumsContent.ourTeam)
    return render_template('index.html', forums = allForums,  team = forumsContent.ourTeam, questions = forumsContent.questionList)


@app.route('/schedule')
def schedule():
    return render_template('schedule.html',  forums = allForums)

@app.route('/executives')
def executives():
    return render_template('executives.html',  executives=forumsContent.executives, forums =allForums)

@app.route('/forums/<string:name>')
def forums(name):
    return render_template(
        'forums.html', forum = forumsContent.whichForum(name), n=name,  forums = allForums)

@app.route('/countryList')
def countryList():
    return render_template('countryList.html', forums=allForums)

@app.route('/codeofconduct')
def codeofconduct():
    return render_template('codeofconduct.html', forums=allForums, cocs = forumsContent.COC)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '8080', debug = True)



