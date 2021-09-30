import numpy as np
import scipy.stats as st
from scipy.stats import pearsonr, hmean, gmean


# SICK and PARA first graph is ignored (empty graph)
STS = ("../sts/orig.test.txt", [0, 1379])
SICK = ("../sick/orig.test.txt", [1, 4928])
PARA = ("../para/orig.test.txt", [1, 1726])

def get_arg_parser():
    import argparse

    parser = argparse.ArgumentParser(description='evaluate AMR metric result')
    
    parser.add_argument('-path_sts_prediction_file_main', type=str, nargs='?',
                                help='path to sts prediction file', required = True)
    parser.add_argument('-path_sick_prediction_file_main', type=str, nargs='?',
                                help='path to sick prediction file', required=True)
    parser.add_argument('-path_para_prediction_file_main', type=str, nargs='?',
                                help='path to para prediction file', required=True)
    
    parser.add_argument('-path_sts_prediction_file_syno', type=str, nargs='?',
                                help='path to sts prediction file', required = True)
    parser.add_argument('-path_sick_prediction_file_syno', type=str, nargs='?',
                                help='path to sick prediction file', required=True)
    parser.add_argument('-path_para_prediction_file_syno', type=str, nargs='?',
                                help='path to para prediction file', required=True)
    
    parser.add_argument('-path_sts_prediction_file_reify', type=str, nargs='?',
                                help='path to sts prediction file', required = True)
    parser.add_argument('-path_sick_prediction_file_reify', type=str, nargs='?',
                                help='path to sick prediction file', required=True)
    parser.add_argument('-path_para_prediction_file_reify', type=str, nargs='?',
                                help='path to para prediction file', required=True)
    
    parser.add_argument('-path_sts_prediction_file_roleconf', type=str, nargs='?',
                                help='path to sts prediction file', required = True)
    parser.add_argument('-path_sick_prediction_file_roleconf', type=str, nargs='?',
                                help='path to sick prediction file', required=True)
    parser.add_argument('-path_para_prediction_file_roleconf', type=str, nargs='?',
                                help='path to para prediction file', required=True)
    
    return parser


def get_predicted_scores(lines, f = lambda x: x.split()[-1], index=STS[0]):
    out = []
    for i,l in enumerate(lines):
        try:
            x = f(l)
            x = float(x)
            out.append(x)
        except:
            out.append("NA")
    return np.array(out[index[0]:index[1]])  


def readl(p):
    with open(p) as f:
        return f.read().split("\n")


def load_human_scores_sts():
    sts = readl(STS[0])[STS[1][0]:STS[1][1]]
    out = []
    for i,l in enumerate(sts):
        x = l.split("\t")[4]
        x = float(x)
        out.append(x)
    mi, ma = np.min(out), np.max(out)
    out = (out - mi) / (ma - mi)
    return out


def load_human_scores_sick():
    sts = readl(SICK[0])[SICK[1][0]:SICK[1][1]]
    out = []
    for i,l in enumerate(sts):
        x = l.split("\t")[3]
        x = float(x)
        out.append(x)
    out = np.array(out)
    mi, ma = np.min(out), np.max(out)
    out = (out - mi) / (ma - mi)
    return out


def load_human_scores_para():
    sts = readl(PARA[0])[PARA[1][0]:PARA[1][1]]
    out = []
    for i,l in enumerate(sts):
        x = l.split("\t")[0]
        x = float(x)
        out.append(x)
    mi, ma = np.min(out), np.max(out)
    out = (out - mi) / (ma - mi)
    return out


def evaluate_with_function(xs, ys, fun):
    return fun(xs, ys)


def safe_evaluate_with_function(xs, ys, fun):
    try:
        mp = evaluate_with_function(xs, ys, fun=fun)
    except (ValueError, TypeError) as e:
        mp = "NA"
    return mp


