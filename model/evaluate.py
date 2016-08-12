#! /usr/bin/env python
#coding=utf-8
"""
Author: wanggang
Github: https://github.com/wanggang3333

"""
from utility.utility import cutoffLine
from utility.utility import floatrange


def simple_evaluate(prediction, result):

    cutoffLine('-')
    print 'Prediction set size: %d' % len(prediction)
    print 'Result set size: %d' % len(result)
    if len(prediction) != len(result):
        print 'please make prediction length equal to result length '
        return

    best_val = 0
    best_P = 0
    best_R = 0
    for val in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
        label0_act_label0_pre = 0
        label1_act_label0_pre = 0
        label0_act_label1_pre = 0
        # label1_act_label1_pre = 0
        for i,j in zip(prediction, result):
            if i == 0 and j == 0:
                label0_act_label0_pre += 1
            elif i == 1 and j == 0:
                label0_act_label1_pre += 1
            elif i == 0 and j == 1:
                label1_act_label0_pre += 1

        precision = label0_act_label0_pre/(label0_act_label0_pre + label1_act_label0_pre)
        recall = label0_act_label0_pre/(label0_act_label0_pre + label0_act_label1_pre)
        print '     val: %2f' % val,
        print '     P : %2f' % precision,
        print '     R : %2f' % recall
        if precision >= 0.90 and recall > best_R:
            best_val = val
            best_P = precision
            best_R = recall

    print 'best prediction: ',
    print 'best P : %2f' % best_P,
    print 'best R : %2f' % best_R,
    print 'best F1: %2f' % best_P * best_R * 2 / (best_P + best_R)

    cutoffLine('-')
    return best_P, best_R, best_val

def complete_evaluate(prediction, result):

    cutoffLine('-')
    print 'Prediction set size: %d' % len(prediction)
    print 'Result set size: %d' % len(result)
    if len(prediction) != len(result):
        print 'please make prediction length equal to result length '
        return

    best_val = 0
    best_P = 0
    best_R = 0
    for val in floatrange(0.0, 1.0, 0.01):
        label0_act_label0_pre = 0
        label1_act_label0_pre = 0
        label0_act_label1_pre = 0
        # label1_act_label1_pre = 0
        for i,j in zip(prediction, result):
            if i == 0 and j == 0:
                label0_act_label0_pre += 1
            elif i == 1 and j == 0:
                label0_act_label1_pre += 1
            elif i == 0 and j == 1:
                label1_act_label0_pre += 1

        precision = label0_act_label0_pre/(label0_act_label0_pre + label1_act_label0_pre)
        recall = label0_act_label0_pre/(label0_act_label0_pre + label0_act_label1_pre)
        print '     val: %2f' % val,
        print '     P : %2f' % precision,
        print '     R : %2f' % recall
        if precision >= 0.90 and recall > best_R:
            best_val = val
            best_P = precision
            best_R = recall

    print 'best prediction: ',
    print 'best P : %2f' % best_P,
    print 'best R : %2f' % best_R,
    print 'best F1: %2f' % best_P * best_R * 2 / (best_P + best_R)

    cutoffLine('-')
    return best_P, best_R, best_val