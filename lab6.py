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
    "Communication and Expession": ["ARTH-204", "ARTH-205", "BA-450", "BI-130", "MUS-311"],
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


def main():

    student_bins = {
        "Creativity and Innovation": [
            ("ART-133", 3),
            ("ENG-105", 4)
        ],

        "Communication and Expression": [
            ("ARTH-204", 3)
        ],

        "Equity, Diversity, and Inclusion": [
            ("ART-450", 4)
        ],

        "Inquiry and Analysis": [
            ("ENG-280", 4),
            ("BI-101", 4)
        ],

        "Numerical Literacy": [
            ("CS-200", 4),
            ("MTH-111", 4)
        ],

        "Purposeful Learning": [
            ("WR-121z", 3)
        ],

        "Uncategorized": [
            ("HIST-100", 3)
        ]
    }

    credit_totals = audit_credits(student_bins)

    print(credit_totals)


if __name__ == "__main__":
    main()


    