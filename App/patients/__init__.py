# ============================
#  Normal Vital Sign Ranges
# ============================

HR_MIN, HR_MAX = 60, 100
SBP_MIN, SBP_MAX = 90, 120
DBP_MIN, DBP_MAX = 60, 80
TEMP_MIN, TEMP_MAX = 36.1, 37.2
RR_MIN, RR_MAX = 12, 20


# ====================================
#  Function to Flag Abnormal Vitals
# ====================================

def flag_abnormal(patient):
	flags = {
		"heart_rate": False,
		"systolic_bp": False,
		"diastolic_bp": False,
		"temperature": False,
		"respiratory_rate": False
	}

	abnormal_count = 0

	if patient["heart_rate"] > HR_MAX or patient["heart_rate"] < HR_MIN:
		flags["heart_rate"] = True
		abnormal_count += 1

	if patient["systolic_bp"] > SBP_MAX or patient["systolic_bp"] < SBP_MIN:
		flags["systolic_bp"] = True
		abnormal_count += 1

	if patient["diastolic_bp"] > DBP_MAX or patient["diastolic_bp"] < DBP_MIN:
		flags["diastolic_bp"] = True
		abnormal_count += 1

	if patient["temperature"] > TEMP_MAX or patient["temperature"] < TEMP_MIN:
		flags["temperature"] = True
		abnormal_count += 1

	if patient["respiratory_rate"] > RR_MAX or patient["respiratory_rate"] < RR_MIN:
		flags["respiratory_rate"] = True
		abnormal_count += 1

	return flags, abnormal_count


# =====================
#  Assign Risk Level
# =====================

def assign_risk(abnormal_count, age):
	if age > 75 and abnormal_count >= 3:
		return "High"
	elif abnormal_count == 2 or (age > 60 and abnormal_count >= 1):
		return "Moderate"
	else:
		return "Low"


# ================================
#  Calculate Summary Statistics
# ================================

def calculate_statistics(patients):
	n = len(patients)
	if n == 0:
		return None

	total_hr = total_sbp = total_dbp = total_temp = total_rr = 0
	min_hr = max_hr = patients[0]["heart_rate"]
	min_sbp = max_sbp = patients[0]["systolic_bp"]
	min_dbp = max_dbp = patients[0]["diastolic_bp"]
	min_temp = max_temp = patients[0]["temperature"]
	min_rr = max_rr = patients[0]["respiratory_rate"]

	for p in patients:

		total_hr += p["heart_rate"]
		if p["heart_rate"] > max_hr: max_hr = p["heart_rate"]
		if p["heart_rate"] < min_hr: min_hr = p["heart_rate"]

		total_sbp += p["systolic_bp"]
		if p["systolic_bp"] > max_sbp: max_sbp = p["systolic_bp"]
		if p["systolic_bp"] < min_sbp: min_sbp = p["systolic_bp"]

		total_dbp += p["diastolic_bp"]
		if p["diastolic_bp"] > max_dbp: max_dbp = p["diastolic_bp"]
		if p["diastolic_bp"] < min_dbp: min_dbp = p["diastolic_bp"]

		total_temp += p["temperature"]
		if p["temperature"] > max_temp: max_temp = p["temperature"]
		if p["temperature"] < min_temp: min_temp = p["temperature"]

		total_rr += p["respiratory_rate"]
		if p["respiratory_rate"] > max_rr: max_rr = p["respiratory_rate"]
		if p["respiratory_rate"] < min_rr: min_rr = p["respiratory_rate"]

		
	stats = {
		"heart_rate": {"avg": total_hr/n, "min": min_hr, "max": max_hr},
		"systolic_bp": {"avg": total_sbp/n, "min": min_sbp, "max": max_sbp},
		"diastolic_bp": {"avg": total_dbp/n, "min": min_dbp, "max": max_dbp},
		"temperature": {"avg": total_temp/n, "min": min_temp, "max": max_temp},
		"respiratory_rate": {"avg": total_rr/n, "min": min_rr, "max": max_rr}
	}

	return stats

