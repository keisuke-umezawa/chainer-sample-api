import io
import numpy as np
import responder

from PIL import Image

from services import PredictionService


api = responder.API(
    cors=True,
    allowed_hosts=["*"],
    cors_params={
        "allow_origins": "*",
        "allow_methods": "*",
        "allow_headers": "*",
    },
)


def preprocess_image(image_binary: bytes) -> np.ndarray:
    """Load and preprocess an image file for the model """
    image = Image.open(io.BytesIO(image_binary))
    image = image.convert("L")
    image = image.resize((28, 28))
    image = np.asarray(image, dtype=np.float32)
    return image.flatten()


@api.route("/")
async def index(request, response):
    """Index page. """
    if request.method == "get":
        # HTML page with file form
        response.html = """
<html>
  <body>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit" value="submit">
    </form>
  </body>
</html>
"""

    elif request.method == "post":
        data = await request.media(format="files")
        x = preprocess_image(data["file"]["content"])
        prediction = PredictionService.predict(x)
        response.html = "<html><body>{}</body></html>".format(prediction)


if __name__ == "__main__":
    api.run(address="0.0.0.0", port=8080)
