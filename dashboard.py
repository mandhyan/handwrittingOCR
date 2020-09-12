from flask import Flask,render_template,request
import cv2
import numpy as np
import base64
import json


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('show.html')


def processData():
	test_img= cv2.imread('test.png')
	with np.load('knn_data.npz') as data:

		train = data['train']
		train_labels = data['train_labels']

	knn = cv2.ml.KNearest_create()
	knn.train(train, cv2.ml.ROW_SAMPLE, train_labels) 
	test_img =cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
	someImg=test_img
	test_img =cv2.resize(test_img, (20, 20)) 
	x = np.array(test_img)
	test_img = x.reshape(-1,400).astype(np.float32)
	ret,result,neighbours,dist = knn.findNearest(test_img,k=1)
	#print (ret,result,neighbours,dist)
	return (int(result))



@app.route('/getImage',methods=['POST'])
def getImage():

	imagefile = request.form.get('imgBase64')
	part = imagefile.split(',')[1]
	
	image= base64.b64decode(part)
	#image= cv2.imdecode(image,cv2.IMREAD_COLOR)

	answer= processData()
	return json.dumps({"Answer":answer}),200

if __name__ == '__main__':
	app.run(debug=True)