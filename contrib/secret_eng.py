# Python generator
import random

chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!?@#$%^&*()"
size = 50
secret_key = "".join(random.sample(chars, size))

chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!?@#$%_"
size = 20
password = "".join(random.sample(chars, size))

CONFIG_STRING = ("""
SECRET_KEY=
DEBUG=True
ALLOWED_HOSTS=127.0.0.1, *
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=localhost
EMAIL_PORT=25
EMAIL_USE_TLS=
EMAIL_USE_SSL=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=

# TypeDB mysql or psql
TYPE_DB=

#BANCO DE DADOS PLANETSCALE MySQL
PLANETSCALE_DB=
PLANETSCALE_DB_USERNAME=
PLANETSCALE_DB_PASSWORD=
PLANETSCALE_DB_HOST=
PLANET_DB_PORT=
PLANETSCALE_SSL_CERT_PATH=/etc/ssl/certs/ca-certificates.crt
# para vercel usar
# PLANETSCALE_SSL_CERT_PATH=/etc/pki/tls/certs/ca-bundle.crt

# BANCO DE DADOS POSTGRESSQL
DATABASE_URL=

# CLOUDNARY
CLOUD_NAME=
CLOUD_API_KEY=  
CLOUD_API_SECRET=
""").strip() % (secret_key, password)

# Writing our configuration file to '.env'
with open('.env', 'w') as configfile:
    configfile.write(CONFIG_STRING)

print('Success!')
print('Type: cat .env')