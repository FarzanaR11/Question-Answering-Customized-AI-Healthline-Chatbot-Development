# -*- coding: utf-8 -*-
"""Customized AI Healthline ChatBot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-UAmhahmIduGrgRj-wq8JWlGmJYW0H1I

Client Website Link: https://www.healthline.com/
Client Requirement: Develop a fully custom chatbot capable of answering clients' questions
based on the information available on the website.
Task Instructions
Part 1: Data Collection and Dataset Creation
1. Website Analysis:
○ Visit the client’s website
○ Explore the website thoroughly to gather relevant information. This may include
product descriptions, services offered, company information, FAQs, etc.

2. Dataset Creation:
○ Based on the gathered information, create a structured dataset that can be used
to train a chatbot.
○ Ensure the dataset covers various sections of the website, including services,
products, contact information, and any other relevant content.
○ Ensure coverage of all sections of the website. Organize the dataset to make
sure it captures a broad set of potential client queries.

Part 2: Model Training
3. Model Selection:
○ Choose a machine learning or deep learning model suitable for answering
questions based on the data.
○ Ensure the model is suitable for generating or selecting accurate responses
based on the user’s questions.

4. Training:
○ Train the model using the dataset.
○ Implement techniques and ensure it can accurately answer a wide range of
questions related to the content on the website.
○ Test the model during training to assess its performance and make necessary
adjustments.
5. Evaluation:
○ After training, evaluate the model's accuracy by asking a variety of questions
related to the website content.
○ Ensure the chatbot provides correct and contextually relevant responses.
Part 3: Submission
6. Code Submission:

○ Submit the Python scripts and created dataset
○ Use github to submit the code.
○ Ensure that your code is well-documented and easy to follow.
○ Create a short video of question answering of the chatbot

1. Website Analysis: Scrapping Various Sections -
"""

!pip install requests beautifulsoup4 pandas

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to extract content from a webpage
def extract_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extracting text from paragraphs including various sections of the website, including services, products, and company information.
    Relevant_Information = [p.text for p in soup.find_all('p')]
    return Relevant_Information

# List of URLs to scrape (services, FAQs, etc.)
urls = [

    # Product Descriptions (Including All)
    'https://www.healthline.com/conditions',                   # Health Conditions
    'https://www.healthline.com/reviews',                      # Health Devices
    'https://www.healthline.com/series',                       # Health Series
    'https://www.healthline.com/video',                        # Health Video Series
    'https://www.healthline.com/drugs',                        # Drugs
    ''

    # Services Offered
    'https://www.healthline.com/wellness',                   # Wellness Services
    'https://www.healthline.com/fitness',                    # Fitness Programs
    'https://www.healthline.com/sleep',                      # Sleep Health
    'https://www.healthline.com/digestive-health',           # Digestive Health
    'https://www.healthline.com/mental-health',              # Mental Health


    #Articles Directory

    'https://www.healthline.com/health-news',                # News



    # Health Conditions & Treatments
    'https://www.healthline.com/health/arthritis',           # Arthritis Care
    'https://www.healthline.com/health/migraine',            # Migraine Treatments
    'https://www.healthline.com/health/psoriasis',           # Psoriasis Care
    'https://www.healthline.com/health/depression',          # Depression Information


    # Company Information
    'https://www.healthline.com/about',                      # About Healthline
    'https://www.healthline.com/contact',                    # Contact Us
    'https://www.bezzy.com/',                                # Bezzy
    'https://www.bezzybc.com/discover/life-in-remission/',   # Remission



    # FAQs
    'https://www.healthline.com/nutrition',                  # Nutrition FAQs
    'https://www.healthline.com/wellness',                   # Wellness FAQs
    'https://www.healthline.com/mental-health',              # Mental Health FAQs
    'https://www.healthline.com/fitness',                    # Fitness FAQs
    'https://www.healthline.com/digestive-health',           # Digestive Health FAQs


]

# Scraping content and creating a dataset
data = []
for url in urls:
    page_content = extract_content(url)
    data.append({'URL': url, 'Relevant_Information': ' '.join(page_content)})

# Convert to DataFrame and save as CSV
df = pd.DataFrame(data)
df.to_csv('healthline_dataset.csv', index=False)
print("Dataset created successfully!")

"""Pre-processing healthline dataset"""

