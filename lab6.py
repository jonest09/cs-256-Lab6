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
def main():

    test_course = " MTH-111, Pre-calculus, 4, Completed "

    result = parse_course_record(test_course)

    print(result)

if __name__ == "__main__":
    main()

    