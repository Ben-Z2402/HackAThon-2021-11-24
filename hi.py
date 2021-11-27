def AvgTuitionCost():
    user_choice = input()
    user_choice = user_choice.lower()

    if user_choice == "dentistry":
        return int(22731)
    elif user_choice == "medicine":
        return int(14604)
    elif user_choice == "veterinary medicine":
        return int(14374)
    elif user_choice == "law":
        return int(12910)
    elif user_choice == "pharmacy":
        return int(11373)
    elif user_choice == "optometry":
        return int(10735)
    elif user_choice == "engineering":
        return int(8184)
    elif user_choice == "business, management and public administration":
        return int(6991)
    elif user_choice == "mathematics, computer and information sciences":
        return int(6953)
    elif user_choice == "architecture":
        return int(6519)
    elif user_choice == "physical and life sciences and technologyies":
        return int(6246)
    elif user_choice == "other health, parks, recreation and fitness":
        return int(6083)
    elif user_choice == "visual and performing arts, and communications technologies":
        return int(5926)
    elif user_choice == "personal, protective and transportation services":
        return int(5828)
    elif user_choice == "nursing":
        return int(5822)
    elif user_choice == "agriculture, natural resources and conservation":
        return int(5820)
    elif user_choice == "humanities":
        return int(5754)
    elif user_choice == "social and behavioural sciences, and legal studies":
        return int(5725)
    elif user_choice == "education":
        return int(4947)
    else:
        print("invalid input, please input a listed option")

AvgTuitionCost()