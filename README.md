# Noor - Offline AI Tutor
=======================

An open-source offline AI tutor built to help Afghan girls continue their education. Noor runs entirely locally on a Raspberry Pi 5, using Gemma for natural conversation and guidance without requiring internet access.

Overview
--------

Noor processes speech input in Farsi, generates contextual responses using a fine-tuned Gemma 2B model, and responds via speech output. The entire pipeline runs offline, making it accessible in areas with limited connectivity.

Components
----------

-   Speech Input: Google Speech Recognition
-   Language Model: Fine-tuned Gemma 2B (via Ollama)
-   Speech Output: Custom Coqui TTS model for Farsi
-   Hardware: Raspberry Pi 5

Setup Requirements
------------------

-   Raspberry Pi 5
-   USB microphone
-   Speaker (via USB audio adapter)


# Example question and response

Input
------------------

اولین پروسه برای اینکه اولین پروسه برای اپلای کردن در آمریکا چیست. به زبان فارسی جواب دهید


Response 
------------------

اولین قدم برای درخواست در کالج‌های آمریکا، انتخاب کالج است.

برای انتخاب کالج مناسب، باید به موارد زیر توجه کنید:

رشته تحصیلی: چه رشته‌ای را می‌خواهید تحصیل کنید؟

موقعیت: در کدام شهر یا استان زندگی می‌کنید؟

محدودیت‌های مالی: چه بودجه‌ای برای تحصیل دارید؟

امکانات: چه امکاناتی در کالج مورد نظر وجود دارد؟ (مثلاً: امکانات ورزشی، فرهنگی، و ... )

بعد از انتخاب کالج، مراحل درخواست شامل موارد زیر است:

اطلاعات شخصی: اطلاعات شخصی خودتان (نام، تاریخ تولد، آدرس، تلفن، ایمیل) را در فرم درخواست وارد کنید.

اطلاعات تحصیلی: اطلاعات مربوط به تحصیلات قبلی خود (مدرک تحصیلی، GPA، و ...) را وارد کنید.

اطلاعات مربوط به برنامه تحصیلی: اطلاعات مربوط به برنامه تحصیلی مورد نظر خود را وارد کنید (مثلاً: رشته تحصیلی، مدت زمان تحصیل، و ...)

اطلاعات مربوط به کار و فعالیت‌های extracurricular: اطلاعات مربوط به فعالیت‌های extracurricular خود را وارد کنید (مثلاً: فعالیت‌های ورزشی، فرهنگ، و ...)

اطلاعات مربوط به توصیه‌نامه: اطلاعات مربوط به توصیه‌نامه از معلم، دانشگاه، یا کارفرمای خود را وارد کنید.

اطلاعات مربوط به زبان انگلیسی: اطلاعات مربوط به مهارت زبان انگلیسی خود را وارد کنید.

اطلاعات مربوط به درخواست مالی: اطلاعات مربوط به درخواست مالی خود را وارد کنید (مثلاً: بودجه، و ...)

نکته: هر کالج، مراحل درخواست خود را دارد. برای اطلاعات دقیق‌تر، به وبسایت کالج مورد نظر مراجعه کنید.

# How to Run Locally
Speech processing pipeline for Noor offline AI tutor. Handles speech-to-text conversion in Farsi and text-to-speech synthesis using local models.

Setup
-----

bash

Copy

`pip install -r requirements.txt
sudo apt-get install ffmpeg`

Components
----------

### Speech to Text (`speech2text.py`)

Converts audio input to text using Google Speech Recognition with Farsi (fa-IR) language support. Handles multiple audio formats by converting to WAV using ffmpeg.

Usage:

bash

Copy

`python speech2text.py input_audio.mp3`

### Text to Speech (`tts.py`)

Synthesizes Farsi text to speech using a local Piper model. Audio is played directly through system audio.

Usage:

bash

Copy

`python tts.py`


# Fine-tuning
The project includes a training pipeline that can be run in Google Colab or any environment with a suitable GPU.

## Prerequisites

- Python 3.10 or later

- CUDA-capable GPU with at least 16GB VRAM

- Google Colab (recommended) or local environment with sufficient computational resources

- Hugging Face account with authentication token

## Installation

1\. Clone this repository:

```bash

git clone [your-repository-url]

cd [repository-name]

```

2\. Install the required packages:

```bash
cd fine-tuning
pip install -r requirements.txt

```

3\. Set up your Hugging Face credentials:

   - Create an account on [Hugging Face](https://huggingface.co)

   - Generate an access token from your [settings page](https://huggingface.co/settings/tokens)

   - Have it ready for the notebook authentication step

## Dataset Preparation

The training process expects a CSV file with the following columns:

- `text_input`: The input text/prompt

- `output`: The desired output/response

Ensure your CSV file follows this format before starting the training process.

## Training Process

1\. Open the Jupyter notebook `gemma_training.ipynb` in Google Colab or your local environment.

2\. Follow these steps in the notebook:

   - Install required dependencies

   - Authenticate with Hugging Face

   - Load the Gemma 2B model

   - Prepare your dataset

   - Configure and run the training process

   - Save the fine-tuned model

## Important Parameters

The training script includes several key parameters that you can adjust:

```python

training_args = TrainingArguments(

    per_device_train_batch_size=1,

    gradient_accumulation_steps=4,

    warmup_steps=2,

    max_steps=10,

    learning_rate=2e-4,

    fp16=True,

    logging_steps=1,

    output_dir="outputs",

    optim="paged_adamw_8bit"

)

```

LoRA configuration:

```python

lora_config = LoraConfig(

    r=8,

    target_modules=[

        "q_proj", "o_proj", "k_proj", "v_proj",

        "gate_proj", "up_proj", "down_proj"

    ],

    task_type="CAUSAL_LM"

)

```

## Saving and Loading the Model

The fine-tuned model will be saved to the specified output directory. If using Google Colab, you can save it to your Google Drive:

```python

trainer.save_model("/content/drive/MyDrive/gemma_ft_saved")

```


*Note: This is an active project in development. We're working to optimize hardware requirements and expand educational capabilities.*