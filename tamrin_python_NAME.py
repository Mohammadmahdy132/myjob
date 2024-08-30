def Name(name, **dic):
    
    List_Name = dic["Name"]

    if name in List_Name:
        Index = List_Name.index(name)

        print(f"*** {name} ***")
        print(f"Score: {dic['Score'][Index]} ")
        print(f"City: {dic['City'][Index]} ")
        print(f"Age: {dic['Age'][Index]} ")

        if dic['education'][Index] == 'B':
            print(f"education: Bachelor ")
        elif  dic['education'][Index] == 'M':
            print(f"education: Masters ")  
        elif  dic['education'][Index] == 'D':
            print(f"education: Doctorate ")  

        print(f"Expertise: {dic['Expertise'][name]} ")

    else:
        print("نام وارد شده یافت نشد")
# =====================================================================

def Expertise(expet, **dic):
    
    text2 = expet.split(' , ')
    text3 = set()

    for i in dic['Expertise']:
        for j in range(len(text2)):
            if text2[j] in dic['Expertise'][i][:]:
                text3.add(i)
                
    return text3





Students = {
    "Name" : ["Farhad", "Afarin", "Mahsa", "Nima", "Ali", "Rasoul", "Mehran", "Zahra", "Mohsen", "Ahmad"],
    "Score" : [18, 19, 17, 16, 20, 20, 19, 17, 18, 18],
    "City" : ["Kermanshah", "Tehran", "Tehran", "Tabriz", "Tehran", "Kermanshah", "Kermanshah", "Tehran", "Kermanshah", "Tabriz"],
    "Age" : [24, 29, 21, 28, 25, 26, 32, 23, 25, 26],
    "education" : ["B", "M", "B", "M", "M", "B", "D", "B", "M", "M"],
    
    "Expertise" :
    {
        "Farhad": ["C#", "Java", "Asp.Net"],
        "Afarin": ["Python", "Deep Learning", "Machine Learning", "AI"],
        "Mahsa": ["C++", "C#", "Asp.Net", "AI", "Java", "Sql Server"],
        "Nima": ["C#", "Fuzzy Logic", "Django", "AI"],
        "Ali": ["AI", "Machine Learning", "Python", "Mongo DB", "Deep Learning", "Django"],
        "Rasoul": ["Fuzzy Logic", "Mongo DB", "AI"],
        "Mehran": ["Mongo DB", "Asp.Net", "Machine Learning", "Sql Server"],
        "Zahra": ["Deep Learning", "Machine Learning", "Python", "Sql Server", "AI"],
        "Mohsen": ["Django", "Python", "C#", "Asp.Net", "Mongo DB", "AI"],
        "Ahmad": ["C++", "Java"]
    }
}




while(True):
    Name(input("name:"), **Students)


