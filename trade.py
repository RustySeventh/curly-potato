#!/usr/bin/python3
# -*- coding: iso-8859-1 -*
""" Python starter bot for the Crypto Trader games, from ex-Riddles.io """
__version__ = "1.0"

import sys
from bandes import *
from info import *
from calcul import *
from datetime import datetime
import math

def convert_time_stamp(timestamp):
    dt_object = datetime.fromtimestamp(timestamp)
    return dt_object.strftime("%Y-%m-%d %H:%M:%S")

class Bot:
    def __init__(self):
        self.botState = BotState()

    def run(self):
        while True:
            reading = input()
            if len(reading) == 0:
                continue
            self.parse(reading)
        print(f"Closing prices:", self.botState.closing_list, file=sys.stderr)


    def make_closing_list(self):
        self.botState.closing_list.clear()
        closes = self.botState.charts["USDT_BTC"].closes
        for close in closes:
            self.botState.closing_list.append(close)
        # print(f"Last closing price is {self.botState.closing_list[-1]}", file=sys.stderr)
        # print(f"The number of closing prices is {len(self.botState.closing_list)}", file=sys.stderr)

    # def buy_and_sell(self):
        # self.botState.list_closing_price.append(self.botState.charts["USDT_BTC"].closes[-1])
    def find_middleBB(self, array, period):
        tmp_list = []
        for i in range(period):
            tmp_list.append(array[-i])
        try:
            return (sum(tmp_list) / len(tmp_list))
        except ZeroDivisionError:
            pass
    
    def getStandardDeviation(self, array, period):
        deviationSum = 0
        tmp_list = array[-period:]
        average = statistics.mean(tmp_list)
        for i in tmp_list:
            deviationSum += pow((abs(i - average)), 2)
        res = (math.sqrt(deviationSum / period))
        # print(f"res {res}", file=sys.stderr)
        return res

    def parse(self, info: str):
        tmp = info.split(" ")
        if tmp[0] == "settings":
            self.botState.update_settings(tmp[1], tmp[2])
        if tmp[0] == "update":
            if tmp[1] == "game":
                self.botState.update_game(tmp[2], tmp[3])
                self.make_closing_list()
        if tmp[0] == "action":
            self.make_closing_list()
            middlebb = self.find_middleBB(self.botState.closing_list, self.botState.candlesGiven)
            # print(f"Middle bb is {middlebb:.2f}", file=sys.stderr)
            getstd = self.getStandardDeviation(self.botState.closing_list, self.botState.candlesGiven)
            # print(f"Standard deviation is {getstd:.2f}", file=sys.stderr)
            upperBB = middlebb + (getstd * 2)
            # print(f"upperBB {upperBB}", file=sys.stderr)
            lowerBB = middlebb - (getstd* 2)
            # print(f"lowerBB {lowerBB}", file=sys.stderr)
            mystack = self.botState.stacks["USDT"]
            # print(f"mystack {mystack}", file=sys.stderr)
            current_closing_price = self.botState.charts["USDT_BTC"].closes[-1]
            print(f"current_closing_price {current_closing_price}", file=sys.stderr)
            oneNumber = self.botState.stacks["USDT"] / self.botState.charts["USDT_BTC"].closes[-1]
            print(f"oneNumber {oneNumber}", file=sys.stderr)
            realtime = convert_time_stamp(self.botState.date)
            timestamp = self.botState.date
            print(f"realtime {realtime}", file=sys.stderr)
            print(f"timestamp {timestamp}", file=sys.stderr)
            buycrypto = oneNumber / 10


            if (middlebb < lowerBB):
                print(f"proutprout", file=sys.stderr)
                print(f"buy USDT_BTC {buycrypto}", flush=True)
            elif (middlebb > upperBB):
                print(f"proutprout", file=sys.stderr)
                print(f"sell USDT_BTC {buycrypto}", flush=True)
            else:     
                print("no_moves", flush=True)
            # if timestamp == 1621260000:
            #     print(f"realtime {realtime}", file=sys.stderr)
            #     print(f"timestamp {timestamp}", file=sys.stderr)
            #     print("no_moves", flush=True)
            

            
            
            # if (current_closing_price < lowerBB) and (mystack > buycrypto and timestamp != 1614556800):
            #     print(f"buy USDT_BTC {buycrypto}")
            # elif (current_closing_price > upperBB) and (self.botState.stacks["BTC"] > 0.0001 or timestamp == 1614556800):
            #     print(f"sell USDT_BTC {self.botState.stacks['BTC']}")
            # print(f"Closing prices:", self.botState.closing_list, file=sys.stderr)
            # This won't work every time, but it works sometimes!
            # dollars = self.botState.stacks["USDT"]
            # current_closing_price = self.botState.charts["USDT_BTC"].closes[-1]
            # affordable = dollars / current_closing_price
            # print(f'My stacks are {dollars}. The current closing price is {current_closing_price}. So I can afford {affordable}', file=sys.stderr)
            # buy, numberlist, slist, rlist, av  = fils_de_la_plage(current_closing_price, self.botState.numberlist, self.botState.slist, self.botState.rlist, self.botState.switchedCount, self.botState.i, self.botState.av)
            
            # print(f"buy is {buy}", file=sys.stderr)
            # real_time = convert_time_stamp(self.botState.date);
            # print(f"real time is {real_time}", file=sys.stderr)
            # arrLen = len(self.botState.charts["USDT_BTC"].volumes) - 1
            # arrSum = sum(self.botState.charts["USDT_BTC"].volumes[0 : len(self.botState.charts["USDT_BTC"].volumes) - 1])
            # arrMoy = arrSum / arrLen
            # currentVolume = self.botState.charts["USDT_BTC"].volumes[-1]
            # pourcent = int((currentVolume / arrMoy) * 100)
            # print(f"ratio du volume a {pourcent}%, pour le volume {currentVolume}\n", file=sys.stderr)
            # period =  self.botState.candlesGiven;
            # print(f"period is {period}\n", file=sys.stderr)
            # if buy == -1:  
            #     print(f'sell USDT_BTC {0.5 * affordable}')
            #     # self.botState.slist = 0
            #     # self.botState.rlist = 0
            # if dollars < 100 or buy == 0:
            #     print("no_moves", flush=True)
            # if dollars >= 100 and buy == 1:
            #     print(f'buy USDT_BTC {0.5 * affordable}', flush=True)
            # if ((buy == 1) and av > 2 and dollars >= 100):
            #     print(f'buy? {buy} and av {av} and dollars {dollars} and pourcent {pourcent}\n', file=sys.stderr)
            #     # print(f'buy USDT_BTC {0.5 * affordable}', flush=True)

            # if (self.botState.slist[-1] > 5 and buy == -1):
            #     print(f'sell? {buy} and av {av} and dollars {dollars} and pourcent {pourcent}\n', file=sys.stderr)
                # print(f'sell USDT_BTC {0.5 * affordable}', flush=True)


