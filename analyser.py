from PyInquirer import prompt
import cv2

from algorithms import sift, orb, gabor, fast_true, fast_false

algo_to_function_map = {
    "sift": sift,
    "orb": orb,
    "gabor": gabor,
    "fast_with_nonmax_suppression": fast_true,
    "fast_without_nonmax_suppression": fast_false,
}


def main(image_path, algos):
    img = cv2.imread(image_path)
    cv2.imshow("Original img", img)

    algorithms = list(map(algo_to_function_map.get, algos))  # List of callables

    for algo in algorithms:
        new_image = algo(img)
        cv2.imshow(algo.__name__, new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    questions = [
        {
            "type": "input",
            "name": "img",
            "message": "Image Path",
        },
        {
            "type": "checkbox",
            "name": "algos",
            "message": "Which algorithms do you want to run?",
            "choices": [{"name": key for key in algo_to_function_map.keys()}]
        }
    ]
    answers = prompt(questions)
    image_path = answers["img"]
    algos = answers["algos"]
    main(image_path, algos)
