import cv2

class Note_book():
    def __init__(self, id, pre_id, name, gender, address):
        self.id = id
        self.pre_id = pre_id
        self.name = name
        self.gender = gender
        self.address = address

    def __str__(self) -> str:
        return f'{self.id} - {self.pre_id} - {self.name} - {self.gender} - {self.address}'


def check_info_and_update(info):
    for object in note_book_list:
        if object.id == info[0]:
            print('Thong tin da co trong he thong!!!')
    else:
        note_book_list.append(Note_book(info[0], info[1], info[2], info[3], info[4]))


if __name__ == '__main__':
    img = cv2.imread('D:/frame.png')
    detector = cv2.QRCodeDetector()
    data, cordinate, _ = detector.detect(img)
    info = data.split('|')
    note_book_list = []
    check_info_and_update(info)