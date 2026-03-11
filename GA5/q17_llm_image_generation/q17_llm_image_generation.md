# GA5 — Q17: LLM Image Generation — OpenAI API Request

## Problem Summary

VisualCraft is building a system that automatically generates images from text descriptions using OpenAI's Image Generation API.

The task is to construct the **JSON request body** that would be sent to the endpoint:

```
https://api.openai.com/v1/images/generations
```

The JSON must include the required parameters to generate images based on a provided text prompt.

---

## Requirements

The request must satisfy the following conditions:

| Parameter | Value |
|----------|------|
| Model | `gpt-image-1` |
| Image Size | `512x512` |
| Number of Images | `2` |
| Prompt | `"An underwater scene with colorful coral reefs and tropical fish"` |

Only the **JSON body** is required — not headers or the URL.

---

## JSON Request Body

```json
{
  "model": "gpt-image-1",
  "prompt": "An underwater scene with colorful coral reefs and tropical fish",
  "size": "512x512",
  "n": 2
}
```

---

## Explanation of Parameters

### `model`
Specifies the OpenAI image generation model to use.

```
"model": "gpt-image-1"
```

This model generates images directly from text prompts.

---

### `prompt`

The natural language description used to generate the image.

```
"prompt": "An underwater scene with colorful coral reefs and tropical fish"
```

The model interprets this description and synthesizes images that match the scene.

---

### `size`

Defines the output resolution of the generated image.

```
"size": "512x512"
```

This produces square images with dimensions **512 × 512 pixels**.

---

### `n`

Specifies how many images to generate for the prompt.

```
"n": 2
```

This returns **two generated images** in the API response.

---

## Why This JSON Is Valid

This request body satisfies all the requirements because it:

- uses the correct image generation model
- includes the provided prompt
- generates exactly **two images**
- sets the required output resolution
- follows valid JSON formatting with properly quoted keys and values

---

## Final Answer

```json
{
  "model": "gpt-image-1",
  "prompt": "An underwater scene with colorful coral reefs and tropical fish",
  "size": "512x512",
  "n": 2
}
```
