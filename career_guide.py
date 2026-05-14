# Career Path Guide v4.0

def career_guide():
    """Provides a user-friendly career guide with an expanded list of professions and detailed guidance."""

    name = input("Enter your name: ")
    print(f"\nWelcome, {name}! Your journey to a fulfilling career starts now.")

    professions = {
        "1": {"title": "Engineer", "guidance": "Excel in mathematics and physics. Develop strong problem-solving and analytical skills. Consider internships to gain practical experience."},
        "2": {"title": "Doctor", "guidance": "Focus on biology, chemistry, and organic chemistry. Volunteer at hospitals or clinics. Prepare for the MCAT and maintain a high GPA."},
        "3": {"title": "Scientist", "guidance": "Cultivate a deep sense of curiosity. Engage in research projects, even at an undergraduate level. Learn data analysis and scientific writing."},
        "4": {"title": "Teacher", "guidance": "Develop strong communication and interpersonal skills. Gain experience working with students through tutoring or volunteering. Pursue a degree in education."},
        "5": {"title": "Artist", "guidance": "Build a strong portfolio of your work. Master the fundamentals of your chosen medium. Network with other artists and seek feedback."},
        "6": {"title": "Writer", "guidance": "Read extensively across different genres. Write consistently to develop your voice. Seek publication opportunities in literary magazines or online platforms."},
        "7": {"title": "Musician", "guidance": "Practice your instrument or voice daily. Study music theory and composition. Collaborate with other musicians and perform live."},
        "8": {"title": "Entrepreneur", "guidance": "Identify a problem and develop a unique solution. Learn about business planning, marketing, and finance. Be prepared to take calculated risks."},
        "9": {"title": "Software Developer", "guidance": "Master at least one programming language. Build projects to showcase your skills on platforms like GitHub. Stay updated with the latest technologies."},
        "10": {"title": "Graphic Designer", "guidance": "Learn the principles of design, color theory, and typography. Master industry-standard software like Adobe Creative Suite. Create a professional portfolio."}
    }

    print("\nChoose your desired profession:")
    for key, profession in professions.items():
        print(f"{key}. {profession['title']}")

    choice = input(f"\nEnter your choice (1-{len(professions)}): ")

    if choice in professions:
        selected = professions[choice]
        print(f"\nGoal: {selected['title']}\n\nGuidance: {selected['guidance']}")
    else:
        print("\nInvalid choice. Focus on finding your passion first!")

    print("\n[Status: Your career insights have been generated]")

if __name__ == "__main__":
    career_guide()
