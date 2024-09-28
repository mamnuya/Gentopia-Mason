from typing import AnyStr
from googlesearch import search
from gentopia.tools.basetool import *

from PIL import Image
import requests
from io import BytesIO

class ImageBlackAndWhiteArgs(BaseModel):
    url: str = Field(..., description="a url to an image")


class ImageBlackAndWhite(BaseTool):
    """Tool that adds the capability to show images."""

    name = "image_black_and_white"
    description = ("A tool to show images in black and white."
                   "Input should be an image url.")

    args_schema: Optional[Type[BaseModel]] = ImageBlackAndWhiteArgs

    def _run(self, url: AnyStr) -> str:
        response = requests.get(url)
        if response.status_code != 200:
                return "Please check the image URL."
            
        image_data = BytesIO(response.content)
        im = Image.open(image_data)
        im = im.convert('1')
        im.show()
        return "Showed black and white image"

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError


if __name__ == "__main__":
    ans = ImageBlackAndWhite()._run("Attention for transformer")
    print(ans)