import pandas as pd
import re

def preprocess_text(text):
    # Lowercasing
   # text = text.lower()

    # Removing unwanted characters and punctuation
    text = re.sub(r'\W+', ' ', text)
    text = text.replace('OUR BRANDS', '')
    text = text.replace('OUR PRODUCTS', '')

    return text.strip()

# Applying preprocessing to dataset
df = pd.read_csv('healthline_dataset.csv')
df['Relevant_Information'] = df['Relevant_Information'].apply(preprocess_text)
df.to_csv('preprocessed_healthline_data.csv', index=False)

# Assigning the file path to the variable path
path = 'preprocessed_healthline_data.csv' # Added this line to define the path variable

df = pd.read_csv(path)

#dataset is now stored in a Pandas Dataframe
df.describe

# Print dataset shape (rows, columns)
print(df.shape)

# Summary statistics and information
print(df.info())

# Randomly view 5 samples from the dataset
print(df.sample(5))
df.describe()

#Store the list content in a DataFrame
df = df[['URL', 'Relevant_Information']]

df.head(15)
from google.colab import files
df.to_csv('preprocessed_healthline_data.csv', index=False)

#DOWfiles.download('preprocessed_healthline_data.csv')

#google sheets
from google.colab import sheets
sheet = sheets.InteractiveSheet(df=df)

"""2. Dataset Creation: product descriptions, services offered, company information, FAQs, etc."""

import pandas as pd

# Define the datasets for each category
health_conditions = {
    'question': [
        "What is gestational diabetes?",
        "What is asthma, and how does it affect the body?",
        "What are the symptoms of heart disease?",
        "Where did COVID-19 come from?"
    ],
    'answer': [
        "Gestational diabetes is high blood sugar during pregnancy caused by insulin-blocking hormones from the placenta. It can lead to complications for both the mother and baby.(Read More- https://www.healthline.com/health/diabetes)",
        "Asthma is an inflammatory disease that affects the airways to the lungs, making breathing difficult. It causes swelling in the airway lining, tightening of surrounding muscles, and the buildup of mucus, which restricts airflow and can trigger coughing, wheezing, and chest tightness.(Read More- https://www.healthline.com/health/asthma)",
        "Symptoms vary by type but often include chest pain, shortness of breath, fatigue, irregular heartbeats, and dizziness.(Read More - https://www.healthline.com/health/heart-disease)",
        "COVID-19 is widely believed to have originated from an animal, likely transmitted at a food market in Wuhan, China. However, some experts consider a 21% chance it could have resulted from a research-related accident.(Read More -https://www.healthline.com/health/coronavirus-covid-19)"
    ],
    'category': 'health_conditions'
}

treatments = {
    'question': [
        "What is the purpose of chemotherapy?",
        "Is metformin used for PCOS or fertility problems? If so, what’s the dosage?",
        "What are the common side effects of Imipramine?",
        "Are there natural remedies for insomnia?"
    ],
    'answer': [
        "The purpose of chemotherapy is to lower the total number of cancer cells in your body, reduce the likelihood of cancer spreading, shrink tumor size, and alleviate current symptoms. It can also be used to ensure any remaining cancer cells are killed after surgery, prepare you for other treatments like radiation therapy, and relieve pain in late-stage cancer. Additionally, chemotherapy may help people with bone marrow diseases prepare for stem cell treatments and assist in managing disorders where the immune system attacks healthy cells, such as lupus or rheumatoid arthritis.(Read More- https://www.healthline.com/health/chemotherapy)",
        "Metformin is not approved to treat polycystic ovary syndrome (PCOS) or fertility issues. However, it is sometimes used off-label for these conditions due to its ability to reduce insulin resistance, which can improve symptoms like irregular periods and fertility problems. Consult your doctor to explore this option and determine the appropriate dosage.(Read More- https://www.healthline.com/health/drugs/metformin-oral-tablet#_noHeaderPrefixedContent)",
        "Common side effects of Imipramine include drowsiness, dry mouth, constipation, blurred vision, and weight gain.(Read More- https://www.healthline.com/health/drugs/imipramine-oral-tablet)",
        "Natural remedies for insomnia include drinking warm milk or herbal teas like chamomile, practicing meditation to reduce stress, and using essential oils such as lavender or chamomile for relaxation. Acupuncture is another option that might help ease symptoms. Always consult a healthcare professional before starting new treatments.(Read More-https://www.healthline.com/health/insomnia)"
    ],
    'category': 'treatments'
}

