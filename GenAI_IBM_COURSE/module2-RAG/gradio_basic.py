import gradio as gr


def greet(name, intensity):
    return f"Hello, {name}. {int(intensity)}"


ui = gr.Interface(
    fn=greet,
    inputs=[
        gr.Textbox(),
        gr.Dropdown(
            choices=[1, 2, 3, 4, 5],
        ),
    ],
    outputs=["text"],
)

ui.launch(server_name="127.0.0.1", server_port=2000, pwa=True)
