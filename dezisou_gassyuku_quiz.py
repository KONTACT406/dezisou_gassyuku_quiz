import tkinter as tk
import tkinter.messagebox as tmsg
import tkinter.ttk as ttk
import random

correct_count = 0
incorrect_count = 0
question_count = 1

ronde_b = "ロンド B スクエア"
biz_ud = "BIZ UDゴシック"

window_size_horizontal = 1024
window_size_virtical = 768
min_x = 0 
max_x = window_size_horizontal
min_y = 0 
max_y = window_size_virtical
half_x = max_x / 2
half_y = max_y / 2

title_main_str = "デジ創合宿-2023夏-思い出クイズ"
title_sub_str = "思い出クイズ"

q = [
    "空要素",
    "自転車で湖畔を回ったのは何湖？",
    "河口湖多佳美のパネルは合計で何人いた？(半角数字のみ入力)",
    "忍野八海の中池で泳いでいた動物は？(ひらがな)",
    "1日目の夜にどるぱが徘徊していた目的は何を探すため？",
    "鳴沢氷穴から出た時にKONの帽子にくっついていたものは？"
    ]
    
a = [
    "空要素",
    "山中湖",
    "6",
    "ねずみ",
    "松前重義像",
    "しゃくとり虫"
    ]

a_fake_1 = [
    "空要素",
    "河口湖",
    "3",
    "たぬき",
    "幽霊",
    "コウモリ"
]

a_fake_2 = [
    "空要素",
    "西湖",
    "10",
    "かえる",
    "自販機",
    "氷塊"
]

a_fake_3 = [
    "空要素",
    "琵琶湖",
    "20",
    "つちのこ",
    "つちのこ",
    "つちのこ"
]


def ChangeToQuiz():
    global frame_quiz
    global entry1_frame_quiz

    if question_count == 1:
        frame_start.destroy()
    else:
        frame_answer.destroy()

    # メインフレームの作成と設置
    frame_quiz = ttk.Frame(root)
    frame_quiz.pack(fill = tk.BOTH, pady=20)

    # 各種ウィジェットの作成
    label1_frame_quiz = ttk.Label(frame_quiz, text="第"+str(question_count)+"問", font=(ronde_b, 28))
    label1_question_frame_quiz = ttk.Label(frame_quiz, text=q[question_count], font=(ronde_b, 28))
    label1_choice_1_frame_quiz = ttk.Label(frame_quiz, text=a[question_count], font=(ronde_b, 28))
    label1_choice_2_frame_quiz = ttk.Label(frame_quiz, text=a_fake_1[question_count], font=(ronde_b, 28))
    label1_choice_3_frame_quiz = ttk.Label(frame_quiz, text=a_fake_2[question_count], font=(ronde_b, 28))
    label1_choice_4_frame_quiz = ttk.Label(frame_quiz, text=a_fake_3[question_count], font=(ronde_b, 28))
    entry1_frame_quiz = ttk.Entry(frame_quiz)
    button_change_frame_quiz = ttk.Button(frame_quiz, text="決定", padding=[5,10], style="basic.TButton", command=ChangeToAnswer)

    # 各種ウィジェットの設置
    label1_frame_quiz.pack(pady=20)
    label1_question_frame_quiz.pack(pady=20)
    
    order = [1, 2, 3, 4]
    random.shuffle(order)
    for i in range(4):
        if order[i] == 1:
            label1_choice_1_frame_quiz.pack(pady=20)
        elif order[i] == 2:
            label1_choice_2_frame_quiz.pack(pady=20)
        elif order[i] == 3:
            label1_choice_3_frame_quiz.pack(pady=20)
        elif order[i] == 4:
            label1_choice_4_frame_quiz.pack(pady=20)

    entry1_frame_quiz.pack(pady=20)
    button_change_frame_quiz.pack(pady=20)

def ChangeToAnswer():
    global frame_answer
    global correct_count
    global incorrect_count

    ans = entry1_frame_quiz.get()
    if ans == a[question_count]:
        correct_count += 1
    else:
        incorrect_count += 1

    frame_quiz.destroy()

    # メインフレームの作成と設置
    frame_answer = ttk.Frame(root)
    frame_answer.pack(fill = tk.BOTH, pady=20)

    # 各種ウィジェットの作成
    label1_frame_answer = ttk.Label(frame_answer, text="解答・解説", font=(ronde_b, 28))
    label1_frame_answer_answer = ttk.Label(frame_answer, text="正答："+a[question_count], font=(ronde_b, 28))
    button_change_frame_answer = ttk.Button(frame_answer, text="次へ", padding=[5,10], style="basic.TButton", command=JudgeEnd)

    # 各種ウィジェットの設置
    label1_frame_answer.pack(pady=20)
    label1_frame_answer_answer.pack(pady=20)
    button_change_frame_answer.pack(pady=20)

