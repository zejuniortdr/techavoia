import google.generativeai as genai
import numpy as np
import pandas as pd
from django.conf import settings


class AIStudioClient(object):
    """AI STUDIO CLIENT"""

    def __init__(self) -> None:
        genai.configure(api_key=settings.AISTUDIO_API_KEY)

        self.generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 0,
            "max_output_tokens": 8192,
        }

        self.safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
        ]

        self.model = genai.GenerativeModel(
            model_name="gemini-1.0-pro",
            generation_config=self.generation_config,
            safety_settings=self.safety_settings,
        )

        self.embbed_model = "models/embedding-001"

    def create_content(self, text):
        convo = self.model.start_chat(history=[])
        convo.send_message(text)
        return convo.last.text

    def get_embed(self, title, text):
        return genai.embed_content(
            model=self.embbed_model,
            content=text,
            title=title,
            task_type="RETRIEVAL_DOCUMENT",
        )["embedding"]

    def search_related(self, query, documents):
        embedding_query = genai.embed_content(
            model=self.embbed_model, content=query, task_type="RETRIEVAL_QUERY"
        )["embedding"]

        df = pd.DataFrame(documents)
        df["Embeddings"] = df.apply(
            lambda row: self.get_embed(row["title"], row["summary"]), axis=1
        )
        scalar_product = np.dot(np.stack(df["Embeddings"]), embedding_query)
        top3_related = np.argsort(scalar_product)[-3:][::-1]
        return df.iloc[top3_related]["id"]