def eval_rep(scores):
    am = np.mean(scores)
    gm = gmean(scores)
    hm = hmean(scores)
    scores.append(am)
    scores.append(gm)
    scores.append(hm)
    ls = [str(round(sc*100, 2)) for sc in scores]
    ls = [x + "0" if len(x.split(".")[1]) == 1 else x for x in ls]
    return " & ".join(ls)


if __name__ == "__main__":
    human_sts = load_human_scores_sts()
    human_sick = load_human_scores_sick()
    human_para = load_human_scores_para()
    parser = get_arg_parser()
    args = parser.parse_args()
    scores = []
    
    path = args.path_sts_prediction_file_main
    pred = get_predicted_scores(readl(path), index=STS[1])
    evalfun = lambda x, y: pearsonr(x,y)[0]
    

    mp = safe_evaluate_with_function(human_sts, pred, fun=evalfun)
    scores.append(mp)
    print(path, mp)

    
    path = args.path_sick_prediction_file_main
    pred = get_predicted_scores(readl(path), index=SICK[1])
    mp = safe_evaluate_with_function(human_sick, pred, fun=evalfun)
    scores.append(mp)
    print(path, mp)

    
    path = args.path_para_prediction_file_main
    pred = get_predicted_scores(readl(path), index=PARA[1])
    mp = safe_evaluate_with_function(human_para, pred, fun=evalfun)
    scores.append(mp)
    print(path, mp)

    
    path = args.path_sts_prediction_file_reify
    pred = get_predicted_scores(readl(path), index=STS[1])
    mp = safe_evaluate_with_function(human_sts, pred, fun=evalfun)
    scores.append(mp)
    print(path, mp)
    
    
    path = args.path_sick_prediction_file_reify
    pred = get_predicted_scores(readl(path), index=SICK[1])
    mp = safe_evaluate_with_function(human_sick, pred, fun=evalfun)
    scores.append(mp)
    print(path, mp)


    path = args.path_para_prediction_file_reify
    pred = get_predicted_scores(readl(path), index=PARA[1])
    mp = safe_evaluate_with_function(human_para, pred, fun=evalfun)
    scores.append(mp)
    print(path, mp)

    
    path = args.path_sts_prediction_file_syno
    pred = get_predicted_scores(readl(path), index=STS[1])
    mp = safe_evaluate_with_function(human_sts, pred, fun=evalfun)
    scores.append(mp)
    print(path, mp)

    
    path = args.path_sick_prediction_file_syno
    pred = get_predicted_scores(readl(path), index=SICK[1])
    mp = safe_evaluate_with_function(human_sick, pred, fun=evalfun)
    scores.append(mp)
    print(path, mp)

    
    path = args.path_para_prediction_file_syno
    pred = get_predicted_scores(readl(path), index=PARA[1])
    mp = safe_evaluate_with_function(human_para, pred, fun=evalfun)
    scores.append(mp)
    print(path, mp)


    path = args.path_sts_prediction_file_roleconf
    pred = get_predicted_scores(readl(path), index=[0, 158])
    mp = safe_evaluate_with_function([0,1]*int(len(pred)/2), pred, fun=evalfun)
    scores.append(mp)
    print(path, mp)

    
    path = args.path_sick_prediction_file_roleconf
    pred = get_predicted_scores(readl(path), index=[0,  238])
    mp = safe_evaluate_with_function([0,1]*int(len(pred)/2), pred, fun=evalfun)
    scores.append(mp)
    print(path, mp)


    path = args.path_para_prediction_file_roleconf
    pred = get_predicted_scores(readl(path), index=[0, 2242]) 
    mp = safe_evaluate_with_function([0,1]*int(len(pred)/2), pred, fun=evalfun)
    scores.append(mp)
    print(path, mp)

    print("Latex --->",  "\multicolumn{12}{c}{Pearson's $\\rho$} & amean & gmean & hmean" )
    print("Latex --->",  eval_rep(scores))



