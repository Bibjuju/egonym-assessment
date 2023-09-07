import cv2
import math

FONT_SCALE = 1e-3  # Adjust for larger font size in images
THICKNESS_SCALE = 1e-3  # Adjust for larger thickness in images
TEXT_Y_OFFSET_SCALE = 2e-2  # Adjust for larger Y-offset of text and bounding box


def annotate_image(image, model):
    """
    Perfoms object detections and draw boxes along with labels on the input image.


        Parameters
        ----------
        image : numpy.ndarray
            Image (numpy.ndarray) to be annotated by the model. 
        model : 
            Detection model.
        
        Returns
        -------
        boxes_and_labels:
            list of annotation boxes with associated label and confidence.
    """
    results = model.predict(image)

    boxes_and_labels = list(map(lambda x:  [int(e) for e in x], results[0].boxes.data))
    # Draw the bounding boxes and labels
    for e in boxes_and_labels:
        x1, y1, x2, y2, score, label = e
        label = results[0].names[label]
        height, width, _ = image.shape
        print(x1, y1, x2, y2, score, label)
        cv2.rectangle(image, (int(x1), int(y1)), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image,
                    label,
                    (x1, y1 + int(height * TEXT_Y_OFFSET_SCALE)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=min(width, height) * FONT_SCALE,
                    thickness=math.ceil(min(width, height) * THICKNESS_SCALE),
                    color=(0, 255, 0))
    return boxes_and_labels