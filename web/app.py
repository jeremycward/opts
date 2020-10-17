from flask import Flask, request, render_template

from web.forms import EvalForm

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route('/options', methods=['GET', 'POST'])
def register():
    form = EvalForm(request.form)
    return render_template('eval.html', form=form)

