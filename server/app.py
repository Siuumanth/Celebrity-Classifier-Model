from flask import Flask, request, jsonify,render_template
import util
import cv2,urllib,numpy as np


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('app copy.html')

@app.route('/classify', methods=['GET', 'POST'])
def classify_image():
    if request.method=='POST':
        link=str(request.form['link'])

        req = urllib.request.urlopen(link)
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        image = cv2.imdecode(arr, -1)
        
        try:
            response = util.classify_image(image,file_path=None)
            """           
            for dic in response:
                dic2=dic['class_probability']
                for i in dic2:
                    if i>70:
                        prob = dic2
                    else:
                        return jsonify({"error":"cannot classify image properly"})
                        """
            celeb=findhim(response[0]['class'])
            link=findlink(celeb)
            prob=response[0]['class_probability']
            return render_template('app.html',fceleb=celeb,celeblink=link,pmessi=prob[0],pmaria=prob[1],proger=prob[2],pserena=prob[3],pvirat=prob[4])
        
                    


        except:
            return jsonify({"error":"cannot classify image "})
        
        


 
        
            return render_template('app.html',fceleb=celeb,celeblink=link,pmessi=prob[0],pmaria=prob[1],proger=prob[2],pserena=prob[3],pvirat=prob[4])



def findhim(lis):
    cel=["Lionel Messi", "Maria Sharapova", "Roger Federer", "Serena Williams","Virat Kohli"]
    dic=["lionel_messi", "maria_sharapova", "roger_federer", "serena_williams", "virat_kohli"]
    result=''
    for i in range(5):
        if lis==dic[i]:
            result=cel[i]
    return result   

def findlink(guy):
    cel=["Lionel Messi", "Maria Sharapova", "Roger Federer", "Serena Williams","Virat Kohli"]
    last=['messi.jpeg','sharapova.jpeg','federer.jpeg','serena.jpeg','virat.jpeg']
    for i in range(5):
        if guy==cel[i]:
            return "C:/Users/gsuma/OneDrive/Desktop/githubstud/Celebrity-Classifier-Model/server/images/ " + last[i]




if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000,debug=True)