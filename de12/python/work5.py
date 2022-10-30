# どこにforをいれるか、タブでずらしていくのを忘れないのが重要！
for i in range(1,4):  
    print(i,"人目")
    
    name=input("名前を教えてください")
    waist=float(input("ウエストは？"))
    weight=float(input("体重は？"))
    height=float(input("身長は？"))
    age=int(input("年齢は？"))
    # floatは小数点必要なものintは少数点いらないもの

    print(name,"さんは現在",age,"歳で、体重",weight,"kg、身長",height,"cmで、ウエストは",waist,"cmです。")

    # どちらかが当てはまっているればコメントされる→or
    if weight>=50 or waist>59.5:
        print(name,"さん、筋トレサボってますね！")
    else:
        print(name,"さん、引き続き筋トレ頑張りましょう！")

    # 入力していかないとエラー出なかった