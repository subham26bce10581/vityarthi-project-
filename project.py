CLASSIFICATION_LEVELS = {
    3: "CONFIRMED Chance Jaundice (HIGH RISK)",
    2: "MODERATE CHANCE Jaundice(MIDDLE RISK)",
    1: "LEAST CHANCE Jaundice(LOW RISK)",
    0: "LEAST CHANCE Jaundice(LOW RISK)"
}


def gather_test_results():
    """Gathers patient records and positive results from 3 tests."""

    print("\n--- BEGIN 3-TEST INPUT ---")

    positive_count = 0
    patient_id = input("Enter Patient ID: ")

    # Jaundice test
    if input("Test 1: Bilirubin  Blood test(yes/no)? ").strip().lower() == 'yes':
        positive_count += 1

    if input("Test 2: Liver Function test (yes/no)? ").strip().lower() == 'yes':
        positive_count += 1

    if input("Test 3: Bilirubin Urine test (yes/no)? ").strip().lower() == 'yes':
        positive_count += 1

    return {
        'ID': patient_id,
        'COUNT': positive_count
    }

#  2. Process test

def classify_outcome(input_data):
    """Classifies risk (Prediction/Classification)."""

    count = input_data['COUNT']

    # classifcation level
    if count == 3:
        risk_level = CLASSIFICATION_LEVELS[3]
    elif count == 2:
        risk_level = CLASSIFICATION_LEVELS[2]
    else:
        # for 0 and 1 test
        risk_level = CLASSIFICATION_LEVELS[count]

    # Returns the necessary data with the correct key 'FINAL_COUNT'
    return {
        'LEVEL': risk_level,
        'FINAL_COUNT': count
    }

# report test

def print_final_summary(summary_data, patient_data):
    """Prints the final  report."""

    print("\n--------------------------------------")
    print(f"REPORT FOR: {patient_data['ID']}")
    print("--------------------------------------")

    # This line Final error is used to prevent any errors
    print(f"Positive Tests: {summary_data['FINAL_COUNT']} / 3")
    print(f"RISK CLASSIFICATION: {summary_data['LEVEL']}")
    print("--------------------------------------\n")




if __name__ == "__main__":

    # 1. Information
    data = gather_test_results()

    # 2. Process
    results = classify_outcome(data)

    # 3. Report
    print_final_summary(results, data)