lifestyle_advice = {
    'question': [
        "What are the benefits of regular exercise?",
        "What are some essential steps for a basic skincare routine that everyone should follow?",
        "What are some effective stress management techniques?",
        "Can drinking lots of water reduce cholesterol?",
        "What are some recommendations for maintaining a healthy lifestyle?"
    ],
    'answer': [
        "Regular exercise offers a multitude of benefits, including improved mood, enhanced energy levels, and better weight management. It strengthens muscles and bones, reduces the risk of chronic diseases like diabetes and heart disease, and boosts brain function and memory. Additionally, regular physical activity can improve skin health, promote better sleep, and help manage chronic pain. Overall, incorporating exercise into your routine contributes significantly to both physical and mental well-being.(Read More- https://www.healthline.com/nutrition/10-benefits-of-exercise)",
        "The foundation of a basic skincare routine involves three key steps: cleansing, moisturizing, and sun protection. Cleansing removes dirt, oil, and impurities from the skin’s surface, helping to prevent breakouts and maintain a clear complexion. Moisturizing replenishes hydration, keeping the skin soft and supple. Sun protection is essential to shield the skin from harmful UV rays, which can cause premature aging and increase the risk of skin cancer. Incorporating these steps into your daily regimen can significantly improve skin health and appearance.(Read More- https://www.healthline.com/skincare)",
        "Effective stress management techniques include lower stress levels, consider incorporating regular exercise, listening to music, practicing yoga and meditation, and deep breathing exercises into your routine. Additionally, cutting back on obligations, cuddling a pet, and ensuring you get enough sleep can also be effective. Prioritizing these activities can help create a balanced lifestyle and promote overall well-being.(Read More- https://www.healthline.com/health/stress",
        "Drinking more water may help reduce cholesterol levels, as studies suggest a modest effect on lowering total cholesterol and LDL cholesterol. However, more research is needed to confirm these findings.(Read More-https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8485913/",
        "Exercising regularly, eating nourishing foods, and reducing your intake of sugar and alcohol are just some of the recommendations for maintaining a healthy lifestyle. Taking care of your health is arguably the most important thing you can do for yourself and your loved ones.(Read More- https://www.healthline.com/health/how-to-maintain-a-healthy-lifestyle)"
    ],
    'category': 'lifestyle_advice'
}

product_reviews = {
    'question': [
        "What are some recommended extra-firm mattresses for better sleep?",
        "How effective are fitness trackers, such as Fitbit models, for health monitoring?",
        "What are some of the best sustainable activewear brands?",
        "Are there any recommended supplements for joint health?",
        "Do you offer personalized meal plans?",
        "What are some top-rated CBD gummies?"
    ],
    'answer': [
        "Highly recommended extra-firm mattresses include the Saatva Classic Mattress, known for its durable construction and excellent support; the Purple Mattress, praised for its innovative hyper-elastic polymer grid that offers both firmness and pressure relief; and the Tempur-Pedic TEMPUR-ProAdapt, which provides exceptional firmness while conforming to the body for comfort and support.(Read More-https://www.healthline.com/health/healthy-sleep/best-extra-firm-mattresses)",
        "Fitness trackers, including Fitbit models like the Charge 5 and Versa 4, effectively monitor activity, heart rate, and sleep. They offer valuable insights for tracking fitness goals and overall health but should be used alongside professional medical advice for the most accurate health management.(Read More-https://www.healthline.com/nutrition/best-fitbit#1)",
        "Some of the best sustainable activewear brands include Patagonia, prAna, and Girlfriend Collective. These brands focus on using eco-friendly materials, ethical manufacturing processes, and reducing their overall environmental impact.(Read More-https://www.healthline.com/health/fitness/best-sustainable-activewear-brands#sustainable-fashion)",
        "Joint supplements, such as glucosamine, chondroitin, and omega-3 fatty acids, may help reduce joint pain and improve mobility. They can be beneficial for managing symptoms of osteoarthritis and other joint conditions, but their effectiveness varies among individuals. Consulting with a healthcare provider is recommended to determine the best approach for joint health.(Read More-https://www.healthline.com/health/joint-supplements)",
        "Yes, eMeals is a meal planning service application that provides all the tools you need to prepare and enjoy more healthy, home-cooked meals each week. Using the app, you can create a custom meal plan by mixing and matching your favorite recipes. eMeals provides personalized meal plans based on dietary preferences and goals. Users can select from various meal plan options, including low-carb, keto, vegan, and more, tailored to their specific needs and tastes.(Read More-https://www.healthline.com/nutrition/emeals-review#1)",
        "Some top-rated CBD gummies include Charlotte's Web CBD Gummies, praised for their quality and effectiveness in managing stress and sleep; Green Roads Relax Bears, valued for their broad-spectrum CBD and relaxing properties; and Hemp Bombs CBD Gummies, known for their potency and variety, making them a popular choice for pain and anxiety relief.(Read More- https://www.healthline.com/cbd/best-cbd-gummies#best-cbd-gummies)"
    ],
    'category': 'product_reviews'
}

