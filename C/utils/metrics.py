import numpy as np
import pandas as pd


def f1_macro(df_true: pd.DataFrame, df_pred: pd.DataFrame) -> float:
    """
    code from the organizers of the competition
    """

    precisions = list()
    recalls = list()

    for column in df_true.columns:
        sol = df_pred[column].tolist()  # сюда нужно передать таблицу с ответом алгоритма
        ans = df_true[column].tolist()

        count = len(sol)

        tp = 0  # правильно заполненная
        fp = 0  # пустая, но чем-то заполненная
        fn = 0  # ложно пустая
        tn = 0  # правильно пустая

        for i in range(count):
            if sol[i] == ans[i]:
                if sol[i] == '':
                    tn += 1
                else:
                    tp += 1
            elif sol[i] == '':
                fp += 1
            else:
                fn += 1

        if tp == 0:
            prec = 0
            rec = 0
        else:
            prec = tp / (tp + fp)
            rec = tp / (tp + fn)

        precisions.append(prec)
        recalls.append(rec)

    prec = np.mean(precisions)
    rec = np.mean(recalls)
    score = 2 * prec * rec / (prec + rec)

    return score
