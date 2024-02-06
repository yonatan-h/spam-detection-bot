from logistic_regression import LogisticRegression
from extract_features import extract_features
import os 
import json
import numpy as np

dir_path = os.path.dirname(os.path.realpath(__file__))
preprocess_data = json.load(open(os.path.join(dir_path,"data","preprocess.json")))
print('extracting pre process data...')
model_data = json.load(open(os.path.join(dir_path,"data", "model.json")))
print('extracting model data')
weights = np.array(model_data["weights"])

def predict(message):
    print(f'Predicting if {message} is spam or not...')
    lr = LogisticRegression(w=weights)
    print(f'Initialized logistic regression')
    x= extract_features(message, preprocess_data)
    x_as_string = " ".join( map(lambda n:str(int(n)), x.tolist())) 
    print(f'Extracted features from message: {x_as_string}')
    X = np.array([x])
    print(f'Predicting...')
    predicted = lr.predict_solid(X)[0]
    print(f'Predicted: {"spam" if predicted == 1 else "ham"}')
    return predicted == 1


# print(predict(""))
# print(predict("network sint eyaswetagn new yekoyehut bizu screenshoot yizalehu hayuta ahun rasu eyasgebagn aydelemHello, how are you?") )
# print(predict("Yared Yenealem is inviting you to a scheduled Zoom meeting.  Topic: Yared Yenealem's Personal Meeting Room Join Zoom Meeting https://us04web.zoom.us/j/6841482527?pwd=jF3bTbsARra6m7AYqIKAhQXP3oKzXq.1 Meeting ID: 684 148 2527 Passcode: CrZ3H0buy our product now for free") )
# print(predict("Guys, could you please make the DS and ML project deadlines after the final exam?  But I want to ask that all of you think the time is enough for a project, in case some of you have finished.") )
# print(predict("You can refer to our srs and sds document for information You can also use already made document for template i will share them here"))
# print(predict("For college and University students, if you need support on Masters degree and Bachelor's degree academic tasks such as:- ✅Research ✅Assignment ✅PROJECTS* 🟢Business plan 💯%🅿️ PLAGIARISM 🆓 💯%🅿️ PLAGIARISM 🆓 *OUR* *SERVICES* 📌 𝘈𝘤𝘤𝘶𝘳𝘢𝘵𝘦 𝘸𝘳𝘪𝘵𝘪𝘯𝘨 📌𝘗𝘭𝘢𝘨𝘪𝘢𝘳𝘪𝘴𝘮 𝘧𝘳𝘦𝘦 📌𝘛𝘪𝘮𝘦𝘭𝘺 𝘥𝘦𝘭𝘪𝘷𝘦𝘳𝘺.  📌𝘎𝘳𝘦𝘢𝘵 𝘤𝘭𝘪𝘦𝘯𝘵 𝘳𝘦𝘭𝘢𝘵𝘪𝘰𝘯𝘴𝘩𝘪𝘱.  🟢RESEARCH & ASSIGNMENT(MA, BA) 🎓Research Support 🎓Title selection 🎓Comment recorrection 🎓 Proposal For (MA,Msc, BA & Bsc ) 🎓Research editing 🎓Article review 🎓Any Assignment 🎓Book Review 🎓Term papers 🎓Case studies & case Analysis 🎓project work 🎓Individual or group assignments 🎓Research related tasks 🎓Title selection 🎓Title description and concept note 🎓Research  proposal 🎓Research for Graduation ( Thesis) 🎓Literature Reviews 🎓 business  plan 🎓Project Feasibility Study 🎓Comment  Correction and 🎓Mini Research 🎓project Business proposals 🎓Worksheet 🎓COC packages solving 🎓Case analysis 🎓CV 🎓Feasibility study 🎓Project Analysis 🎓Data Analysis 🎓In plant Study 🎓Business plan 🎓Essay Writing 🎓 Report Writing 🎓 Financial statement preparation ✅ለ SPSS, STATA ስልጠና የምትፈልጉ አናግሩን Research with SPSS software 💎Reliability test ♦️Correlation ♦️Regression ♦️multiple linear regression ✅Regression assumption 💎linearity test 💎normality test 💎multicollinearity test 💎Homoscedasticity test 💎ANOVA 💎MODEL SUMMARY 💎hypothesis testing 👇👇👇👇👇 0930524576 0912936468 0930524576 0913474199 👇👇👇👇👇👇👇 Telegram Chanel https://t.me/educatehere https://t.me/educatehere Or https://t.me/Assignmet_Research https://t.me/Assignmet_Research Or https://t.me/Assignment_Research https://t.me/Assignment_Research 👇👇👇👇👇👇👇👇👇 💯%🅿️ PLAGIARISM 🆓"))
