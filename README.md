An AI model that can classify images of celebrities into the respective class
As of now , different images of 5 sports person have been fed into the model so it can differentiate between those 5 only
Messi,Virat Kohli, Roger Federer, Serene Williams and Maria Sharapova

No UI has been created yet, just the model and the backend for it.....yeah weird i know, i just hate frontend very much

The model uses haar cascades and wavelet transform to extract features and train the model.


If you want to test the model, go to "model/classification_model.py", and run the find_celeb method with your image file path
or you can go to "server/util.py" , enter base64 value of the image in the method and run the file to get all the probabilities
