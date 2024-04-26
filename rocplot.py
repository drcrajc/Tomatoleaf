import pandas as pd
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

# Read the data from Excel file
df = pd.read_excel('path/to/your/excel/file.xlsx')

# Assuming your Excel file has 'Predicted Class' and 'Actual Class' columns
predicted_class = df['Predicted Class']
actual_class = df['Actual Class']

# Calculate the false positive rate (fpr), true positive rate (tpr), and threshold values
fpr, tpr, thresholds = roc_curve(actual_class, predicted_class)

# Calculate the area under the ROC curve (AUC)
auc = roc_auc_score(actual_class, predicted_class)

# Plot the ROC curve
plt.plot(fpr, tpr, label=f'AUC = {auc:.2f}')
plt.plot([0, 1], [0, 1], 'k--')  # Diagonal line representing random chance
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.show()