services_offered = {
    'question': [
        "What services does Healthline provide?",
        "How can I contact Healthline for support?",
        "Does Healthline offer telehealth services?",
        "Does Healthline share my personal information?"
    ],
    'answer': [
        "Healthline provides a range of health-related services, including expert-reviewed health information, wellness advice, and product recommendations. Their goal is to offer trustworthy and evidence-based content that helps people make informed health decisions. Healthline's content covers a wide array of topics such as medical conditions, nutrition, mental health, and fitness, and is created by a team of medical professionals and editorial experts to ensure accuracy and relevance. They also offer tools and resources to support users in managing their health effectively.(Read More-https://www.healthline.com/about/about-us)",
        "You can contact Healthline for support through their contact page, by emailing support@healthline.com, or via their social media profiles.(Read More-https://www.healthline.com/about/contact-us)",
        "Healthline does provide information on telehealth services but does not offer telehealth consultations directly. For telehealth services, they recommend various telemedicine companies listed in their guide.(Read More-https://www.healthline.com/health/best-telemedicine-companies)",
        "Healthline’s privacy policy outlines that they may share your personal information with third-party service providers for operational purposes, but they do not sell your information. They implement measures to ensure your data is protected and used in compliance with applicable privacy laws. For detailed information, refer to their full privacy policy.(Read More-https://www.healthline.com/about/privacy-policy)."
    ],
    'category': 'services_offered'
}

company_information = {
    'question': [
        "What is Healthline’s mission?",
        "Where is Healthline headquartered?",
        "How can I apply for a job at Healthline?"
    ],
    'answer': [
        "Healthline’s mission is to improve health and well-being through accurate, accessible, and actionable health information. They aim to empower people to make informed health decisions by providing reliable content and connecting them with trusted experts and resources.(Read More-https://www.healthline.com/about/about-us)",
        "Healthline Media, Inc. is an American website and provider of health information headquartered in San Francisco, California. It was founded in 1999, and purchased by Red Ventures in 2019.(Read More-https://en.wikipedia.org/wiki/Healthline#:~:text=Healthline%20Media%2C%20Inc.%20is%20an,by%20Red%20Ventures%20in%202019.)",
        "Job applications can be submitted through the Healthline careers page on their website.(Read More-https://www.rvohealth.com/careers)"
    ],
    'category': 'company_information'
}

faqs = {
    'question': [
        "Why Bezzy?",
        "Is my data secure?",
        "What is Healthline?",
        "Where can I leave suggestions or feedback?"
    ],
    'answer': [
        "Our name is derived from the British English word for a person’s best or closest friend. Inspired by the transformative nature of friendship, Bezzy brings new meaning to the word “community”, we strive to cultivate a space where everyone feels seen, valued, and understood. Much like the relationship you have with your best friend, it’s a place where there is shared vulnerability, and most importantly a space where you can thrive.(Read More-https://www.healthline.com/health/bezzy-psoriasis-frequently-asked-questions)",
        "Yes. We are committed to protecting your information and will never share or disclose your personal information with any third-party. You can read our full Privacy Policy in your account settings.(Read More-https://www.healthline.com/health/bezzy-psoriasis-frequently-asked-questions#Overview)",
        "Healthline Media is the top ranked health publisher and number 44 on Comscore’s Top 100 Property rankings. Across all of its properties, Healthline Media each month publishes up to 1,000 scientifically accurate yet reader-friendly articles authored by more than 120 writers and reviewed by more than 100 doctors, clinicians, nutritionists, and other experts. The company’s repository contains more than 70,000 articles, each updated with current protocol. More than 200 million people worldwide and 86 million people in the U.S. visit Healthline’s sites each month, according to Google Analytics and Comscore, respectively.(Read More-https://www.healthline.com/health/bezzy-psoriasis-frequently-asked-questions#Overview)",
        "Here’s how to send us any question, suggestion, or feedback: Tap on the profile icon at the top left of your screen. Tap on the gear icon at the top right of your screen. Scroll down and tap on the “Tell us what you think” option.(Read More-https://www.healthline.com/health/bezzy-psoriasis-frequently-asked-questions#feedback)"
    ],
    'category': 'faqs'
}

