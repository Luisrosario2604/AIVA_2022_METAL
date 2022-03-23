import unittest
import ImperDetect as ID

class projectTesting (unittest.TestCase):
    def check_input_image(self):
        '''
            Test input image. 
        '''
        file = 'dataset/IMAGES/inclusion_1.jpg'
        img = cv2.imread(file)
        size = img.shape

        self.assertEqual(size, (200,200))

    
    def check_result_label(self):
        '''
            Test result of system. 
        '''
        file = 'dataset/IMAGES/inclusion_1.jpg'
        img = cv2.imread(file)
        label, _ = ID.classify_and_locate()
        self.assertEqual(?)

    def check_result_location(self):
        '''
            Test result of system. 
        '''
        file = 'dataset/IMAGES/inclusion_1.jpg'
        img = cv2.imread(file)
        _, location = ID.classify_and_locate()
        self.assertEqual(?)
    