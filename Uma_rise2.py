# ウマ娘全自動リセマラプログラム
# ※Blue Stuck4を使用
# python Uma_rise.py
import pyautogui
from time import sleep
import requests
import os
import pyautogui
import cv2
import glob
import os
import csv
import random
import pyperclip
import pyautogui
import sys
#######################################################################
#ディレクトリの存在チェック、及び存在しない場合作成
SAMPLE_DIR = "./スクショ保存"
if not os.path.exists(SAMPLE_DIR):
   # ディレクトリが存在しない場合、ディレクトリを作成する
   os.makedirs(SAMPLE_DIR)
#######################################################################
# 画像認識
# scr1:判定先、moto1:判定元
def Gazo_ninsk(scr1,moto1):
   def Push_Stamp(num):
       if 0.99 < num:
           return 1
       else:
           return 0
   
   files =glob.glob(scr1) #検索画像保管フォルダパスを指定
   template = cv2.imread(moto1)
   wrcsv = []
   num = 0
   for fname in files:
       # 検索対象画像の読み込み
       image = cv2.imread(fname)
       # 画像マッチング処理
       result = cv2.matchTemplate(image, template, cv2.TM_CCORR_NORMED)
       # 最も類似度が高い位置を取得する。
       minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
       # 類似度から、判定結果を求める（上で設定した式を使用）
       Judg = Push_Stamp(maxVal)
   return Judg
#######################################################################
def Gazo_screen():
   #全画面スクショ
   screenshot = pyautogui.screenshot(region = (0, 50, 550, 975))
   screenshot.save('screen.PNG')
#######################################################################
#画像判定 xy:座標、moto1:判定元
#画像が見えるまで、xy座標をクリックし続ける
def Gazo_hantei(x_1,y_1,moto1):
   for num in range(60):
       pyautogui.click(x_1,y_1)
       #スクリーンショット
       sleep(0.5)
       Gazo_screen()
       Judg = Gazo_ninsk('screen.PNG',moto1)
       if Judg == 1:
           break
#######################################################################
#######################################################################
#画像判定 xy:座標、moto1:判定元
#画像が存在する場合、xy座標をクリックする
def Gazo_click(x_1,y_1,moto1):
   Judg = 0
   for num in range(30):
       #スクリーンショット
       sleep(1)
       Gazo_screen()
       Judg = Gazo_ninsk('screen.PNG',moto1)
       if Judg == 1:
           pyautogui.click(x_1,y_1)
           break
   if Judg == 0:
       #new_down_chk()
       #update_chk()
       Fleez_chk()
       riset()
#######################################################################
# 強制終了
def riset():
   sleep(4)
	# 閉じる
   pyautogui.click(294,9)
   sleep(2)
   pyautogui.click(1107,20)
   sleep(2)
	# ウマ娘起動
   pyautogui.click(201,197)
   sleep(2)
   # ウマ娘起動
   pyautogui.click(1797,21)
   sleep(2)
   test()
#######################################################################
def Fleez_chk():
   Gazo_screen()
   Judg = Gazo_ninsk('screen.PNG','title.PNG')
   if Judg == 1:
	    # 閉じる
       pyautogui.click(294,9)
       sleep(2)
       pyautogui.click(1107,20)
       sleep(2)
	    # ウマ娘起動
       pyautogui.click(201,197)
       sleep(2)
       # ウマ娘起動
       pyautogui.click(1797,21)
       sleep(2)
       Gazo_screen()
#######################################################################
#アプリ更新確認
def update_chk():
   Gazo_screen()
   sleep(2)
   Judg = Gazo_ninsk('screen.PNG','app_update.PNG')
   if Judg == 1:
       #ストアへをクリックする
       sleep(2)
       pyautogui.click(273,683)
       Gazo_screen()
       sleep(2)
       Judg = Gazo_ninsk('screen.PNG','kousin.PNG')
       if Judg == 1:
           sleep(2)
           pyautogui.click(402,243)
           sleep(300)
           Judg = Gazo_ninsk('screen.PNG','hiraku.PNG')
           if Judg == 1:
               riset()
#######################################################################
# 指定した画像が見えるまで待機する
def chk_sleep(gazo_moto):
   while True:
       Gazo_screen()
       sleep(1)
       Judg = Gazo_ninsk('screen.PNG',gazo_moto)
       if Judg == 1:
           break
