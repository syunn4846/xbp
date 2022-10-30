name="aaa"
waist=86
age=39

print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

if waist>=85 and age>=40: # =をつけるのを忘れると以上にならない
    print(name,"さん、内臓脂肪蓄積注意です")
else:
    print(name,"さん、腹囲は問題ありません")

name="m"
waist=60
weight=48
height=169
age=20

print(name,"さんは現在",age,"歳で、体重",weight,"kg、身長",height,"cmで、ウエストは",waist,"cmです。")

# どちらかが当てはまっているれば反応する→or
if weight>=50 or waist>60:
    print(name,"さん、筋トレサボってますね！")
else:
    print(name,"さん、引き続き筋トレ頑張りましょう！")