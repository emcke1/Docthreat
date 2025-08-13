import os
import certifi
os.environ["SSL_CERT_FILE"] = certifi.where()
print("SSL_CERT_FILE set to:", os.environ["SSL_CERT_FILE"])
