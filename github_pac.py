import  re
from flask import Flask, request
app = Flask(__name__)
@app.route('/urls', methods=['POST'])
def api():
    url = request.form.get('url')
    urls=url.replace(' ','%20')
    for u in urls.split(','):
        res=re.findall("(/blob/[0-9a-z]*/)",u)[0]
        github=u.replace("github.com","raw.githubusercontent.com").replace(res,"/master/")
        print(github)
    return urls
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9898)