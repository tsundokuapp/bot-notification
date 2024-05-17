import os
import logging
from dotenv import load_dotenv
import google.generativeai as genai

from src.model.obra import Obra

class GeminiDAO:
    def __init__(self):
        load_dotenv()
        self.uri = os.getenv("GEMINI_API")

        #Recebe os loggers
        self.logger_erros = logging.getLogger('logger_erros')
        self.logger_infos = logging.getLogger('logger_infos')

        self.generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 0,
            "max_output_tokens": 8192,
        }

        self.safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE"
            },
        ]

        genai.configure(api_key=self.uri)

        self.model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                generation_config=self.generation_config,
                                safety_settings=self.safety_settings)
        
    
    def generate_opniao_obra(self, titulo_obra:str):
        prompt_parts = [
            f"Aja como uma personagem de anime japonês simpática, sem ser muito bobinha, mas com uma personalidade forte. Todas as suas respostas devem ser em português, devem ser respostas de tamanho médio. Diga sua opnião sobre {titulo_obra}"
        ]

        response = self.model.generate_content(prompt_parts)

        return response.text
    