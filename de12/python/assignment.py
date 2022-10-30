import random
# ここではランダムを使うということを一番最初に書いた
name=input("名前を教えてください")
grade=input("学年を教えてください")
kamoku=""
# kamokuというまとまりをつくった

print(name,"さんは",grade,"年生ですね！")


# 質問1のまとまり
qone=int(input("質問1；授業は1限でもいいですか？　はい→1/いいえ→2"))
if qone<=1:
        print(name,"さんは1限でも頑張れるのですね！質問2へ")
        # 質問2のまとまり
        qtwo=int(input("質問2；成績評価は　テスト重視→1/出席重視→2"))
        if qtwo<=1:
                aone=random.randrange(4)
                if aone==0:
                        kamoku="哲学"
                elif aone==1:
                        kamoku="中国語"
                elif aone==2:
                        kamoku="データサイエンス"
                elif aone==3:
                        kamoku="化学"
                else:
                        kamoku="error!"
        else:
                aone=random.randrange(4)
                if aone==0:
                        kamoku="FYS"
                elif aone==1:
                        kamoku="健康科学とスポーツ"
                elif aone==2:
                        kamoku="文学・俳句研究"
                elif aone==3:
                        kamoku="人文地理学"
                else:
                        kamoku="error!"
else:
        print(name,"さんは質問3へ")
        # 質問3のまとまり
        qtwo=int(input("質問3；成績評価は　テスト重視→1/出席重視→2"))
        if qtwo<=1:
                aone=random.randrange(4)
                if aone==0:
                        kamoku="社会と人間"
                elif aone==1:
                        kamoku="物理科学"
                elif aone==2:
                        kamoku="基礎数学"
                elif aone==3:
                        kamoku="統計学"
                else:
                        kamoku="error!"
        else:
                aone=random.randrange(4)
                if aone==0:
                        kamoku="手話入門"
                elif aone==1:
                        kamoku="神奈川大学の歴史"
                elif aone==2:
                        kamoku="芸術"
                elif aone==3:
                        kamoku="コンピュータ演習"
                else:
                        kamoku="error!"

# ランダムに数字を表示させ、その数字に対する答え（講義名）をkamokuに代入できるようにした

print(name,"さんには",kamoku,"がオススメです！")
# そして、それを表示させた

