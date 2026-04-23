# -*- coding: utf-8 -*-
"""
Chemprop 1.6.1 Full pipeline execution script
Generates dataset -> Trains model -> Predicts molecular properties
"""
import subprocess
import sys
import os


def run_script(script_name):
    """Execute specified Python script, capture output and handle exceptions"""
    script_path = os.path.join(os.path.dirname(__file__), script_name)
    if not os.path.exists(script_path):
        print(f"[ERROR] Script not found: {script_name}")
        return False

    try:
        result = subprocess.run(
            [sys.executable, script_path],
            check=True,
            capture_output=True,
            encoding="utf-8",
            errors="replace"
        )
        if result.stdout:
            print(f"[INFO] {script_name} output:\n{result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] {script_name} execution failed! Error:\n{e.stderr}")
        return False


if __name__ == '__main__':
    print("===== Starting Chemprop 1.6.1 Full Pipeline =====")

    print("\n[Step 1/3] Generating catalytic dataset...")
    if not run_script("generate_csv.py"):
        sys.exit(1)

    print("\n[Step 2/3] Training multi-task regression model...")
    if not run_script("train.py"):
        sys.exit(1)

    print("\n[Step 3/3] Predicting molecular catalytic properties...")
    if not run_script("predict.py"):
        sys.exit(1)

    print("\n===== Full Pipeline Complete! =====")