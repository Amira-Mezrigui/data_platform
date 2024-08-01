FROM python:3.8-slim
WORKDIR /work/jupyter
RUN pip install --no-cache-dir notebook
EXPOSE 8888
# Lancer Jupyter Notebook lorsque le conteneur démarre
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--notebook-dir=/work/jupyter"]