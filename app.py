from flask import Flask, render_template, redirect, url_for, flash
from forms.form import ContactForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route('/')
def homepage():

    title = "Epic Tutorials"
    paragraph = ["wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!","wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!"]

    try:
        return render_template("index.html", title = title, paragraph=paragraph)
    except Exception(e):
        return str(e)

@app.route('/about.html')
def aboutPage():

    title = "About VIP Humor Genome"
    paragraph = ["blah blah blah memememememmeme blah blah memememe"]

    pageType = 'about'

    return render_template("about.html", title=title, paragraph=paragraph, pageType=pageType)


@app.route('/index.html')
def homePage():

    title = "About this site"
    paragraph = ["blah blah blah memememememmeme blah blah memememe"]

    pageType = 'about'

    return render_template("index.html", title=title, paragraph=paragraph, pageType=pageType)

@app.route('/subteam.html')
def subteamPage():

    title = "About this site"
    paragraph = ["blah blah blah memememememmeme blah blah memememe"]

    pageType = 'about'

    return render_template("subteam.html", title=title, paragraph=paragraph, pageType=pageType)

@app.route('/contact.html', methods=['get', 'post'])
def contactPage():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Your message was sent!')
        first = form.first.data
        last = form.last.data
        email = form.email.data
        body = form.body.data
        print((first, last, email, body))
        return redirect(url_for('contactPage'))
    return render_template("contact.html", form=form)

if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0', port=8080, passthrough_errors=True)