#######################################################################
#追加データのダウンロードがある場合、待機する
def new_down_chk():
   pyautogui.click(408,690)
   Gazo_screen()
   sleep(2)
   Judg = Gazo_ninsk('screen.PNG','data_dawn.PNG')
   print(Judg)
   if Judg == 1:
       print("２追加データのダウンロードがある場合の処理")
       #追加データをダウンロードしますをクリック
       sleep(2)
       Gazo_click(408,690,'OK.PNG')
       sleep(2)
       Gazo_click(170,689,'atode.PNG')
       sleep(2)
       Gazo_click(408,690,'OK.PNG')
       chk_sleep('menu.PNG')
       riset()
#######################################################################
def gatya_renda(str1):
   x = 513
   y = 981
   Gazo_hantei(x, y,'mouikkai.PNG')
   for num in range(12):
       sleep(0.5)
	    #1枚目
       screenshot = pyautogui.screenshot(region = (50, 141, 120, 150))
       screenshot.save('scsho1.png')
	    #2枚目
       screenshot = pyautogui.screenshot(region = (214, 140, 120, 150))
       screenshot.save('scsho2.png')
       #3枚目
       screenshot = pyautogui.screenshot(region = (382, 139, 120, 150))
       screenshot.save('scsho3.png')
       #4枚目
       screenshot = pyautogui.screenshot(region = (130, 324, 120, 150))
       screenshot.save('scsho4.png')
       #5枚目
       screenshot = pyautogui.screenshot(region = (298, 322, 120, 150))
       screenshot.save('scsho5.png')
       #6枚目
       screenshot = pyautogui.screenshot(region = (51, 512, 120, 150))
       screenshot.save('scsho6.png')
       #7枚目
       screenshot = pyautogui.screenshot(region = (216, 512, 120, 150))
       screenshot.save('scsho7.png')
       #8枚目
       screenshot = pyautogui.screenshot(region = (382, 510, 120, 150))
       screenshot.save('scsho8.png')
       #9枚目
       screenshot = pyautogui.screenshot(region = (132, 702, 120, 150))
       screenshot.save('scsho9.png')
       #10枚目
       screenshot = pyautogui.screenshot(region = (298, 700, 120, 150))
       screenshot.save('scsho10.png')
       def Push_Stamp(num):
           if 0.99 < num:
               return 1
           else:
               return 0
       
       files =glob.glob("scsho*.PNG") #検索画像保管フォルダパスを指定
       template = cv2.imread('SSR.PNG')
       wrcsv = []
       num = 0
       for fname in files:
           # 検索対象画像の読み込み
           image = cv2.imread(fname)
           # 画像マッチング処理
           result = cv2.matchTemplate(image, template, cv2.TM_CCORR_NORMED)
           # 最も類似度が高い位置を取得する。
           minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
           # 類似度から、判定結果を求める（上で設定した式を使用）
           Judg = Push_Stamp(maxVal)
           num += Judg
       #判定
       if str1 < num :
           str1 = num
   return str1
