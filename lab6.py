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

        if course_status == "Completed":

            student_bins[category].append((course_code, course_credits))

    return student_bins

def main():

    transcript = (
        "MTH-111, Pre-calculus, 4, COMPLETED",
        "WR-121z, Composition I, 3, COMPLETED",
        "WR-122z, Composition II, 3, INCOMPLETE",
        "GSWS-210, Violence Prevention, 4, COMPLETED",
        "HIST-100, World History, 3, COMPLETED"
    )

    student_bins = bin_student_course(
        transcript, gen_ed_categories
    )

    print(student_bins)


if __name__ == "__main__":
    main()
                                    


    