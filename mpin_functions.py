# PART A 
commonPins = {
    '1234', '0000', '1111', '1212', '1313', '7777',
    '4444', '2222', '6969', '9999', '3333', '5555',
    '1122', '4321', '1010', '6666',
    '1230', '2345', '3456', '4567', '5678', '6789'
}

def isCommon(mpin):# To check if the mpin entered is part of the common mpin list specified
    return mpin in commonPins

# PART B
def extract_segments(date_str):
    if len(date_str) != 8:
        return set()
#Formatting through Slicing
    
    dd = date_str[:2] #date
    mm = date_str[2:4] #month
    yyyy = date_str[4:] #year
    yy = yyyy[2:] #last two digits of year
    
    #Possible combinations of 4-digit
    return {
        dd + mm, mm + dd,
        dd + yy, yy + dd,
        mm + yy, yy + mm,
        yyyy
    }

def isWeakByDemographics(mpin, dob, spouse_dob, anniversary):#checks if mpin entered is a combination formed by demoghraphics
    segments = extract_segments(dob).union(
    extract_segments(spouse_dob),
    extract_segments(anniversary)
)
    return mpin in segments

# PART C
def isWeakByDemographics2(mpin, dob, spouse_dob, anniversary):#returns reasons for Weak mpins
    reasons = []
    if mpin in extract_segments(dob):
        reasons.append("DEMOGRAPHIC_DOB_SELF")
    if mpin in extract_segments(spouse_dob):
        reasons.append("DEMOGRAPHIC_DOB_SPOUSE")
    if mpin in extract_segments(anniversary):
        reasons.append("DEMOGRAPHIC_ANNIVERSARY")
    return reasons

# PART D
commonMpinList_6 = {
    '123456', '000000', '111111', '121212', '654321',
    '666666', '696969', '112233', '999999', '101010',
    '123123', '987654'
}

def isCommon2(mpin):
    return (mpin in commonPins) if len(mpin) == 4 else (mpin in commonMpinList_6)

def extract_segments2(date_str, mpin_length):
    if len(date_str) != 8:
        return set()

    dd = date_str[:2]
    mm = date_str[2:4]
    yyyy = date_str[4:]
    yy = yyyy[2:]
    
    if mpin_length == 4: #possible combinations of 4-digit
        return {
            dd + mm, mm + dd,
            dd + yy, yy + dd,
            mm + yy, yy + mm,
            yyyy
        }
    elif mpin_length == 6: #possible combinations of 6-digit
        return {
            dd + mm + yy, mm + dd + yy,
            yy + mm + dd, mm + yy + dd,
            dd + yy + mm, yy + dd + mm,
            mm + yyyy, yyyy + mm,
            dd + yyyy, yyyy + dd,
            dd + mm + yyyy[:2],
            mm + dd + yyyy[:2],
            yy + mm + yyyy[:2],
        }
    return set()

def isWeakByDemographics3(mpin, dob, spouse_dob, anniversary):#returns list of reasons for 4 and 6 digit weak mpins
    reasons = []
    length = len(mpin)
    if mpin in extract_segments2(dob, length):
        reasons.append("DEMOGRAPHIC_DOB_SELF")
    if mpin in extract_segments2(spouse_dob, length):
        reasons.append("DEMOGRAPHIC_DOB_SPOUSE")
    if mpin in extract_segments2(anniversary, length):
        reasons.append("DEMOGRAPHIC_ANNIVERSARY")
    return reasons