
import discord ##discordでBOTを使うのにこれが必ずいる
import random ##運勢リストからランダムに出力するために必要

lot_channel_id = "694570598512328754" #ここにコマンドを送るチャンネルID
lot_result_channel_id = "694570598512328754" #ここに結果を出力するチャンネルID

client = discord.Client()

@client.event #BOT起動時にcmdに表示される部分で無くてもよい
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message): #メッセージを受け取る関数なので必ず必要
    if message.content == "あおみは？": #:を忘れずつけよう！Enterを押すと自動で4文字分あけて改行されるよ！
        uranai = ["雑魚", "くそ雑魚", "クラマス", "黒髪ボブ", "開幕解読恐怖", "天才", "良い子", "リーダー"]
        choi = random.choice(uranai)
        await client.send_message(message.channel, choi)
    
    if message.content == "PONは？": #:を忘れずつけよう！Enterを押すと自動で4文字分あけて改行されるよ！
        uranai = ["天才", "元クラマス", "現サブマス", "最強", "もうすぐ引退", "ピーオン", "歌うまい人", "ぽんこつやろう", "利敵", "ぽん大貧民は草", "あおみよりくそ雑魚"]
        choi = random.choice(uranai)
        await client.send_message(message.channel, choi)

    if message.content == "しゆは？": #:を忘れずつけよう！Enterを押すと自動で4文字分あけて改行されるよ！
        uranai = ["しゆうさちゃん", "救助恐怖", "技師", "Dさんの元相方", "いけめん"]
        choi = random.choice(uranai)
        await client.send_message(message.channel, choi)

    if message.content == "占い":
        unsei = ["大吉", "中吉", "吉", "末吉", "小吉", "凶", "大凶"]
        choice = random.choice(unsei) #randomモジュール使用
        uranau = ["★", "★★", "★★★", "★★★★", "★★★★★",]
        choice2 = random.choice(uranau)
        uranau3 = ["★", "★★", "★★★", "★★★★", "★★★★★",]
        choice3 = random.choice(uranau3)
        uranau4 = ["★", "★★", "★★★", "★★★★", "★★★★★",]
        choice4 = random.choice(uranau4)
        uranau5 = ["★", "★★", "★★★", "★★★★", "★★★★★",]
        choice5 = random.choice(uranau5)
        uranai2 = ["幸運児", "弁護士", "医師", "泥棒", "庭師", "マジシャン", "冒険家", "空軍", "機械技師", "傭兵", "オフェンス", "心眼", "祭司", "調香師", "カウボーイ", "踊り子", "占い師", "納棺師", "探鉱者", "呪術師", "野人", "曲芸師", "一等航海士", "バーメイド", "ポストマン", "墓守", "囚人"]
        uranau2 = random.choice(uranai2)
        uranai3 = ["復習者", "断罪狩人", "道化師", "リッパー", "結魂者", "芸者", "黄衣の王", "白黒無常", "写真家", "狂眼", "夢の魔女", "泣き虫", "魔トカゲ", "血の王女", "ガードNo.26", "使徒"]
        uranau6 = random.choice(uranai3)
        uranai4 = ["フクロウ付けたジャン！ｱｱｱｱｱｱｱｱ！", "おーとこれは！！ボロタイで殴られた後に付けてしまいましたー！", "これは凄い！フクロウの枠が見えませんでした！", "あー残念！即付けを狙い過ぎて腐ってしまいました！", "あー残念！自分に付けてしまいました！居た堪れない！"]
        uranau7 = random.choice(uranai4)
        num = random.randint(1, 100)
        if message.channel.id == lot_channel_id:
            lot_result_channel = [channel for channel in client.get_all_channels() if channel.id == lot_result_channel_id][0]
            await client.send_message(lot_result_channel, message.author.mention + "の運勢```\n運勢　" + choice + "\n総合運　" + choice2 + "\nサバイバー運　" + choice3 + "\nハンター運　" + choice4 + "\nランクマ運　" + choice5 + "\nラッキーサバイバー　" + uranau2 + "\nラッキーハンター　" + uranau6 + "\n利敵率　" + str(num) + "%" + "\n即時フクロウの呼吸　" + str(uranau7) + "```")
        else:
            await client.send_message(message.channel, "ここではコマンドは実施できません") #指定したIDじゃない場合実行される

    if message.content == "&help":
        if message.channel.id == lot_channel_id:
            lot_result_channel = [channel for channel in client.get_all_channels() if channel.id == lot_result_channel_id][0]
            await client.send_message(lot_result_channel, "```・○○は？でその人がどんな人か分かります\nあおみは？, PONは？, しゆは？\n・占い イライ君があなたの運勢を占うよ！\n・&help イライ君の使い方を表示```")
        else:
            await client.send_message(message.channel, "ここではコマンドは実施できません") #指定したIDじゃない場合実行される

        

# この＊＊＊に自分のトークンを書き替える
client.run('Njk0NDk5NTgxMjI0MDI2MTIy.XoNAEg.j8fiZOUuFek0DhYrKEWHFSyCb4g')
