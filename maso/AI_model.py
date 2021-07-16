import joblib #jbolib模块
import requests 

def HMC_estimate(X):
    #读取Model
    SVR = joblib.load('./AI_model/HMC_svr_model.pkl')

    X = [X]
    #测试读取后的Model
    SVR_prediction = SVR.predict(X)

    HMC_ = round(SVR_prediction[0],2)
    print('含水量%s％w.b.'%(str(HMC_)))

    return HMC_

import requests 
def download_model():
    url = 'https://976658e65208.ngrok.io/static/AI_Model/HMC_svr_model.pkl'
    res = requests.get(url)
    with open('./AI_model/HMC_svr_model.pkl','wb') as f:
        f.write(res.content)
        f.close()