def JudgeEnd():
    global question_count
    if(question_count == 5):
        question_count = 1
        ChangeToResult()
    else:
        question_count += 1
        ChangeToQuiz()

def ChangeToResult():
    global frame_result

    frame_answer.destroy()

    # メインフレームの作成と設置
    frame_result = ttk.Frame(root)
    frame_result.pack(fill = tk.BOTH, pady=20)

    # 各種ウィジェットの作成
    label1_frame_result = ttk.Label(frame_result, text="結果発表！！", font=(ronde_b, 28))
    label1_correct_frame_result = ttk.Label(frame_result, text="正解数"+str(correct_count)+"問", font=(ronde_b, 28))
    label1_incorrect_frame_result = ttk.Label(frame_result, text="不正解数"+str(incorrect_count)+"問", font=(ronde_b, 28))
    button_change_frame_result = ttk.Button(frame_result, text="次へ", padding=[5,10], style="basic.TButton", command=ChangeToNickname)

    # 各種ウィジェットの設置
    label1_frame_result.pack(pady=20)
    label1_correct_frame_result.pack(pady=20)
    label1_incorrect_frame_result.pack(pady=20)
    button_change_frame_result.pack(pady=20)

def ChangeToNickname():
    global frame_nickname
    global entry1_frame_nickname

    frame_result.destroy()

    # メインフレームの作成と設置
    frame_nickname = ttk.Frame(root)
    frame_nickname.pack(fill = tk.BOTH, pady=20)

    # 各種ウィジェットの作成
    label1_frame_nickname = ttk.Label(frame_nickname, text="名前を入れてね", font=(ronde_b, 28))
    entry1_frame_nickname = ttk.Entry(frame_nickname)
    button_change_frame_nickname = ttk.Button(frame_nickname, text="決定", padding=[5,10], style="basic.TButton", command=NameInput)

    # 各種ウィジェットの設置
    label1_frame_nickname.pack(pady=20)
    entry1_frame_nickname.pack(pady=20)
    button_change_frame_nickname.pack(pady=20)

def NameInput():
    # 入力された文字列を取得
    name = entry1_frame_nickname.get()

    # 名前とスコアをリザルトとして出力
    path_w = 'result.txt'
    s = name + ',' + str(correct_count) + ',' + str(incorrect_count) + '\n'

    with open(path_w, mode='a') as f:
        f.write(s)

    # # 入力できているかチェック
    # tmsg.showinfo("test", name)
    ChangeToStart()

def ChangeToStart():
    global frame_start
    global correct_count
    global incorrect_count
    global question_count
    
    correct_count = 0
    incorrect_count = 0
    question_count = 1

    frame_nickname.destroy()

    # メインフレームの作成と設置
    frame_start = ttk.Frame(root)
    frame_start.pack(fill = tk.BOTH, pady=20)

    # 各種ウィジェットの作成
    label1_logo_frame_start = ttk.Label(frame_start, image=logo_img)
    label1_frame_start = ttk.Label(frame_start, text=title_sub_str, font=(ronde_b, 28))
    button_change_frame_start = ttk.Button(frame_start, text="スタート", padding=[5,10], style="basic.TButton", command=ChangeToQuiz)

    # 各種ウィジェットの設置
    label1_logo_frame_start.pack(pady=20)
    label1_frame_start.pack(pady=20)
    button_change_frame_start.pack(pady=20)

if __name__ == "__main__":
    # rootメインウィンドウの設定
    root = tk.Tk()
    root.title(title_main_str)
    root.geometry(str(window_size_horizontal) + "x" + str(window_size_virtical))

    # メインフレームの作成と設置
    frame_start = ttk.Frame(root)
    frame_start.pack(fill = tk.BOTH, pady=20)

    #ボタンのスタイルの作成
    style = ttk.Style()
    style.configure("basic.TButton", font=(ronde_b, 20), anchor="S")
    
    #　ロゴ画像のロード
    logo_img = tk.PhotoImage(file="Logo_s.png")

    # 各種ウィジェットの作成
    label1_logo_frame_start = ttk.Label(frame_start, image=logo_img)
    label1_frame_start = ttk.Label(frame_start, text=title_sub_str, font=(ronde_b, 28))
    button_change_start = ttk.Button(frame_start, text="スタート", padding=[5,10], style="basic.TButton", command=ChangeToQuiz)

    # 各種ウィジェットの設置
    label1_logo_frame_start.pack(pady=20)
    label1_frame_start.pack(pady=20)
    button_change_start.pack(pady=20)

    root.mainloop()

# ------------------------------------------------------------------------------

# for f in tk.Tk().call("font", "families"):  # フォント一覧取得
#     print(f)

# version = tk.Tcl().eval('info patchlevel')  # tkinterバージョン確認
# print(version)