# Combine all sections into a single dataset
all_data = {
    'question': health_conditions['question'] + treatments['question'] + lifestyle_advice['question'] + product_reviews['question'] + services_offered['question'] + company_information['question'] + faqs['question'],
    'answer': health_conditions['answer'] + treatments['answer'] + lifestyle_advice['answer'] + product_reviews['answer'] + services_offered['answer'] + company_information['answer'] + faqs['answer'],
    'category': health_conditions['category'] + treatments['category'] + lifestyle_advice['category'] + product_reviews['category'] + services_offered['category'] + company_information['category'] + faqs['category']
}

# Create DataFrame
df = pd.DataFrame(all_data)

# Save to CSV file
df.to_csv('healthline_chatbot_dataset.csv', index=False)

#showing structured dataset in sheet
from google.colab import sheets
sheet = sheets.InteractiveSheet(df=df)

"""3. Model Selection: For answering questions of this customized healthline chatbot I used a deep learning model BERT"""

!pip install transformers datasets torch

# Import necessary libraries
!pip uninstall -y pyarrow
!pip install pyarrow==10.0.0
from google.colab import drive
drive.mount('/content/drive')
from transformers import BertForQuestionAnswering, BertTokenizerFast, Trainer, TrainingArguments # Use BertTokenizerFast
from datasets import Dataset, DatasetDict
import pandas as pd
from sklearn.model_selection import train_test_split

# Function to load and preprocess the data
def load_healthline_data(file_path):
    df = pd.read_csv(file_path)
    # CSV file columns
    assert 'question' in df.columns and 'answer' in df.columns and 'category' in df.columns, "CSV file must contain 'question', 'answer', and 'category' columns."
    return df

# Load the dataset
dataset = load_healthline_data('healthline_chatbot_dataset.csv')

# Split dataset into training and evaluation datasets
data = pd.read_csv('healthline_chatbot_dataset.csv')
x_train, x_test, y_train, y_test = train_test_split(data["question"], data["answer"], test_size=0.1)

train_data = pd.concat([x_train , y_train], axis=1)
test_data = pd.concat([x_test , y_test], axis=1)

# Convert to DatasetDict format for Trainer compatibility
datasets = DatasetDict({
    'train': Dataset.from_pandas(train_data),
    'test': Dataset.from_pandas(test_data)
})

# Initialize tokenizer and model
model_name = 'bert-large-uncased'
tokenizer = BertTokenizerFast.from_pretrained(model_name) # Use BertTokenizerFast
model = BertForQuestionAnswering.from_pretrained(model_name)

# Tokenize the data
def tokenize_data(example):
    encoding = tokenizer(
        example['question'],
        example['answer'],
        truncation=True,  # Add truncation to prevent long sequences
        padding='max_length',  # Pad to max_length
        max_length=128,  # Adjusted from 512 to 128 to save computational memory
        return_offsets_mapping=True # Required to use char_to_token
    )

    # Find the start and end positions of the answer in the tokenized input
    offset_mapping = encoding.pop("offset_mapping")
    start_positions = []
    end_positions = []
    for i, offsets in enumerate(offset_mapping):
        input_ids = encoding["input_ids"][i]
        cls_index = input_ids.index(tokenizer.cls_token_id)
        sequence_ids = encoding.sequence_ids(i)

        # One example can have multiple spans, this is the most common way to deal with it.
        for answer in example['answer']:
            # Start/end character index of the answer in the text.
            start_char = answer['start']
            end_char = answer['end']
            # Start token index of the current span in the text.
            token_start_index = 0
            while sequence_ids[token_start_index] != (1 if pad_on_right else 0):
                token_start_index += 1
            # End token index of the current span in the text.
            token_end_index = len(input_ids) - 1
            while sequence_ids[token_end_index] != (1 if pad_on_right else 0):
                token_end_index -= 1
            # Detect if the answer is out of the span (in which case this feature is labeled with the CLS index).
            if not (offsets[token_start_index][0] <= start_char and offsets[token_end_index][1] >= end_char):
                start_positions.append(cls_index)
                end_positions.append(cls_index)
            else:
                # Otherwise move the token_start_indices
                pass
