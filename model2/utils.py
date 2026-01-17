import numpy as np # type: ignore
from tensorflow.keras.applications.mobilenet_v2 import ( # type: ignore
    MobileNetV2,
    preprocess_input,
    decode_predictions
)
from tensorflow.keras.preprocessing import image # type: ignore

model = MobileNetV2(weights='imagenet')

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    decoded = decode_predictions(preds, top=1)[0][0]

    return {
        "class": decoded[1],
        "confidence": float(decoded[2])
    }
