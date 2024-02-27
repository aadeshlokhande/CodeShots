msgs ="Ready to code? %0AJoin ICE Computers, Nagpur! %0ALearn C, C++, Python, Java, Web Development. %0AEnroll: 9673067036. %0AYour coding journey starts here!".replace(" ","+")
msg = f"https://wa.me/9767355587?text={msgs}"


file = open("aa.txt","w")
file.write(f"{msg}")
file.close()