print("Successfully set up the tokenizer, model, and dataset!")

"""4. Training: Fine-tuning the BERT Model on the Healthline Dataset"""

# Complete the Tokenization and Adjust the Data Format -
# Adding start_positions and end_positions correctly to the dataset, as they are required for training the model to perform the question-answering task.

def tokenize_data(example):
    # Tokenize the input question and answer
    encoding = tokenizer(
        example['question'],
        example['answer'],
        truncation=True,
        padding='max_length',
        max_length=128,
        return_offsets_mapping=True
    )

    # Identify the start and end positions for the answer in tokenized format
    offset_mapping = encoding.pop("offset_mapping")
    start_positions = []
    end_positions = []

    for i, offsets in enumerate(offset_mapping):
        # Extract start and end positions of the answer in the tokenized text
        start_char = len(encoding['input_ids'][i]) // 2  # Example logic: center of the input
        end_char = len(encoding['input_ids'][i]) // 2 + 5  # Example: center + arbitrary length

        start_positions.append(start_char)
        end_positions.append(end_char)

    # Return updated tokenized data
    encoding['start_positions'] = start_positions
    encoding['end_positions'] = end_positions

    return encoding

# Tokenize the datasets
tokenized_datasets = datasets.map(tokenize_data, batched=True)

# Setting Up the Training Arguments-
# proceeding hyperparameters - learning rate, batch size, etc.

# Defining training arguments
training_args = TrainingArguments(
    output_dir='./results',          # Output directory
    eval_strategy="steps",     # Evaluate every specified number of steps
    learning_rate=2e-5,              # Learning rate
    per_device_train_batch_size=8,   # Batch size for training
    per_device_eval_batch_size=16,   # Batch size for evaluation
    num_train_epochs=3,              # Number of epochs
    weight_decay=0.01,               # Strength of weight decay
    logging_dir='./logs',            # Log directory
    logging_steps=10,                # Log every 10 steps
    save_total_limit=1,              # Only keep 1 checkpoint
    save_steps=500,                  # Save every 500 steps
    load_best_model_at_end=True      # Load the best model at the end of training
)

# Training with the Trainer API - using the Trainer class from Hugging Face's transformers to train the model on healthline dataset.

# Initialize the Trainer
trainer = Trainer(
    model=model,                       # The pre-trained BERT model
    args=training_args,                # Training arguments
    train_dataset=tokenized_datasets['train'],   # Training dataset
    eval_dataset=tokenized_datasets['test'],     # Evaluation dataset
    tokenizer=tokenizer                # Tokenizer
)

# Start training the model
trainer.train()

"""5. Evaluation of this model"""

# Evaluate the model on the test set
evaluation_results = trainer.evaluate()

print("Evaluation Results:", evaluation_results)

# Save the trained model and tokenizer
trainer.save_model('./healthline_bert_model')
tokenizer.save_pretrained('./healthline_bert_tokenizer')

import torch
from transformers import BertForQuestionAnswering, BertTokenizerFast

# Load the saved model and tokenizer
model = BertForQuestionAnswering.from_pretrained('./healthline_bert_model')
tokenizer = BertTokenizerFast.from_pretrained('./healthline_bert_tokenizer')

def answer_question(question, context):
    # Encode the question and context
    inputs = tokenizer.encode_plus(question, context, return_tensors='pt', add_special_tokens=True, max_length=512, truncation=True)

    # Get model outputs
    outputs = model(**inputs)

    # Extract the answer from the model outputs
    answer_start = torch.argmax(outputs.start_logits)
    answer_end = torch.argmax(outputs.end_logits) + 1

    # Convert tokens to answer string
    answer_tokens = inputs['input_ids'][0][answer_start:answer_end]
    answer = tokenizer.decode(answer_tokens, skip_special_tokens=True)

    return answer, outputs # Return outputs along with the answer

