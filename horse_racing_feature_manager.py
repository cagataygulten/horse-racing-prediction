import pandas as pd
import numpy as np
import time
from multiprocessing import Process


def calculate_new_features(df1, y1, y2):
    st = time.time()
    length = len(df1)
    average = 0
    sum_calc_time = 0

    output_yz1_list = []
    output_yz2_list = []
    output_yz3_list = []
    output_yz4_list = []

    for index, row in df1.iterrows():
        lst = time.time()
        tf = np.where(df1[y1].values == row[y1], True, False)
        tf2 = np.where(df1[tf][y2].values == row[y2], True, False)

        # print("alt tablo süresi : "+str(time.time()-lst))

        df_processed = df1[tf][tf2]
        toplam_kosu = len(df_processed)
        ilk_4 = len(df_processed[df_processed["sira"] < 5])
        ilk_3 = len(df_processed[df_processed["sira"] < 4])
        ilk_2 = len(df_processed[df_processed["sira"] < 3])
        ilk_1 = len(df_processed[df_processed["sira"] < 2])

        # print("sıra bulma süresi : "+str(time.time()-lst))

        if toplam_kosu == 0:
            yz1 = 0
            yz2 = 0
            yz3 = 0
            yz4 = 0
        else:
            yz1 = ilk_1 / toplam_kosu
            yz2 = ilk_2 / toplam_kosu
            yz3 = ilk_3 / toplam_kosu
            yz4 = ilk_4 / toplam_kosu

        output_yz1_list.append(yz1)
        output_yz2_list.append(yz2)
        output_yz3_list.append(yz3)
        output_yz4_list.append(yz4)

        # print("sıra yazma süresi : "+str(time.time()-lst))

        calc_time = (time.time() - lst) * length
        sum_calc_time += calc_time
        if index != 0:
            average = sum_calc_time / index

        lt = time.strftime('%H:%M:%S', time.gmtime(average))
        g = time.strftime('%H:%M:%S', time.gmtime(time.time() - st))

        print(str(y1)+"-"+str(y2)+" / Estimated Total Time = " + str(lt) + " / Current Index = " + str(index) + " / Percentage = " + str(
            round(index / length * 100)) + " % / Time elapsed = " + str(g), end="\n")

    temp_dict = {"yz1": output_yz1_list, "yz2": output_yz2_list, "yz3": output_yz3_list, "yz4": output_yz4_list}
    df_temp = pd.DataFrame(temp_dict)
    df_temp.to_csv(str(y1) + "_" + str(y2) + ".csv")

def calculate_new_features_one_input(df1, y1):
    st = time.time()
    length = len(df1)
    average = 0
    sum_calc_time = 0

    output_yz1_list = []
    output_yz2_list = []
    output_yz3_list = []
    output_yz4_list = []

    for index, row in df1.iterrows():
        lst = time.time()
        tf = np.where(df1[y1].values == row[y1], True, False)

        # print("alt tablo süresi : "+str(time.time()-lst))

        df_processed = df1[tf]
        toplam_kosu = len(df_processed)
        ilk_4 = len(df_processed[df_processed["sira"] < 5])
        ilk_3 = len(df_processed[df_processed["sira"] < 4])
        ilk_2 = len(df_processed[df_processed["sira"] < 3])
        ilk_1 = len(df_processed[df_processed["sira"] < 2])

        # print("sıra bulma süresi : "+str(time.time()-lst))

        if toplam_kosu == 0:
            yz1 = 0
            yz2 = 0
            yz3 = 0
            yz4 = 0
        else:
            yz1 = ilk_1 / toplam_kosu
            yz2 = ilk_2 / toplam_kosu
            yz3 = ilk_3 / toplam_kosu
            yz4 = ilk_4 / toplam_kosu

        output_yz1_list.append(yz1)
        output_yz2_list.append(yz2)
        output_yz3_list.append(yz3)
        output_yz4_list.append(yz4)

        # print("sıra yazma süresi : "+str(time.time()-lst))

        calc_time = (time.time() - lst) * length
        sum_calc_time += calc_time
        if index != 0:
            average = sum_calc_time / index

        lt = time.strftime('%H:%M:%S', time.gmtime(average))
        g = time.strftime('%H:%M:%S', time.gmtime(time.time() - st))

        print(str(y1)+" / Estimated Total Time = " + str(lt) + " / Current Index = " + str(index) + " / Percentage = " + str(
            round(index / length * 100)) + " % / Time elapsed = " + str(g), end="\n")

    temp_dict = {"yz1": output_yz1_list, "yz2": output_yz2_list, "yz3": output_yz3_list, "yz4": output_yz4_list}
    df_temp = pd.DataFrame(temp_dict)
    df_temp.to_csv(str(y1)  + ".csv")

if __name__ == '__main__':

    df1=pd.read_csv("tjk_data_raw_mesafe_cat.csv")

    p1 = Process(target=calculate_new_features, args=(df1, "atid_id", "sehir",))
    p1.start()

    p2 = Process(target=calculate_new_features, args=(df1, "atid_id", "pist",))
    p2.start()

    p3 = Process(target=calculate_new_features, args=(df1, "anneid_id", "pist",))
    p3.start()

    p4 = Process(target=calculate_new_features, args=(df1, "babaid_id", "pist",))
    p4.start()

    p5 = Process(target=calculate_new_features, args=(df1, "anneid_id", "mesafe_cat",))
    p5.start()

    p6 = Process(target=calculate_new_features, args=(df1, "babaid_id", "mesafe_cat",))
    p6.start()

    p7 = Process(target=calculate_new_features_one_input, args=(df1,"anneid_id",))
    p7.start()

    p8 = Process(target=calculate_new_features_one_input, args=(df1,"babaid_id",))
    p8.start()

    p9 = Process(target=calculate_new_features_one_input, args=(df1, "jokeyid_id",))
    p9.start()

    p10 = Process(target=calculate_new_features, args=(df1, "atid_id", "mesafe_cat",))
    p10.start()
