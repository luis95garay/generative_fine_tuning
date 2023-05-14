from typing import Any
import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import PIL
import numpy as np
import matplotlib.pyplot as plt


class PokemonPipeline:
    def __init__(self, 
                 model_base: str="CompVis/stable-diffusion-v1-4",
                 model_trained: str="sd-pokemon-model",
                 device: str="cpu"
                 ) -> None:

        self.model = StableDiffusionPipeline.from_pretrained(model_base, torch_dtype=torch.float16)
        self.model.scheduler = DPMSolverMultistepScheduler.from_config(self.model.scheduler.config)

        self.model.unet.load_attn_procs(model_trained)
        self.model.to(device)

    def __call__(self, prompt: str, scale: np.float16=0.5, num_inference_steps: int=25, guidance_scale: float=7.5) -> PIL.Image:
        return self.model(
            prompt=prompt, 
            num_inference_steps=num_inference_steps, 
            guidance_scale=guidance_scale, 
            cross_attention_kwargs={"scale": scale}
            ).image[0]

if '__main__' == __name__:
    pipe = PokemonPipeline()

    image = pipe(
        "A pokemon with blue eyes.", scale=0.5
    ).images[0]

    plt.imshow(image)
    plt.show()

