
# Task 1: Student Scholarship Eligibility System

# Step 1: Display program title
print("==========================================")
print("STUDENT SCHOLARSHIP SYSTEM")
print("==========================================")

# Step 2: Get student's name
student_name = input("Enter Student Name: ")

# Step 3: Get and validate academic marks
marks = float(input("Enter Academic Marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid Marks! Marks must be between 0 and 100.")

else:
    # Step 4: Get and validate attendance percentage
    attendance = float(input("Enter Attendance Percentage (0-100): "))

    if attendance < 0 or attendance > 100:
        print("Invalid Attendance! It must be between 0 and 100.")

    else:
        # Step 5: Get and validate monthly family income
        family_income = float(input("Enter Monthly Family Income (Rs.): "))

        if family_income < 0:
            print("Invalid Income! Income cannot be negative.")

        else:
            # Step 6: Check scholarship eligibility conditions

            # Initially, assume the student is eligible
            eligible = True

            # Check academic marks
            if marks < 80:
                eligible = False

            # Check attendance percentage
            if attendance < 85:
                eligible = False

            # Check monthly family income
            if family_income > 50000:
                eligible = False

            # Step 7: Decide scholarship type
            if eligible == True:

                if marks >= 90:
                    scholarship = "Full Scholarship"

                elif marks >= 80:
                    scholarship = "Partial Scholarship"

            else:
                scholarship = "Not Eligible"

            # Step 8: Display complete evaluation report
            print("\n==========================================")
            print("       SCHOLARSHIP EVALUATION REPORT")
            print("==========================================")

            print("Student Name:", student_name)
            print("Academic Marks:", marks, "%")
            print("Attendance:", attendance, "%")
            print("Monthly Family Income: Rs.", family_income)

            print("------------------------------------------")

            # Step 9: Display eligibility result and reasons
            if eligible == True:
                print("Eligibility Status: Eligible")
                print("Scholarship Award:", scholarship)

            else:
                print("Eligibility Status: Not Eligible")
                print("Reason(s) for Ineligibility:")

                if marks < 80:
                    print("- Academic marks are below 80%.")

                if attendance < 85:
                    print("- Attendance is below 85%.")

                if family_income > 50000:
                    print("- Monthly family income exceeds Rs. 50,000.")

            print("==========================================")
            print("       EVALUATION COMPLETED")
            print("==========================================")
