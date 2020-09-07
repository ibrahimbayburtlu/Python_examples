import random

def generate_names():
    first_name=["İbrahim","Furkan","Berk","Yusuf","Mert","Umut","Enes"]
    last_name=["Bayburtlu","Bingöl","Özgür","Eser","Koç","Çalışkan","Türköz"]
    return "{} {}".format(random.choices(first_name),random.choices(last_name))

for i in range(5):
    print(generate_names())