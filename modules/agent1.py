import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from transformers import AutoTokenizer, AutoModel
import torch

from dotenv import load_dotenv


tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

inputs = tokenizer("This is a sample sentence.", return_tensors="pt")
outputs = model(**inputs)
embedding = outputs.last_hidden_state
sentence_embedding = embedding.mean(dim=1)  # Pool over tokens
print("Sentence embedding shape:", sentence_embedding.shape)