#######################################################################
def test():
   #メニューボタンクリック
   x = 514
   y = 991
   Gazo_click(x,y,'menu.PNG')
   Fleez_chk()
   # ユーザーデータ削除クリック
   x = 223
   y = 815
   Gazo_click(x,y,'user_data_del.PNG')
   # ユーザーデータ削除クリック
   x = 388
   y = 686
   Gazo_click(x,y,'user_data_del2.PNG')
   # ユーザーデータ削除クリック
   x = 388
   y = 686
   Gazo_click(x,y,'user_data_del2.PNG')
   # 閉じるクリック
   x = 280
   y = 685
   Gazo_click(x,y,'toziru.PNG')
   #画面クリック-同意するが見えるまで
   x = 280
   y = 685
   Gazo_hantei(x,y,'doui.PNG')
   # 同意するクリック
   x = 401
   y = 957
   Gazo_click(x,y,'doui.PNG')
   # 同意するクリック2
   x = 401
   y = 957
   Gazo_click(x,y,'doui.PNG')
   # キャンセルをクリック
   x = 175
   y = 695
   Gazo_click(x,y,'cancel.PNG')
   # 後でするをクリック
   x = 175
   y = 695
   Gazo_click(x,y,'atode.PNG')
   # スキップするをクリック
   x = 381
   y = 686
   Gazo_click(x,y,'skip.PNG')
   # トレーナー名クリック
   x = 304
   y = 486
   Gazo_click(x,y,'trainer_name.PNG')
   sleep(1)
   # トレーナー登録　トレーナー名入力
	# pyautogui.write('いくずき')
   pyautogui.write('gita-', interval=0.25)
   sleep(2)
   pyautogui.click(287, 685)
   sleep(2)
	# トレーナー登録　登録する
   Gazo_hantei(287, 685,'OK.PNG')
   sleep(1)
   # OKクリック
   x = 403
   y = 683
   Gazo_click(x,y,'OK.PNG')
   #閉じるが見えるまで右下クリック
   x = 509
   y = 982
   Gazo_hantei(x,y,'toziru.PNG')
   
   sleep(2)
   # 閉じるクリック
   x = 283
   y = 949
   Gazo_click(x,y,'toziru.PNG')
   sleep(2)
   # 閉じるクリック
   x = 282
   y = 682
   Gazo_click(x,y,'toziru.PNG')
   sleep(3)
   # 閉じるクリック
   x = 283
   y = 949
   Gazo_click(x,y,'toziru.PNG')
   sleep(2)
	# プレゼントクリック
   pyautogui.click(509,747)
   sleep(2)
   # 一括受け取りクリック
   x = 402
   y = 955
   Gazo_click(x,y,'ikkatu.PNG')
   # 閉じるクリック
   x = 281
   y = 960
   Gazo_click(x,y,'toziru.PNG')
   # 閉じるクリック
   x = 160
   y = 955
   Gazo_click(x,y,'toziru.PNG')
   sleep(1)
	# ガチャクリック
   pyautogui.click(507,983)
   sleep(1)
   # 左項目クリック
   x = 34
   y = 647
   Gazo_hantei(x,y,'sup_gatya.PNG')
   sleep(1)
   # 10連ガチャクリック
   x = 451
   y = 838
   Gazo_click(x,y,'10ren2.PNG')
   sleep(1)
   # ガチャを引くクリック
   x = 404
   y = 687
   Gazo_click(x,y,'gatyahiku.PNG')
   sleep(1)
   #チェック変数
   chk1 = 0
   chk2 = 0
   chk3 = 0
   chk4 = 0
   chk5 = 0
   chk6 = 0
   chk1 = gatya_renda(chk1)
   sleep(1)
   # もう1回引く
   Gazo_click(391,969,'mouikkai.PNG')
   sleep(1)
	# ガチャを引く！
   Gazo_click(406,683,'gatyahiku.PNG')
   chk2 = gatya_renda(chk2)
   sleep(1)
   # もう1回引く
   Gazo_click(391,969,'mouikkai.PNG')
   sleep(1)
	# ガチャを引く！
   Gazo_click(406,683,'gatyahiku.PNG')
   chk3 = gatya_renda(chk3)
   sleep(1)
   # もう1回引く
   Gazo_click(391,969,'mouikkai.PNG')
   sleep(1)
	# ガチャを引く！
   Gazo_click(406,683,'gatyahiku.PNG')
   chk4 = gatya_renda(chk4)
   sleep(1)
   # もう1回引く
   Gazo_click(391,969,'mouikkai.PNG')
   sleep(1)
	# ガチャを引く！
   Gazo_click(406,683,'gatyahiku.PNG')
   chk5 = gatya_renda(chk5)
   
   sleep(1)
   # もう1回引く
   Gazo_click(391,969,'mouikkai.PNG')
   sleep(1)
	# ガチャを引く！
   Gazo_click(406,683,'gatyahiku.PNG')
   chk6 = gatya_renda(chk6)
   num = chk1 + chk2 + chk3 + chk4 + chk5 + chk6
   
   if num < 4:
       line_notify_token = '発行したトークン'
       line_notify_api = 'https://notify-api.line.me/api/notify'
       LIME_MESS = f'リセマラ結果:SSR数:{num}'
       payload = {'message': LIME_MESS}
       headers = {'Authorization': 'Bearer ' + line_notify_token}  # 発行したトークン
       line_notify = requests.post(line_notify_api, data=payload, headers=headers)
	    # 閉じる
       pyautogui.click(294,9)
       sleep(2)
       pyautogui.click(1107,20)
       sleep(2)
	    # ウマ娘起動
       pyautogui.click(201,197)
       sleep(2)
       # ウマ娘起動
       pyautogui.click(1797,21)
       sleep(2)
       test()
