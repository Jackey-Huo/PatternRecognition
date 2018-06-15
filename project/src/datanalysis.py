import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
plt.plot(range(10))
plt.close()

import numpy as np
import lib

filename = "futuresData/0-20170704-day.log"

def plot_contract(dic, contract_name="A1", st=0, ed=1000):
    for k, v in dic[contract_name].items():
        plt.plot(v[st:ed])
        plt.savefig("fig/" + contract_name + "_" + k + "_" + str(st) + "_" + str(ed) + ".png")
        plt.close()

def plot_compare(dic, contract_name=["A1", "A3", "B2", "B3"], st=0, ed=1000, comp=["askPrice1", "bidPrice1"], ifNorm=True):
    colors = "rgbc"
    for cname in contract_name:
        name = cname
        if len(dic[cname].keys()) < 2:
            print(cname + " not exist")
            continue

        for i, k in enumerate(comp):
            c = colors[i]
            name = name + "_" + k
            if ifNorm and k.find("slope") == -1:
                x = dic[cname][k][st:ed].astype("float32")
                plt.plot(range(st, ed), (x-x.min())/(x.max()-x.min()), c)
                #plt.plot(x, c)
            else:
                plt.plot(range(st, ed), dic[cname][k][st:ed], c)
        
        plt.savefig("fig/" + name + "_" + str(st) + "_" + str(ed) + ".png")
        plt.close()

def print_contract(dic, contract_name='A1', st=0, ed=1000, printItems=["askPrice1", "bidPrice1"]):
    pass


def get_figures(dic):
    lib.analysis_diff_ask_bid(dic)
    plot_contract(dic, st=5000, ed=6000)

raw_data = lib.read_text(filename)

dic = lib.extract_data(raw_data)

lib.get_mean_price(dic)
lib.get_fit_slope(dic)
lib.denote_dataset(dic)
lib.show_label(dic, st=5000, ed=10000)
lib.show_label(dic, contract_name="A3", st=5000, ed=10000)
print(dic["A1"].keys())
plot_compare(dic, comp=['bidPrice1', "meanPrice200", "slopePrice40"], st=5000, ed=10000, ifNorm=True)
plot_compare(dic, comp=['askPrice1', 'bidPrice1'], st=0, ed=1000, ifNorm=False)
lib.analysis_diff_ask_bid(dic)
#get_figures(dic)