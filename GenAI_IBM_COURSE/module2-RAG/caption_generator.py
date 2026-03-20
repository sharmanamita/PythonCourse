from transformers import BlipProcessor, BlipForConditionalGeneration
import gradio as gr
import os

os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"


processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)


def generate_caption(image):
    inputs = processor(images=image, return_tensors="pt")
    outputs = model.generate(**inputs)
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    return caption


def get_caption(image):
    try:
        caption = generate_caption(image)
        return caption
    except Exception as e:
        print(e)


caption = gr.Interface(
    fn=get_caption,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="Image Captioning with BLIP",
    description="Upload an image to generate a caption.",
)

caption.launch(server_name="127.0.0.1", server_port=2000)