# #クイズのメイン部分
# def quiz():
#     collect_count = 0
#     incollect_count = 0
#     FutodokimonoFlag = False

#     q = ["空要素",
#          "自転車で湖畔を回ったのは何湖？",
#          "河口湖多佳美のパネルは合計で何人いた？(数字のみ入力)",
#          "忍野八海の中池で泳いでいた動物は？(ひらがな)",
#          "1日目の夜にどるぱが徘徊していた目的は何を探すため？",
#          "鳴沢氷穴から出た時にKONの帽子にくっついていたものは？"]
    
#     a = ["空要素",
#          "山中湖",
#          "6",
#          "ねずみ",
#          "松前重義像",
#          "しゃくとり虫"
#         ]

#     for i in range(1,6):
#         print("第"+str(i)+"問")
#         print(q[i])
#         ans = input()
#         if ans == a[i]:
#             print("正解！")
#             collect_count += 1
#         else:
#             print("不正解！")
#             incollect_count += 1
#             if i == 1:
#                 FutodokimonoFlag = True
    
#     rank = result(collect_count, FutodokimonoFlag)

#     print("結果発表！")
#     print("正解数："+ str(collect_count) + "問")
#     print("不正解数："+ str(incollect_count) + "問")
#     print("あなたは...")
#     print(rank)

# # 結果に応じて称号を決める関数
# def result(right, flag):
#     if right == 5:
#         title = "名誉合宿参加者"
#     elif right >= 3:
#         title = "合宿を楽しみし者"
#     elif right >= 2:
#         title = "合宿参加者"
#     else:
#         title = "不届き者"

#     if flag == True:
#         title = "不届き者"

#     return title




# 実装部

# print("デジ創合宿-2023夏-思い出クイズ")
# print("please push 's' to start")

# command = input()

# if (command == 's'):
#     quiz()

# -----------------------------------------------------------------------------------------------------

# status = "Answer"
# correct_count = 0
# incorrect_count = 0
# question_count = 1

# window_size_horizontal = 1024
# window_size_virtical = 768
# min_x = 0 
# max_x = window_size_horizontal
# min_y = 0 
# max_y = window_size_virtical
# half_x = max_x / 2
# half_y = max_y / 2

# title_main_str = "デジ創合宿-2023夏-思い出クイズ"
# title_sub_str = "思い出クイズ"

# q = [
#     "空要素",
#     "自転車で湖畔を回ったのは何湖？",
#     "河口湖多佳美のパネルは合計で何人いた？(数字のみ入力)",
#     "忍野八海の中池で泳いでいた動物は？",
#     "1日目の夜にどるぱが徘徊していた目的は何を探すため？",
#     "鳴沢氷穴から出た時にKONの帽子にくっついていたものは？"
#     ]
    
# a = [
#     "空要素",
#     "山中湖",
#     "6",
#     "ねずみ",
#     "松前重義像",
#     "しゃくとり虫"
#     ]

# a_fake_1 = [
#     "空要素",
#     "河口湖",
#     "3",
#     "たぬき",
#     "幽霊",
#     "コウモリ"
# ]

# a_fake_2 = [
#     "空要素",
#     "西湖",
#     "10",
#     "かえる",
#     "自販機",
#     "氷塊"
# ]

# a_fake_3 = [
#     "空要素",
#     "琵琶湖",
#     "20",
#     "ツチノコ",
#     "ツチノコ",
#     "ツチノコ"
# ]

# def NameInput():
#     # 入力された文字列を取得
#     name = name_input_box.get()
#     status = "Start"
#     # 入力できているかチェック
#     # tmsg.showinfo("test", name)

# def QuizStart():
#     status = "NameInput"

# def QuizAnswer():
#     answer_num = question_answer_box.get()
#     status = "Start"

# def AnswerNext():
#     # クイズを終了するかどうか
#     if question_count == 6:
#         status = "Result"
#     else:
#         status = "Question"

# if __name__ == "__main__":
#     # rootメインウィンドウの設定

#     root = tk.Tk()

#     # ウィンドウサイズ
#     root.geometry(str(window_size_horizontal) + "x" + str(window_size_virtical))
#     # ウィンドウタイトル
#     root.title(title_main_str)

#     # メインフレームの作成と設置
#     frame = ttk.Frame(root)
#     frame.pack(fill = tk.BOTH, pady=20)

#     # # 各種ウィジェットの作成
#     # label1_frame = ttk.Label(frame, text="メインウィンドウ")
#     # entry1_frame = ttk.Entry(frame)
#     # button_change = ttk.Button(frame, text="ウィンドウ変更", command=change)

#     # # 各種ウィジェットの設置
#     # label1_frame.pack()
#     # entry1_frame.pack()
#     # button_change.pack()



