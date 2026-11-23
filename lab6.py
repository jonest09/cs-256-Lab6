from unittest import result

def parse_course_record(course_string):
    """
    Takes a course string and returns a dictionary
    """

    course_parts = course_string.split(",")

    code = course_parts[0].strip()
    name = course_parts[1].strip()
    credits = int(course_parts[2].strip())
    status = course_parts[3].strip()

    course = {
        'code': code,
        'name': name,
        'credits': credits,
        'status': status
    }

    return course

gen_ed_categories = {
    "Creativity and Innovation": ["ART-133", "ART-291", "ENG-105", "GSWS-210", "MUS-330"],
    "Communication and Expression": ["ARTH-204", "ARTH-205", "BA-450", "BI-130", "MUS-311"],
    "Equity, Diversity, and Inclusion": ["ART-450", "ENG-214", "ES-220", "GSWS-312", "MUS-205"],
    "Inquiry and Analysis": ["GSWS-300", "ES-200", "ENG-280", "BI-101", "COMM-482"],
    "Numerical Literacy": ["CS-200", "MTH-111", "CS-346", "STAT-243z"],
    "Purposeful Learning": ["WR-121z", "WR-122z", "WR-123"]
}

def get_gen_ed_category(course_code, gen_ed_mapping):

    for category in gen_ed_mapping:

        if course_code in gen_ed_mapping[category]:
            return category

    return "Uncategorized"


def audit_credits(student_bins):

    audit = {
        "Creativity and Innovation": 0,
        "Communication and Expression": 0,
        "Equity, Diversity, and Inclusion": 0,
        "Inquiry and Analysis": 0,
        "Numerical Literacy": 0,
        "Purposeful Learning": 0,
        "Uncategorized": 0
    }

    for bin in student_bins:

        total_credits = 0

        for course in student_bins[bin]:

            code, credits = course
            total_credits = total_credits + credits

        audit[bin] = total_credits

    return audit



def bin_student_course(transcript, gen_ed_mapping):

    student_bins = {}

    for category in gen_ed_mapping:
        student_bins[category] = []

    student_bins["Uncategorized"] = []

    for course in transcript:

        course_record = parse_course_record(course)

        course_code = course_record["code"]
        course_credits = course_record["credits"]
        course_status = course_record["status"]

        category = get_gen_ed_category(course_code, gen_ed_mapping)

        if course_status.lower() == "completed":

            student_bins[category].append((course_code, course_credits))

    return student_bins

def main():

    # Create the Gen Ed categories
    gen_ed_categories = {
        "Creativity and Innovation": [
            "ART-133", "ART-291", "ENG-105",
            "GSWS-210", "MUS-330"
        ],

        "Communication and Expression": [
            "ARTH-204", "ARTH-205", "BA-450",
            "BI-130", "MUS-311"
        ],

        "Equity, Diversity, and Inclusion": [
            "ART-450", "ENG-214", "ES-220",
            "GSWS-312", "MUS-205"
        ],

        "Inquiry and Analysis": [
            "GSWS-300", "ES-200", "ENG-280",
            "BI-101", "COMM-482"
        ],

        "Numerical Literacy": [
            "CS-200", "MTH-111", "CS-346",
            "STAT-243z"
        ],

        "Purposeful Learning": [
            "WR-121z", "WR-122z", "WR-123"
        ]
    }

    # Create the student transcript
    transcript = (
        "ART-133, Drawing, 3, COMPLETED",
        "ENG-105, Creative Writing, 4, COMPLETED",
        "ARTH-204, Art History, 3, COMPLETED",
        "ART-450, Diversity Studies, 4, COMPLETED",
        "ENG-280, Research Methods, 4, COMPLETED",
        "BI-101, Biology, 4, COMPLETED",
        "CS-200, Computer Science, 4, COMPLETED",
        "MTH-111, Pre-calculus, 4, COMPLETED",
        "WR-121z, Composition I, 3, COMPLETED",
        "WR-122z, Composition II, 3, INCOMPLETE",
        "HIST-100, World History, 3, COMPLETED"
    )

    # Sort the student courses into Gen Ed bins
    student_final_bins = bin_student_course(
        transcript, gen_ed_categories
    )

    print("Student course bins")
    print(student_final_bins)

    # Calculate totale credits
    credits_totals = audit_credits(student_final_bins)

    print("\nTotal completed credits")
    print(credits_totals)

if __name__ == "__main__":
    main()
    
