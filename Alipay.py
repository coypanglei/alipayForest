import aircv as ac
import os
import cv2

PATH = lambda p: os.path.abspath(p)
path = PATH(os.getcwd() + "/img")
TEMP_FILE = PATH(path + "/alipay.png")
TEMP_FILE_TWO = PATH(path + "/shou.jpg")
TEMP_FILE_THREE = PATH(path + "/crile.jpg")


def matchImg(srcfile, objfile, confidencevalue=0.5):  # imgsrc=原始图像，imgobj=待查找的图片
    imsrc = ac.imread(srcfile)
    imobj = ac.imread(objfile)
    match_result = ac.find_template(imsrc, imobj,
                                    confidencevalue)  # {'confidence': 0.5435812473297119, 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.0)}
    # if match_result is not None:
    #     match_result['shape'] = (imsrc.shape[1], imsrc.shape[0])  # 0为高，1为宽

    return match_result


def draw_circle(img, pos, circle_radius, color, line_width):
    cv2.circle(img, pos, circle_radius, color, line_width)
    cv2.imshow('objDetect', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# if __name__ == '__main__':
#
#     print()
#     imsrc = ac.imread(TEMP_FILE)
#     imnew = ac.imread(TEMP_FILE_THREE)
#     imobj = ac.imread(TEMP_FILE_TWO)
#     print(matchImg(imsrc, imobj, 0.9))
#     pos = matchImg(imsrc, imobj, 0.9)
#     circle_center_pos = pos['rectangle']
#     print(circle_center_pos[0])
#     circle_radius = 50
#     color = (0, 255, 0)
#     line_width = 10
#     cv2.rectangle(imnew, circle_center_pos[0], circle_center_pos[3], color, 10)
#     cv2.imshow('objDetect', imnew)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
