import cv2
import numpy as np

def convert_gamma(gamma, img):
    gamma_cvt_lut = np.zeros((256,1), dtype=np.uint8)
    for i in range(256):
        gamma_cvt_lut[i][0] = 255*(float(i)/255)**(1.0/gamma)
    return cv2.LUT(img, gamma_cvt_lut)

def convert_equalizeHist(img):
    return cv2.equalizeHist(img)

def convert_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def convert_CLAHE(img):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    return clahe.apply(img)

def convert_grayscale(img):
  return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


print("---start---")

# 動画ファイルを読み込む
input_filename = "./videos/street.mp4"
video = cv2.VideoCapture(input_filename)

# 幅と高さを取得
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (width, height)

# 総フレーム数を取得
frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
# フレームレート(単位はミリ秒)の取得
frame_rate = int(video.get(cv2.CAP_PROP_FPS))

# 保存用
output_filename = "./videos/street-gray.mp4"
fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
writer = cv2.VideoWriter(output_filename, fmt, frame_rate, size, False) # 第５引数はisColorフラグ

for i in range(frame_count):
    ret, frame = video.read()
    ### ここに加工処理などを記述する 
    #frame = create_gamma_img(2, frame)
    frame = convert_grayscale(frame)
    #frame = convert_equalizeHist(frame)
    #frame = convert_CLAHE(frame)

    
    writer.write(frame)

    # 現在読んでいるフレームを描画
    # 処理結果見えなくていいから軽量化したい場合はここをコメントアウト
    # dockerだとrun実行時に、x-winndow? 共有設定が何かしら必要？。要調査
    #cv2.imshow("frame", frame)

    # qを押せば処理を中止できるようにしておく
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"): break


writer.release()
video.release()
cv2.destroyAllWindows()

print("---end---")