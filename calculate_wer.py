import jiwer

def calculate_wer(file1, file2):
    # Read content of both files
    with open(file1, 'r', encoding='utf-8') as f1:
        reference = f1.read().replace('\n', ' ')

    with open(file2, 'r', encoding='utf-8') as f2:
        hypothesis = f2.read().replace('\n', ' ')

    # Calculate WER using jiwer (no transformations)
    wer = jiwer.wer(reference, hypothesis)
    
    return wer

# Example usage
file1 = "test_actual_telugu.txt"
file2 = "test_tel_pred.txt"

wer_value = calculate_wer(file1, file2)
print(f"Word Error Rate")
print(wer_value)