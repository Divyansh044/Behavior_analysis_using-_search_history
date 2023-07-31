from tkinter import *
from Analyze_Behavioural_Data import classifier1, cv
import browserhistory as bh
import webbrowser
def GO():
    webbrowser.open('https://colab.research.google.com/drive/1wYGCSFVkvbViX5NLl5eqcLhWLqEgHA12?usp=sharing')

def manual_feed():
    # print("button clicked", string_data.get())
    new = []
    new.append(string_data.get())
    new = cv.transform(new).toarray()
    # print(type(new))
    custom_predict = classifier1.predict(new)
    if custom_predict == 0:
        result_label.config(text = "Intreseted in Entertainment")
    else:
        result_label.config(text="Intreseted in Education and Studies")


def automatic_feed():
    dict = bh.get_browserhistory()
    bh.write_browserhistory_csv()

    list1 = list(dict.values())
    res = [item for t in list1 for item in t]
    history_list = [item for t in res for item in t]
    # print(history_list)

    i = 1
    final_list = []
    while i < len(history_list):
        final_list.append(history_list[i])
        i += 3

    ## Final_list contains my latest chrome history
    # print(final_list)

    entertainment = 0
    study = 0
    predict_res = 0
    feed_list = []
    for item in final_list:
        feed_list.append(item)
        feed_list1 = cv.transform(feed_list).toarray()
        predict_res = int(classifier1.predict(feed_list1))
        # print(type(predict_res))
        if predict_res == 0:
            entertainment += 1
        else:
            study += 1
        feed_list.clear()
    if(entertainment > study):
        result_label.config(text = "User more Inclined towards Fun")
    else:
        result_label.config(text="User more Inclined towards Study")



root = Tk()
root.title('Behaviour Analysis')
root.geometry('666x444')

################## VARIABLES ################

string_data = StringVar()

#############################################

## for manual feeding
manual = Label( text='Enter a string :', font= ('comicsansms 14'), padx = 5, pady = 20)
manual.grid(row = 0, column = 0)

manual_entry = Entry(textvariable=string_data, font = ('Arial 10'))
manual_entry.grid(row = 0, column = 1)
## button to execture the function
B1 = Button(root, text = "RESULT", font = ('Arial 10 bold'), relief=SUNKEN, command = manual_feed)
B1.grid(row = 1, column = 1, sticky=W)


## Shows result for manual feed
result_label = Label(font = ('Arial 10 bold'),  borderwidth=10)
result_label.grid(row = 0, column = 2)


## For automatic history collection
B2 = Button(root, text = "AUTO RES", font = ('Arial 10 bold'), relief=SUNKEN, command = automatic_feed)
B2.grid(row = 1, column = 2, sticky=W)

### SOURCE CODE BUTTON ####################
B3 = Button(root, text = "SOURCE CODE", font = ('Arial 12 bold'), relief=SUNKEN, borderwidth= 3,
            command = GO, anchor= W)
B3.grid(row = 4, column = 0, sticky=W)
#############################

# ## to show result for automatic feed
result_label_auto = Label(font = ('Arial 10 bold'),  borderwidth=10)
result_label_auto.grid(row = 1, column = 3)


root.mainloop()