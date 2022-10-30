name=input("名前を教えてください")
waist=input("ウエストは？")
weight=input("体重は？")
height=input("身長は？")
age=input("年齢は？")

print(name,"さんは現在",age,"歳で、体重",weight,"kg、身長",height,"cmで、ウエストは",waist,"cmです。")

# どちらかが当てはまっているればコメントされる→or
if weight>=50 or waist>60:
    print(name,"さん、筋トレサボってますね！")
else:
    print(name,"さん、引き続き筋トレ頑張りましょう！")

# 入力していかないとエラー出なかった