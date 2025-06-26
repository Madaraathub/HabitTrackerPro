import pandas as pd
from jinja2 import Template
import os
import sys

def generate_report():
    try:
        print("\n" + "="*50)
        print("Habit Tracker Pro - Report Generator")
        print("="*50 + "\n")
        
        # Load data
        habits = pd.read_csv('habits.csv')
        tracker = pd.read_csv('daily_tracker.csv')
        
        # Load template
        with open('habit_tracker_template.txt', 'r', encoding='utf-8') as file:
            template = Template(file.read())
        
        # Generate report
        report = template.render(
            month=habits['month'][0],
            goal=habits['goal'][0],
            habits=habits.iloc[0].to_dict(),
            tracker=tracker.to_dict('records')
        )
        
        # Save report
        os.makedirs('reports', exist_ok=True)
        report_path = 'reports/habit_report.md'
        with open(report_path, 'w', encoding='utf-8') as file:
            file.write(report)
            
        print(f"✅ Report generated successfully at {report_path}")
        print(f"⭐ Total habits processed: {len(habits)}")
        print(f"📅 Days tracked: {len(tracker)}")
        return True
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\nPlease check:")
        print("- All files exist in the project directory")
        print("- CSV files have correct headers")
        return False

if __name__ == "__main__":
    if not generate_report():
        sys.exit(1)
