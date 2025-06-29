def gethensachi():
    return 75

def randomhensachi():
    import random
    return random.randint(40, 70)

def gethensachi_by_university(university_name):
    # 偏差値のデータベース（例）
    hensachi_data = {
        "東京大学": 70,
        "京都大学": 68,
        "大阪大学": 65,
        "早稲田大学": 63,
        "慶應義塾大学": 62,
        "明治大学": 60,
        "立教大学": 58,
        "中央大学": 57,
        "法政大学": 55,
        "関西学院大学": 54
    }
    
    return hensachi_data.get(university_name, None)