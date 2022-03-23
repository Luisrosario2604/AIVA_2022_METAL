from cv2 import cv2
import random
import ImperDetect as ID
 
   
if __name__ == '__main__':

    # Load image
    inputPath = 'dataset/IMAGES/inclusion_1.jpg'
    print('Cargando imagen...')
    img = cv2.imread(inputPath)
    label, location = ID.classify_and_locate(img)

    if label == 0:
        text_label = 'inclusions'
    elif label ==1:
        text_label = 'scratches'
    elif label == 2:
        text_label = 'patches'
    
    print('Etiqueta del defecto: ' + str(label) + " = " + text_label)
    print('Location: ' + str(location))
    
    test_img = cv2.rectangle(img, (location[0], location[1]), (location[2], location[3]), (255,0,0), 2)
    test_img = cv2.putText(test_img, text_label, (25, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2, cv2.LINE_AA)
    
    cv2.imshow('image', test_img)
    cv2.waitKey()