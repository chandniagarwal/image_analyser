import cv2 as cv


def fast_true(img):
    # Initiate FAST object with default values
    fast = cv.FastFeatureDetector_create()
    return fast_analyser(img, fast)


def fast_false(img):
    fast = cv.FastFeatureDetector_create()
    # Disable nonmaxSuppression
    fast.setNonmaxSuppression(0)
    return fast_analyser(img, fast)


def fast_analyser(img, fast):
    kp = fast.detect(img, None)
    img2 = cv.drawKeypoints(img, kp, None, color=(255, 0, 0))
    # Print all default params
    print("Threshold: {}".format(fast.getThreshold()))
    print("nonmaxSuppression:{}".format(fast.getNonmaxSuppression()))
    print("neighborhood: {}".format(fast.getType()))
    print("Total Keypoints with nonmaxSuppression: {}".format(len(kp)))
    cv.imwrite('fast_true.png', img2)
