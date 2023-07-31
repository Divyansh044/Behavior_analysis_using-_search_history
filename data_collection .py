from Analyze_Behavioural_Data import cv, classifier3
from get_data import final_list


# ##################### TESTING CUSTOM INPUTS ##############################
# #
# # ################ If you want to take user history automatically ################
def feed_automatic():

 entertainment = 0
 study = 0
 predict_res = 0
 feed_list = []
for item in final_list:
 feed_list.append(item)
 feed_list1 = cv.transform(feed_list).toarray()
 predict_res = int(classifier3.predict(feed_list1))
 print(type(predict_res))
if predict_res == 0:
  entertainment += 1
else:
   study += 1
feed_list.clear()
print("Entertainment - ",entertainment,"Study - ", study)
#
# ########## If you want to insert something from your side ##############
# # 1 - Study and 0 - Entertainment

string = input("Enter a string-->")
new = []
new.append(string)
new = cv.transform(new).toarray()
custom_predict = classifier3.predict(new)
print(custom_predict)
if custom_predict == 0:
 print("User is Interested in Entertainment and fun")
else:
   print("User is interested in Education related content")
