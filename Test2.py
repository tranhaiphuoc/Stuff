import cv2

def check_duplicate_and_update_info(info):
    f = open('note_book.txt', 'a+')
    f.seek(0)
    for line in f:
        line = line.rstrip()
        if info == line:
            print('Thong tin da co trong he thong!!!')
            f.close()
            break
    else:
        f.write(info)
        f.write('\n')
        f.close()

if __name__ == '__main__':
    img = cv2.imread('D:/frame.png')
    detector = cv2.QRCodeDetector()
    data, cordinate, _ = detector.detectAndDecode(img)
    info = data.replace('|', ' - ')
    check_duplicate_and_update_info(info)