from flask import Flask, request, jsonify,render_template
import util
import cv2,urllib,numpy as np


app = Flask(__name__)


@app.route("/")
def home():
    util.load_saved_artifacts()
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
                    
            test=[]
            for dic in response:
                dic2=dic['class_probability']
                for i in dic2:
                   test.append(i)

            max=test[0]  
            best=int(test.index(max)/5)      
            for i in test:
                if i>max:
                    best=int(test.index(i)/5)
                    max=i
 
            if response==[]:
                 return jsonify({"error":"cannot classify image properly"})

        
        
            c=response[best]['class']
            celeb=findhim(c)
            link=findlink(celeb)
            prob=response[best]['class_probability']
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
            return  last[i]  




if __name__ == "__main__":
    app.run(debug=True)