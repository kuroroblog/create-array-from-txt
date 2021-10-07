import re

# テキスト情報を配列に格納する変数。
txt_array_list = []
# 文章情報を一時的に格納する変数。
tmp_sentences = []
# 一つ前の段落idxを格納する変数。
front_paragraph_idx = -1
# 一つ前の節idxを格納する変数。
front_theory_idx = -1
# テキストファイルパス
file_path = 'sample.txt'
# 節かどうかを判定するフラグ。節の配列の初期化を行うために利用する。
theory_flag = False

# 参考 : https://note.nkmk.me/python-file-io-open-with/
with open(file_path, 'r') as f:
    for s_line in f:
        # 正規表現を利用して、節にマッチする場合の処理を行う。
        # 正規表現参考 : https://qiita.com/luohao0404/items/7135b2b96f9b0b196bf3
        res = re.match('.+\d.\d 第.+章.+節', s_line)
        if res:
            # 段落から初めて節が読み込まれる場合
            if not theory_flag:
                # 空配列を用意する。
                txt_array_list[front_paragraph_idx].append([])

            # 一度節が読み込まれたら、フラグをTrueにする。
            theory_flag = True

            # 節の情報を格納する。
            txt_array_list[front_paragraph_idx][1].append([s_line.strip()])

            # 改めて節の正規表現マッチが発生した場合、前の説へ文章情報を格納する。
            if not front_theory_idx == -1:
                txt_array_list[front_paragraph_idx][1][front_theory_idx].append(tmp_sentences)

            # 文章情報を空にする。
            tmp_sentences = []
            # 前の節の更新を行う。
            front_theory_idx += 1
            # 後続処理を行わないようにするため、continueを利用する。
            continue

        # 正規表現を利用して、段落にマッチする場合の処理を行う。
        # 正規表現参考 : https://qiita.com/luohao0404/items/7135b2b96f9b0b196bf3
        res = re.match('\d. 第.+章', s_line)
        if res:
            # 段落の情報を格納する。
            txt_array_list.append([s_line.strip()])

            # 節から段落への読み込みの場合、最終文章は節の文章である。節の章へ文章を格納する。
            if theory_flag == True and not front_theory_idx == -1:
                # 前の節へ文章情報を格納する。
                txt_array_list[front_paragraph_idx][1][front_theory_idx].append(tmp_sentences)

            # theory_flagがTrueでない場合のみ、段落へ文章を格納する。
            # 改めて段落の正規表現マッチが発生した場合、前の段落へ文章情報を格納する。
            if not theory_flag == True and not front_paragraph_idx == -1:
                txt_array_list[front_paragraph_idx].append(tmp_sentences)

            # 文章情報を空にする。
            tmp_sentences = []
            # 前の段落の更新を行う。
            front_paragraph_idx += 1
            # 段落が現れる = 節が終わる。を意味するので、リセットを行う。
            front_theory_idx = -1
            # 節のフラグを再度初期化する。
            theory_flag = False
            # 後続処理を行わないようにするため、continueを利用する。
            continue

        # 文章情報を格納する。
        tmp_sentences.append(s_line.strip())

# 最後の節の文章情報を格納するために、以下の処理が行われる。
if theory_flag == True and not front_theory_idx == -1:
    txt_array_list[front_paragraph_idx][1][front_theory_idx].append(tmp_sentences)

# 最後の段落の文章情報を格納するために、以下の処理が行われる。
if not theory_flag == True and not front_paragraph_idx == -1:
    txt_array_list[front_paragraph_idx].append(tmp_sentences)

print(txt_array_list)
