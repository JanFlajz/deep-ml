import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    scores = [i - max(scores) for i in scores]
    _sum = sum(math.exp(i) for i in scores)

    return [math.exp(i)/_sum for  i in scores]