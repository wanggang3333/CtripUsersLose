#! /usr/bin/env python
# coding=utf-8
"""
Author: wanggang
Github: https://github.com/wanggang3333

"""

import pandas as pd
from datetime import datetime


def txt_to_csv():
    """
    将train 和 test 文件格式从 txt 转换成 csv 格式，方便后面的处理
    :return: None
    """
    train = pd.read_csv('../data/train.txt', sep='\t')
    train.to_csv('../data/train.csv', index=False)
    test = pd.read_csv('../data/test.txt', sep='\t')
    test.to_csv('../data/test.csv', index=False)


def cut():
    """
    把train集分割，一部分用来测试，一部分用来训练
    :return: None
    """
    train = '../data/train.csv'
    trainfile = pd.read_csv(train)
    n = len(trainfile) / 7
    print 'train_test'
    trainfile[:n].to_csv('../data/train_test.csv', index=False)
    print 'train_test_result'
    trainfile.ix[:n, ['sampleid', 'label']].to_csv('../data/train_test_result.csv', index=False)
    print 'train_train'
    trainfile[n + 1:].to_csv('../data/train_train.csv', index=False)

def count_null(data):
    data['nullcount'] = pd.isnull(data).apply(sum, axis=1)
    data.to_csv('../data/train_train_nullcount.csv', index=False)
    #return data

def process_date(data):
    newSeries = data['arrival'].map(lambda x: datetime.strptime(x,'%Y-%m-%d')) - data['d'].map(lambda x: datetime.strptime(x,'%Y-%m-%d'))
    return newSeries.map(lambda x: pd.tslib.Timedelta(x).days)

def process_mean(train, test=None):
    features = ['hotelcr', 'landhalfhours', 'novoters', 'cancelrate', 'hoteluv','cr_pre',
                'lowestprice', 'customereval_pre2', 'commentnums_pre2','cancelrate_pre',
                'novoters_pre2', 'novoters_pre', 'lowestprice_pre', 'uv_pre', 'uv_pre2',
                'lowestprice_pre2', 'cityuvs', 'cityorders'] # missing rate <= 10%
    for fea in features:
        # if fea in train.columns:
        #     print fea, ': True'
        # else:
        #     print '-----', fea, ': False'
        means = train[fea].mean()
        train[fea].fillna(means, inplace=True)
        test[fea].fillna(means, inplace=True)

def process_most(train, test=None):
    features = ['decisionhabit_user','historyvisit_7ordernum', 'historyvisit_totalordernum', 'ordercanceledprecent',
                'ordercanncelednum', 'commentnums', 'starprefer', 'consuming_capacity', 'historyvisit_avghotelnum',
                'historyvisit_visit_detailpagenum', 'delta_price1', 'price_sensitive', 'businessrate_pre',
                'ordernum_oneyear', 'avgprice', 'firstorder_bu', 'delta_price2', 'commentnums_pre', 'customer_value_profit',
                'ctrip_profits', 'deltaprice_pre2_t1', 'lasthtlordergap', 'businessrate_pre2', 'lastpvgap',
                'cr', 'visitnum_oneyear']
    for fea in features:
        # if fea in train.columns:
        #     print fea, ': True'
        # else:
        #     print '-----', fea, ': False'
        mosts = train[fea].value_counts().index[0]
        train.fillna(mosts, inplace=True)
        test.fillna(mosts, inplace=True)

if __name__ == '__main__':
    print 'start processing'
    # txt_to_csv()
    # cut()
    # train = pd.read_csv('../data/train_train.csv')
    # count_null(train)
    tests = pd.read_csv('../data/train_test.csv')
    # process_date(test)
    process_mean(tests)
    process_most(tests)