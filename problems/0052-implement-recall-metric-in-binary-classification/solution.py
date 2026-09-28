import numpy as np

def recall(y_true, y_pred):
    """
    Calculate the recall metric for binary classification.
    
    Args:
        y_true: Array of true binary labels (0 or 1)
        y_pred: Array of predicted binary labels (0 or 1)
    
    Returns:
        Recall value as a float
    """
    # Your code here
    assert len(y_pred) == len(y_true), "wrong"
    tp = fn = 0
    for i in range(len(y_pred)):
        if y_true[i] and y_pred[i]:
            tp += 1
        if not y_pred[i] and y_true[i]:
            fn += 1
    if tp == 0 and fn == 0:
        return  0
    return tp/(tp + fn)

