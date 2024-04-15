from flask import Flask, request, jsonify,render_template
import util
import base64

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('app2.html')


@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    if request.method =='POST':
        if 'image' not in request.files:
            return jsonify({"error":"no image provided"}),400
        
        uploaded_file = request.files['image']
        image_data = uploaded_file.read()
        
       
      
        if uploaded_file:
            base64_image = base64.b64encode(image_data).decode('utf-8')

        res = jsonify(util.classify_image(image_data))

    return render_template('app.html',prediction=res)

   


    

   
    


    return response



@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded file from the request
    uploaded_file = request.files['imageFile']
    if uploaded_file:
        # Read the file content and convert it to base64
        image_data = uploaded_file.read()
        base64_image = base64.b64encode(image_data).decode('utf-8')
        
        # Send the base64 image to your model (replace this with your model code)
        # model_output = your_model_function(base64_image)

        # Example response (replace this with your model's response)
        model_output = {'result': 'Model received the image successfully.'}


if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(debug=True)






