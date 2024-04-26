import pandas as pd

def evaluate_classification(y_true, y_pred):
    TP = 0
    TN = 0
    FP = 0
    FN = 0

    if y_true == 'Positive' and y_pred == 'Positive':
        TP = 1
    elif y_true == 'Negative' and y_pred == 'Negative':
        TN = 1
    elif y_true == 'Negative' and y_pred == 'Positive':
        FP = 1
    elif y_true == 'Positive' and y_pred == 'Negative':
        FN = 1

    return TP, TN, FP, FN

# Read the Excel sheet into a pandas dataframe
df = pd.read_excel('test_results.xlsx', sheet_name='Sheet1')

# Get the columns from the dataframe
test_image_name_col = 'Test Image Name'
predicted_class_col = 'Predicted Class'
true_class_col = 'True Class'

# Get the input data from the dataframe
input_data = df[[test_image_name_col, predicted_class_col, true_class_col]].values.tolist()

# Calculate TP, TN, FP, and FN for each row of the input data
TP_list = []
TN_list = []
FP_list = []
FN_list = []

for row in input_data:
    y_true = row[2]
    y_pred = row[1]
    TP, TN, FP, FN = evaluate_classification(y_true, y_pred)
    TP_list.append(TP)
    TN_list.append(TN)
    FP_list.append(FP)
    FN_list.append(FN)

# Add the evaluation metrics to the dataframe
df['TP'] = TP_list
df['TN'] = TN_list
df['FP'] = FP_list
df['FN'] = FN_list

# Calculate total TP, TN, FP, and FN for all rows
total_TP = sum(TP_list)
total_TN = sum(TN_list)
total_FP = sum(FP_list)
total_FN = sum(FN_list)

# Print the evaluation metrics
print('TP:', total_TP)
print('TN:', total_TN)
print('FP:', total_FP)
print('FN:', total_FN)