class Candle:
    def __init__(self, format, intel):
        tmp = intel.split(",")
        for (i, key) in enumerate(format):
            value = tmp[i]
            if key == "pair":
                self.pair = value
            if key == "date":
                self.date = int(value)
            if key == "high":
                self.high = float(value)
            if key == "low":
                self.low = float(value)
            if key == "open":
                self.open = float(value)
            if key == "close":
                self.close = float(value)
            if key == "volume":
                self.volume = float(value)

    def __repr__(self):
        return str(self.pair) + str(self.date) + str(self.close) + str(self.volume)


class Chart:
    def __init__(self):
        self.dates = []
        self.opens = []
        self.highs = []
        self.lows = []
        self.closes = []
        self.volumes = []
        self.indicators = {}

    def add_candle(self, candle: Candle):
        self.dates.append(candle.date)
        self.opens.append(candle.open)
        self.highs.append(candle.high)
        self.lows.append(candle.low)
        self.closes.append(candle.close)
        self.volumes.append(candle.volume)


class BotState:
    def __init__(self):
        self.closing_list = []
        self.timeBank = 0
        self.maxTimeBank = 0
        self.timePerMove = 1
        self.candleInterval = 1
        self.candleFormat = []
        self.candlesTotal = 0
        self.candlesGiven = 0
        self.initialStack = 0
        self.transactionFee = 0.1
        self.date = 0
        self.stacks = dict()
        self.charts = dict()
        # ajout groundhoung
        self.numberlist =[];
        self.switchedCount = 0;
        # self.weirdList = [];
        self.av = 0
        self.rlist = [];
        self.slist = [];
        self.i = 0;

    def isSwitched(rlist, periode, index):
        if index <= periode:
            # return (reprint("", 0));
            return (0);
        else:
            if rlist[index] > 0 and rlist[index - 1] > 0:
                return (reprint ("", 0));
            elif rlist[index] <= 0 and rlist[index - 1] <= 0:
                # return (reprint("", 0));
                return (0);
            else:
                # return (reprint("\t\ta switch occurs", 1));
                return (1);

        #fin grou ndhoung
    def update_chart(self, pair: str, new_candle_str: str):
        if not (pair in self.charts):
            self.charts[pair] = Chart()
        new_candle_obj = Candle(self.candleFormat, new_candle_str)
        self.charts[pair].add_candle(new_candle_obj)

    def update_stack(self, key: str, value: float):
        self.stacks[key] = value

    def update_settings(self, key: str, value: str):
        if key == "timebank":
            self.maxTimeBank = int(value)
            self.timeBank = int(value)
        if key == "time_per_move":
            self.timePerMove = int(value)
        if key == "candle_interval":
            self.candleInterval = int(value)
        if key == "candle_format":
            self.candleFormat = value.split(",")
        if key == "candles_total":
            self.candlesTotal = int(value)
        if key == "candles_given":
            self.candlesGiven = int(value)
        if key == "initial_stack":
            self.initialStack = int(value)
        if key == "transaction_fee_percent":
            self.transactionFee = float(value)

    def update_game(self, key: str, value: str):
        if key == "next_candles":
            new_candles = value.split(";")
            self.date = int(new_candles[0].split(",")[1])
            for candle_str in new_candles:
                candle_infos = candle_str.strip().split(",")
                self.update_chart(candle_infos[0], candle_str)
        if key == "stacks":
            new_stacks = value.split(",")
            for stack_str in new_stacks:
                stack_infos = stack_str.strip().split(":")
                self.update_stack(stack_infos[0], float(stack_infos[1]))


if __name__ == "__main__":
    # sys.stderr = open("dimwit.txt", "w")
    mybot = Bot()
    mybot.run()
    # sys.stderr.close()
