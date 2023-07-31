import browserhistory as bh
from Analyze_Behavioural_Data import classifier1, cv


def automatic_history_collection():

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


