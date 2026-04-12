import seaborn as sns
import matplotlib.pyplot as plt

def run_eda_dashboards(df):
    # Dashboard 1: Cancellation Overview
    plt.figure(figsize=(8, 5))
    sns.countplot(x='is_canceled', data=df)
    plt.title("Cancellation Distribution")
    plt.show() # This opens a window in VS Code to show the plot

    # Dashboard 2: Lead Time vs Cancellation
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='is_canceled', y='lead_time', data=df)
    plt.title("Lead Time vs Cancellation")
    plt.show()

    # Dashboard 3: Deposit Type Impact
    plt.figure(figsize=(8, 5))
    sns.barplot(x='deposit_type', y='is_canceled', data=df)
    plt.title("Cancellation Rate by Deposit Type")
    plt.show()
    