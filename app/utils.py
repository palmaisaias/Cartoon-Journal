# from openai import OpenAI
# import os

# def create_image_variation(api_key, image_path, model="dall-e-2", n=1, size="1024x1024"):
#     client = OpenAI(api_key=api_key)
    
#     with open(image_path, "rb") as image_file:
#         response = client.images.edit(
#             model=model,
#             image=image_file,
#             mask=open(mask_path, 'rb'),
#             prompt='Transform this image into a vibrant, high-quality Pixar-style cartoon. Emphasize expressive, large eyes with detailed reflections, smooth and slightly exaggerated facial features, and soft, rounded shapes. Ensure bright, vivid colors and a high level of detail in the shading and textures to capture the whimsical, heartwarming essence of Pixar characters. Include a slight glossy finish on surfaces to mimic the polished look of Pixar animations. The overall style should be friendly, engaging, and full of life, suitable for an animated movie setting.',
#             n=n,
#             size=size
#         )
    
#     return response.data[0].url

# # Example usage:
# api_key = 'YOUR API KEY HERE'
# image_path = os.path.join('app', 'static', 'images', '2_image.png')
# mask_path = os.path.join('app', 'static', 'images', 'mask.png')

from openai import OpenAI

def create_image_variation(api_key, model="dall-e-3", n=1, size="1024x1024"):
    client = OpenAI(api_key=api_key)
    

    response = client.images.generate(
        model=model,
        prompt="In the transformed Pixar-style cartoon, the scene captures two people sitting in a room with a bright window in the background. The man in the foreground is depicted with large, expressive eyes that convey a sense of calm and friendliness, with smooth and slightly exaggerated facial features, including a rounded face, a gentle smile, and detailed hair. He holds up a peace sign with his fingers, which are slightly exaggerated in size to add a playful feel. The woman in the background is depicted with a friendly expression, large eyes, and slightly exaggerated facial features, including a rounded face and a warm smile. Her hair is rendered with soft, flowing strands and a slight gloss. Both characters wear bright, colorful clothing with intricate textures that match their personalities. The colors are vibrant, and the lighting is warm and inviting, casting a soft glow that adds depth and a sense of three-dimensionality to the scene. The background features a bright window with whimsical, softly shaded curtains in a rich, vibrant color, enhancing the cozy atmosphere. Props like the wooden chairs are rendered with smooth textures and attention to detail, adding richness to the scene. The overall scene captures a moment of relaxation and friendliness, with a warm, inviting atmosphere that suggests a story waiting to unfold. The combination of smooth textures, bright colors, and whimsical details paints a vivid picture of a Pixar-style cartoon, bringing out the charm, warmth, and storytelling magic characteristic of Pixar animations.",
        n=n,
        quality="standard",
        size=size
    )
    
    return response.data[0].url

# Example usage:
api_key = "sk-proj-dTQQZkaoTFRiAbW9txo9T3BlbkFJRIl6Ybrj9drGL4sxnBex"

