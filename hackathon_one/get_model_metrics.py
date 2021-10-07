# import libraries

from sklearn.metrics import (
    accuracy_score,
    roc_auc_score,
    precision_score,
    recall_score,
    f1_score,
)


def calc_metrics(model, X, y):
    """Get model evaluation metrics on the test set."""

    # Get model predictions
    y_predict_r = model.predict(X)

    # Calculate evaluation metrics for assesing performance of the model.
    roc = roc_auc_score(y, y_predict_r)
    acc = accuracy_score(y, y_predict_r)
    prec = precision_score(y, y_predict_r)
    rec = recall_score(y, y_predict_r)
    f1 = f1_score(y, y_predict_r)

    return {"acc": acc, "roc": roc, "prec": prec, "rec": rec, "f1": f1}
