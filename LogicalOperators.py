has_high_income=True
has_good_credit=True
has_criminal_record = False
if has_high_income and has_good_credit:
    print("You are eligible for loan")
if has_good_credit and not has_criminal_record:
    print("You are a good civilian")

temperature =30

if temperature >= 30:
    print("Its a hot day")
elif temperature == 25:
    print("Its a pleasant day")
else:
    print("bad choice")