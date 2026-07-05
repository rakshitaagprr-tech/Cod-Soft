print("========== Course Recommendation System ==========")

print("\nChoose your interest:")
print("1. Artificial Intelligence")
print("2. Web Development")
print("3. Data Science")
print("4. Cyber Security")
print("5. Mobile App Development")

choice = input("\nEnter your choice (1-5): ")

if choice == "1":
    print("\nRecommended Courses:")
    print("- Python Programming")
    print("- Machine Learning")
    print("- Deep Learning")
    print("- Artificial Intelligence")

elif choice == "2":
    print("\nRecommended Courses:")
    print("- HTML & CSS")
    print("- JavaScript")
    print("- React JS")
    print("- Django")

elif choice == "3":
    print("\nRecommended Courses:")
    print("- Python")
    print("- Statistics")
    print("- SQL")
    print("- Data Visualization")

elif choice == "4":
    print("\nRecommended Courses:")
    print("- Ethical Hacking")
    print("- Network Security")
    print("- Kali Linux")
    print("- Cryptography")

elif choice == "5":
    print("\nRecommended Courses:")
    print("- Java")
    print("- Kotlin")
    print("- Flutter")
    print("- Android Development")

else:
    print("Invalid Choice!")
