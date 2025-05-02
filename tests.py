from mpin_functions import isCommon2, isWeakByDemographics3

def run_testcases():
    test_cases = [
        ("1234", "01012000", "02021999", "03032020", "WEAK", ["COMMONLY_USED"]),
        ("2000", "01012000", "02021999", "03032020", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
        ("1999", "01012000", "02021999", "03032020", "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),
        ("2020", "01012000", "02021999", "03032020", "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
        ("0101", "01012000", "02021999", "03032020", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
        ("1230", "01012000", "02021999", "03032020", "WEAK", ["COMMONLY_USED"]),
        ("1212", "12121212", "12121212", "12121212", "WEAK", ["COMMONLY_USED", "DEMOGRAPHIC_DOB_SELF", "DEMOGRAPHIC_DOB_SPOUSE", "DEMOGRAPHIC_ANNIVERSARY"]),
        ("654321", "01012000", "02021999", "03032020", "WEAK", ["COMMONLY_USED"]),
        ("0303", "01012000", "02021999", "03032020", "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
        ("999999", "01012000", "02021999", "03032020", "WEAK", ["COMMONLY_USED"]),
        ("4791", "01012000", "02021999", "03032020", "STRONG", []),
        ("7654", "01012000", "02021999", "03032020", "STRONG", []),
        ("8888", "01012000", "02021999", "03032020", "STRONG", []),
        ("2001", "01012001", "02021999", "03032020", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
        ("010199", "01011999", "02021999", "03032020", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
        ("030320", "01012000", "02021999", "03032020", "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
        ("6543", "01012000", "02021999", "03032020", "STRONG", []),
        ("4321", "01012000", "02021999", "03032020", "WEAK", ["COMMONLY_USED"]),
        ("111111", "01012000", "02021999", "03032020", "WEAK", ["COMMONLY_USED"]),
        ("310119", "31011999", "02021999", "03032020", "WEAK", ["DEMOGRAPHIC_DOB_SELF"])
    ]

    for i in range(len(test_cases)):
        mpin, dob, spouse_dob, anniversary, expected_strength, expected_reasons = test_cases[i]
        reasons = []

        if isCommon2(mpin):
            reasons.append("COMMONLY_USED")
        reasons.extend(isWeakByDemographics3(mpin, dob, spouse_dob, anniversary))

        if reasons:
            result_strength = "WEAK" 
        else:
            result_strength = "STRONG"

        if result_strength == expected_strength and set(reasons) == set(expected_reasons):
            print("Test", i + 1, ": PASSED")
        else:
            print("Test", i + 1, ": FAILED")
            print("  MPIN:", mpin)
            print("  Expected:", expected_strength, expected_reasons)
            print("  Got:", result_strength, reasons)

# Run the test cases
run_testcases()