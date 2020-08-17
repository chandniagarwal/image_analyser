import cv2


def orb(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    orb = cv2.ORB_create(nfeatures=1500)
    keypoints_orb, descriptors = orb.detectAndCompute(gray, None)
    return cv2.drawKeypoints(img, keypoints_orb, img)