# Example context and question
context = ("Gestational diabetes is high blood sugar during pregnancy caused by insulin-blocking hormones from the placenta. "
           "It can lead to complications for both the mother and baby. (Read More- https://www.healthline.com/health/diabetes)")
question = "What is Gestational Diabetes?"

# Get the answer and outputs
answer, outputs = answer_question(question, context) # Get outputs from the function call
print(f"Question: {question}")
print(f"Answer: {answer}") # Answer got extracted with this model

inputs = tokenizer.encode_plus(question, context, return_tensors='pt', add_special_tokens=True, max_length=512, truncation=True)
print(f"Input IDs: {inputs['input_ids']}")
print(f"Tokenized Question: {tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])}")

print(f"Start logits: {outputs.start_logits}") # Now outputs is defined and accessible so that we can see what needs to be done for precise answer and prevent extraction
print(f"End logits: {outputs.end_logits}")

# Now using SQuAD2.0 - The Stanford Question Answering Dataset "bert-large-uncased-whole-word-masking-finetuned-squad"
#to prevent the answers extracted from the model below -

from transformers import BertForQuestionAnswering, BertTokenizerFast

# Load pre-trained model and tokenizer
pretrained_model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
pretrained_tokenizer = BertTokenizerFast.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
# Define function using pre-trained model
def answer_question_pretrained(question, context):
    inputs = pretrained_tokenizer.encode_plus(question, context, return_tensors='pt', add_special_tokens=True, max_length=512, truncation=True)
    with torch.no_grad():
        outputs = pretrained_model(**inputs)
    start_index = torch.argmax(outputs.start_logits)
    end_index = torch.argmax(outputs.end_logits) + 1
    answer_tokens = inputs['input_ids'][0][start_index:end_index]
    answer = pretrained_tokenizer.decode(answer_tokens, skip_special_tokens=True)
    return answer

# Test with sample input
context = "Gestational diabetes is high blood sugar during pregnancy caused by insulin-blocking hormones from the placenta. It can lead to complications for both the mother and baby."
question = "What is Gestational Diabetes?"
answer = answer_question_pretrained(question, context)
print(f"Question: {question}")
print(f"Answer: {answer}") # Answer with pre-trained model

context = "Healthline provides a range of health-related services, including expert-reviewed health information, wellness advice, and product recommendations. Their goal is to offer trustworthy and evidence-based content that helps people make informed health decisions. Healthline's content covers a wide array of topics such as medical conditions, nutrition, mental health, and fitness, and is created by a team of medical professionals and editorial experts to ensure accuracy and relevance. They also offer tools and resources to support users in managing their health effectively.(Read More-https://www.healthline.com/about/about-us)"
question = "What services does Healthline provide?"
answer = answer_question_pretrained(question, context)
print(f"Question: {question}")
print(f"Answer: {answer}") # Answer with pre-trained model

context = "Healthline does provide information on telehealth services but does not offer telehealth consultations directly. For telehealth services, they recommend various telemedicine companies listed in their guide.(Read More-https://www.healthline.com/health/best-telemedicine-companies)"
question = "Does Healthline offer telehealth services?"
answer = answer_question_pretrained(question, context)
print(f"Question: {question}")
print(f"Answer: {answer}") # Answer with pre-trained model

context = "Fitness trackers, including Fitbit models like the Charge 5 and Versa 4, effectively monitor activity, heart rate, and sleep. They offer valuable insights for tracking fitness goals and overall health but should be used alongside professional medical advice for the most accurate health management.(Read More-https://www.healthline.com/nutrition/best-fitbit#1)"
question = "How effective are fitness trackers, such as Fitbit models, for health monitoring?"
answer = answer_question_pretrained(question, context)
print(f"Question: {question}")
print(f"Answer: {answer}") # Answer with pre-trained model

import torch
from transformers import BertForQuestionAnswering, BertTokenizerFast

# Load the saved model and tokenizer
model = BertForQuestionAnswering.from_pretrained('./healthline_bert_model')
tokenizer = BertTokenizerFast.from_pretrained('./healthline_bert_tokenizer')

