"""
Project 3: Exploratory Data Analysis (EDA) Project
------------------------------------------------------
Goal   : Analyze a dataset to uncover patterns and trends.
Tools  : Pandas, Matplotlib, Seaborn
Output : Statistical summary, correlation analysis, and a structured
         EDA report printed to the console + visualization dashboard.

NOTE: A synthetic "Student Exam Performance" dataset is generated below so
the script runs anywhere without an external file. To use your own data,
replace `generate_dataset()` with `pd.read_csv("your_file.csv")`.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(7)
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate_dataset(n=400):
    study_hours = np.random.normal(5, 2, n).clip(0, 12)
    attendance = np.random.normal(80, 10, n).clip(40, 100)
    sleep_hours = np.random.normal(6.5, 1.2, n).clip(3, 10)
    prev_score = np.random.normal(65, 12, n).clip(20, 100)

    exam_score = (
        10 + 6 * study_hours + 0.3 * attendance + 1.5 * sleep_hours
        + 0.25 * prev_score + np.random.normal(0, 5, n)
    ).clip(0, 100)

    gender = np.random.choice(["Male", "Female"], n)

    df = pd.DataFrame({
        "StudyHours": study_hours.round(1),
        "Attendance": attendance.round(1),
        "SleepHours": sleep_hours.round(1),
        "PreviousScore": prev_score.round(1),
        "Gender": gender,
        "ExamScore": exam_score.round(1),
    })
    return df


def statistical_summary(df):
    print("\n--- Statistical Summary ---")
    print(df.describe())
    print("\n--- Data Types ---")
    print(df.dtypes)


def correlation_analysis(df):
    numeric_df = df.select_dtypes(include=[np.number])
    corr = numeric_df.corr()
    print("\n--- Correlation with ExamScore ---")
    print(corr["ExamScore"].sort_values(ascending=False))
    return corr


def build_dashboard(df, corr):
    fig, axes = plt.subplots(2, 2, figsize=(13, 10))
    fig.suptitle("Exploratory Data Analysis Dashboard", fontsize=16, fontweight="bold")

    sns.histplot(df["ExamScore"], kde=True, color="teal", ax=axes[0, 0])
    axes[0, 0].set_title("Distribution of Exam Scores")

    sns.scatterplot(data=df, x="StudyHours", y="ExamScore", hue="Gender", ax=axes[0, 1])
    axes[0, 1].set_title("Study Hours vs Exam Score")

    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=axes[1, 0])
    axes[1, 0].set_title("Correlation Heatmap")

    sns.boxplot(data=df, x="Gender", y="ExamScore", ax=axes[1, 1])
    axes[1, 1].set_title("Exam Score by Gender")

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    path = os.path.join(OUTPUT_DIR, "eda_dashboard.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"\nDashboard saved to: {path}")


def generate_report(df, corr):
    top_factor = corr["ExamScore"].drop("ExamScore").abs().idxmax()
    top_value = corr["ExamScore"][top_factor]
    avg_score_by_gender = df.groupby("Gender")["ExamScore"].mean()

    report = f"""
========== EDA STRUCTURED REPORT ==========
1. Dataset Overview
   - Records: {len(df)}
   - Features: {list(df.columns)}

2. Key Statistics
   - Average Exam Score: {df['ExamScore'].mean():.2f}
   - Median Exam Score: {df['ExamScore'].median():.2f}
   - Std Deviation: {df['ExamScore'].std():.2f}

3. Correlation Insight
   - Strongest influencing factor on ExamScore: '{top_factor}' (r = {top_value:.2f})

4. Group Comparison
   - Average score by gender:
     {avg_score_by_gender.to_dict()}

5. Conclusion
   - Study hours and previous academic performance show the strongest
     positive relationship with final exam outcomes, suggesting that
     consistent study habits matter more than any single demographic factor.
=============================================
"""
    print(report)
    report_path = os.path.join(OUTPUT_DIR, "eda_report.txt")
    with open(report_path, "w") as f:
        f.write(report)
    print(f"Report saved to: {report_path}")


def main():
    df = generate_dataset()
    statistical_summary(df)
    corr = correlation_analysis(df)
    build_dashboard(df, corr)
    generate_report(df, corr)


if __name__ == "__main__":
    main()