##################################################################
   sleep(10)
	# 戻る
   x=158
   y=972
   Gazo_click(x,y,'modoru.PNG')
   
   sleep(10)
	# 強化編成クリック
   Gazo_click(55,994,'kyouka.PNG')
   sleep(2)
	# サポートカードクリック
   Gazo_click(395,681,'sup.PNG')
   sleep(2)
	# サポートカード一覧クリック
   Gazo_click(181,800,'sup_itiran.PNG')
   sleep(2)
##################################################################
   rand = random.random()
   screenshot = pyautogui.screenshot(region = (0, 50, 550, 975))
   screenshot.save('結果.PNG')
   screenshot.save(f'./スクショ保存/{rand}サポートカードリスト.PNG')
   line_notify_token = '発行したトークン'
   line_notify_api = 'https://notify-api.line.me/api/notify'
   LIME_MESS = "リセマラ結果"
   headers = {'Authorization': 'Bearer ' + line_notify_token}  # 発行したトークン
   message = f'リセマラ結果:SSR数:{num}'
   image = '結果.png'  # png or jpg
   payload = {'message': message}
   files = {'imageFile': open(image, 'rb')}
   r = requests.post(line_notify_api, headers=headers, params=payload, files=files,)
   sleep(5)
   #ホームクリック
   Gazo_click(283,980,'home.PNG')
   sleep(5)
   #メニュークリック
   Gazo_click(514,96,'menu2.PNG')
   sleep(2)
   #データ連携クリック
   pyautogui.click(410,711)
   sleep(3)
   #データ連携クリック2
   pyautogui.click(399,687)
   sleep(3)
   #設定クリック
   pyautogui.click(465,607)
   sleep(3)
   #設定クリック２
   pyautogui.click(400,684)
   sleep(3)
   #連携パスワードクリック
   pyautogui.click(287,463)
   sleep(3)
   # パスワード入力
   # クリップボードへコピー
   pyperclip.copy('ISBN9781300a')
   sleep(3)
   pyautogui.keyDown('ctrl')
   pyautogui.press('v')
   pyautogui.keyUp('ctrl')
   sleep(3)
   #連携パスワードクリック2
   pyautogui.click(294,566)
   sleep(3)
   #連携パスワードクリック2
   pyautogui.click(294,566)
   # パスワード入力
   sleep(3)
   pyautogui.keyDown('ctrl')
   pyautogui.press('v')
   pyautogui.keyUp('ctrl')
   sleep(3)
   #チェックにクリック
   pyautogui.click(138,686)
   sleep(3)
   #チェックにクリック
   pyautogui.click(138,686)
   sleep(3)
   #OKクリック
   pyautogui.click(403,745)
   sleep(3)
   screenshot = pyautogui.screenshot(region = (0, 50, 550, 975))
   screenshot.save('引継ぎトレーナーID.PNG')
   screenshot.save(f'./スクショ保存/{rand}引継ぎトレーナーID.PNG')
   line_notify_token = '発行したトークン'
   line_notify_api = 'https://notify-api.line.me/api/notify'
   LIME_MESS = "SSR4以上、引継ぎスクリーンショット"
   headers = {'Authorization': 'Bearer ' + line_notify_token}  # 発行したトークン
   message = f'リセマラ結果:SSR数:{num}'
   image = '引継ぎトレーナーID.PNG'  # png or jpg
   payload = {'message': message}
   files = {'imageFile': open(image, 'rb')}
   r = requests.post(line_notify_api, headers=headers, params=payload, files=files,)
   sleep(3)
	# 閉じる
   pyautogui.click(294,9)
   sleep(2)
   pyautogui.click(1107,20)
   sleep(2)
	# ウマ娘起動
   pyautogui.click(201,197)
   sleep(2)
   # ウマ娘起動
   pyautogui.click(1797,21)
   sleep(2)
   test()
