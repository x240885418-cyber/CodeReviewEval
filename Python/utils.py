def reverse_string(text):
    """Reverses the characters in a string."""
    return text[::-1]

def count_words(sentence):
    return len(sentence.split())

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def calculate_metrics(true_positives: int, false_positives: int, false_negatives: int) -> dict[str, float]:
    """Calculate precision, recall, and F1 from review-finding counts."""
    if min(true_positives, false_positives, false_negatives) < 0:
        raise ValueError("Counts must be non-negative")

    precision_denominator = true_positives + false_positives
    recall_denominator = true_positives + false_negatives
    precision = true_positives / precision_denominator if precision_denominator else 0.0
    recall = true_positives / recall_denominator if recall_denominator else 0.0
    f1_denominator = precision + recall
    f1 = 2 * precision * recall / f1_denominator if f1_denominator else 0.0

    return {"precision": precision, "recall": recall, "f1": f1}     

def data_div(x, y):
    if x == 0:
        return 0
    return x/y