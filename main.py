import Seam
import cv2
import numpy as np
import FindObject as fo


def main():
    path_list = []

    img_name = input('Image name: ')
    original = cv2.imread(img_name)
    Img = original

    print('Loading photo..')
    print('Original shape: ', original.shape)
    print('Press left mouse and choose area to cut')
    print('Press c key to start cuting image')
    # Nhấn và giữ chuột trái để vẽ hình chữ nhật, sau khi nhả chuột thì nhấn phím c để tiếp tục chương trình
    points = fo.user_select_object(Img)
    top = points[0][1]
    bottom = points[1][1]
    left = points[0][0]
    right = points[1][0]


    print('Cutting Image..')
    cv2.imshow('Original image', original)
    cv2.waitKey(3)
    i = 1
    while left <= right:
        print(i)
        print('Left = ', left)
        print('Right = ',right)

        # Bước 1: Chuyển sang ảnh mức xám
        greyImg = Seam.rgbToGrey(Img)
        

        # Bước 2: Tìm cạnh của các đối tượng bằng lọc Sobel
        edgeImg = Seam.getEdge(greyImg)
        
        # Gán lại giá trị cho vùng cần xóa
        edgeImg = fo.fill_area(edgeImg,top,bottom,left,right)
        cv2.imshow("fill",edgeImg)
        
        # Bước 3: Quy hoạch động, tìm ma trận chi trí nhằm giúp lưu lại hướng đi của seam
        cost = Seam.findCostArr(edgeImg)
        
        # Bước 4: Tìm đường seam nhỏ nhất trên E
        # theo chiều từ trên xuống dưới
        path = Seam.findSeam(cost)

        # Bước 5: Vẽ Seam lên ảnh
        Seam.drawSeam(Img,path)
        cv2.imshow('crop', Img)

        # Bước 6: "chặt" đường seam trên ảnh mức xám
        Img = Seam.removeSeam(Img,path)
        
        cv2.waitKey(3)

        i += 1
        right -= 1


    cv2.imshow('crop', Img)

    name_list = img_name.split('.')
    new_name = name_list[0] + '_remove'+ '.' + name_list[1]

    cv2.imwrite(new_name,Img)
    print('Save new image')

    cv2.destroyAllWindows()
    print('Done !!!')
    return 0


#Run 
main()