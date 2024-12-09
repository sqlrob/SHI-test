import os

# Get the configration for the ollama server from the environment
# reasonable local defaults if undefined
ollama_url =  os.environ.get('OPENLIBRARY_ML_OLLAMA_HOST','http://localhost:11434')
ollama_model = os.environ.get('OPENLIBRARY_ML_OLLAMA_MODEL','llama3:latest')