# # -----------------------------------------------------------------------------------------------------
#     # タイトル画面
#     # キャンバス作成
#     canvas_back = tk.Canvas(root, bg="#e0ffff", height=window_size_virtical, width=window_size_horizontal)
#     canvas_logo = tk.Canvas(root, bg="#e0ffff", height=window_size_virtical, width=window_size_horizontal)
#     # キャンバス表示
#     canvas_back.place(x=min_x, y=min_y)
#     canvas_logo.place(x=150, y=-50)

#     # イメージ作成
#     logo_img = tk.PhotoImage(file="Logo_s.png", width=679, height=480)
#     # キャンバスにイメージを表示
#     canvas_logo.create_image(30, 30, image=logo_img, anchor=tk.NW)

#     # サブタイトル表示
#     title_title_label = ttk.Label(frame, text=title_sub_str, font=("ロンド B スクエア", 28))
#     title_title_label.place(x = 400, y = 500)

#     # pressメッセージ表示
#     title_press_label = ttk.Label(frame, text="please push 's' to start", font=("ロンド B スクエア", 28))
#     title_press_label.place(x = 370, y = 620)

#     # スタートボタン表示
#     title_start_button = ttk.Button(frame, text="決定", font=("ロンド B スクエア", 28), command=QuizStart)
#     title_start_button.place(x=400, y=700)


#     title_title_label.pack()
#     title_press_label.pack()
#     title_start_button.pack()
# -----------------------------------------------------------------------------------------------------

    # root.mainloop()

# # -----------------------------------------------------------------------------------------------------
# elif (status == "Question"):
#     # 何問目か表示
#     question_number_label = tk.Label(root, text="第"+str(question_count)+"問", font=("ロンド B スクエア", 28))
#     question_number_label.place(x = 470, y = 120)

#     # 問題文表示
#     question_question_label = tk.Label(root, text=q[question_count], font=("ロンド B スクエア", 28))
#     question_question_label.place(x = 250, y = 220)

#     # 選択肢表示
#     question_a1_label = tk.Label(root, text=a[question_count], font=("ロンド B スクエア", 28))
#     question_a1_label.place(x = 250, y = 320)

#     question_a2_label = tk.Label(root, text=a_fake_1[question_count], font=("ロンド B スクエア", 28))
#     question_a2_label.place(x = 650, y = 320)

#     question_a2_label = tk.Label(root, text=a_fake_2[question_count], font=("ロンド B スクエア", 28))
#     question_a2_label.place(x = 250, y = 420)

#     question_a2_label = tk.Label(root, text=a_fake_3[question_count], font=("ロンド B スクエア", 28))
#     question_a2_label.place(x = 650, y = 420)


#     # 入力フォーム表示
#     question_answer_box = tk.Entry(width=20, font=("ロンド B スクエア", 28))
#     question_answer_box.place(x=320, y=650)

#     # 回答ボタン表示
#     question_answer_button = tk.Button(root, text="回答", font=("ロンド B スクエア", 28), command=QuizAnswer)
#     question_answer_button.place(x=700, y=635)
    
# # -----------------------------------------------------------------------------------------------------
# elif (status == "Answer"):

#     # 正答表示
#     answer_correct_label = tk.Label(root, text=a[question_count], font=("ロンド B スクエア", 28))
#     answer_correct_label.place(x = 250, y = 320)

#     if (status == "Answer"):
#         answer_result = "正解！"
#         correct_count += 1
#     else:
#         answer_result = "不正解！"
#         incorrect_count += 1

#     answer_result_label = tk.Label(root, text=answer_result, font=("ロンド B スクエア", 28))
#     answer_result_label.place(x = 450, y = 120)

#     question_count += 1

#     # 次へボタン表示
#     answer_next_button = tk.Button(root, text="次へ", font=("ロンド B スクエア", 28), command=AnswerNext)
#     answer_next_button.place(x=700, y=635)



# # -----------------------------------------------------------------------------------------------------
# elif (status == "Result"):
#     print("a")
# # -----------------------------------------------------------------------------------------------------
# elif (status == "NameInput"):
#     # 名前入力画面
#     # 名前入力を促すメッセージ表示
#     name_input_message_label = tk.Label(root, text="名前を入力してね", font=("ロンド B スクエア", 28))
#     name_input_message_label.place(x = 350, y = 220)

#     # 名前入力ボックス表示
#     name_input_box = tk.Entry(width=20, font=("ロンド B スクエア", 28))
#     name_input_box.place(x=320, y=300)

#     # 決定ボタン表示
#     name_input_button = tk.Button(root, text="決定", font=("ロンド B スクエア", 28), command=NameInput)
#     name_input_button.place(x=700, y=288)


# root.mainloop()



# やりたいことメモ
# tkinterでウィンドウ化
# exe化
# 表記ゆれ回答を許容する方法