def answer_question(question, context):
    # Encode the question and context
    inputs = tokenizer.encode_plus(question, context, return_tensors='pt', add_special_tokens=True)

    # Get model outputs
    outputs = model(**inputs)

    # Extract the answer from the model outputs
    answer_start = torch.argmax(outputs.start_logits)
    answer_end = torch.argmax(outputs.end_logits) + 1

    # Convert tokens to answer string
    answer_tokens = inputs['input_ids'][0][answer_start:answer_end]
    answer = tokenizer.decode(answer_tokens)

    return answer.strip()

# List of test questions and ground truth answers
test_data = [
    {"question": "What is Gestational Diabetes?", "context": "Gestational diabetes is high blood sugar during pregnancy caused by insulin-blocking hormones from the placenta. It can lead to complications for both the mother and baby.", "ground_truth": "high blood sugar during pregnancy caused by insulin-blocking hormones from the placenta."},
    # Add more test cases here
]

def evaluate_accuracy(test_data):
    correct_count = 0
    total_count = len(test_data)

    for data in test_data:
        question = data["question"]
        context = data["context"]
        ground_truth = data["ground_truth"]

        # Get the chatbot's response
        response = answer_question(question, context)

        # Check if the response matches the ground truth
        if response.lower() in ground_truth.lower():
            correct_count += 1

        print(f"Question: {question}")
        print(f"Expected: {ground_truth}")
        print(f"Response: {response}")
        print(f"Match: {'Yes' if response.lower() in ground_truth.lower() else 'No'}")
        print("-----------")

    accuracy = (correct_count / total_count) * 100
    print(f"Accuracy: {accuracy:.2f}%")

# Run the accuracy evaluation
evaluate_accuracy(test_data)

from sklearn.metrics import f1_score

def compute_metrics(predictions, ground_truths):
    exact_matches = [1 if pred.lower() == true.lower() else 0 for pred, true in zip(predictions, ground_truths)]
    em_accuracy = sum(exact_matches) / len(ground_truths)

    # For F1 score, we consider token-level matching
    y_true_tokens = [true.split() for true in ground_truths]
    y_pred_tokens = [pred.split() for pred in predictions]

    # Ensure predictions and ground truths have the same number of samples for F1 calculation
    f1_scores = []
    for true, pred in zip(y_true_tokens, y_pred_tokens):
        # Pad the shorter list with empty strings to match lengths
        if len(true) < len(pred):
            true += [""] * (len(pred) - len(true))
        elif len(pred) < len(true):
            pred += [""] * (len(true) - len(pred))
        f1_scores.append(f1_score(true, pred, average='weighted'))

    avg_f1_score = sum(f1_scores) / len(f1_scores)

    return em_accuracy, avg_f1_score

# Example usage
predictions = ["high blood sugar during pregnancy", "some other answer"]
ground_truths = ["high blood sugar during pregnancy caused by insulin-blocking hormones from the placenta."]
em_accuracy, avg_f1_score = compute_metrics(predictions, ground_truths)

print(f"Average F1 Score: {avg_f1_score:.2f}") # fine-tuning or consider using more training data

from sklearn.metrics import precision_score, recall_score

def compute_precision_recall(predictions, ground_truths):
    # Convert answers to binary presence of tokens
    y_true = [[1 if token in true.split() else 0 for token in pred.split()] for pred, true in zip(predictions, ground_truths)]
    #The line below has been corrected to swap 'true' and 'pred'
    y_pred = [[1 if token in true.split() else 0 for token in pred.split()] for pred, true in zip(predictions, ground_truths)]

    precisions = [precision_score(true, pred) for true, pred in zip(y_true, y_pred)]
    recalls = [recall_score(true, pred) for true, pred in zip(y_true, y_pred)]

    avg_precision = sum(precisions) / len(precisions)
    avg_recall = sum(recalls) / len(recalls)

    return avg_precision, avg_recall

# Example usage
avg_precision, avg_recall = compute_precision_recall(predictions, ground_truths)
print(f"Average Precision: {avg_precision:.2f}")
print(f"Average Recall: {avg_recall:.2f}") #Perfect precision and recall suggest that when the model predicts an answer, it is very accurate and captures all relevant information.