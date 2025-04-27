import secrets
import string
import base64

def generate_random_string(length=32):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def generate_base64_key(length=32):
    return base64.b64encode(secrets.token_bytes(length)).decode('utf-8')

env_template = f'''############
# N8N Configuration
############
N8N_ENCRYPTION_KEY={generate_random_string(32)}
N8N_USER_MANAGEMENT_JWT_SECRET={generate_random_string(32)}

############
# Supabase Secrets
############
POSTGRES_PASSWORD={generate_random_string(16)}
JWT_SECRET={generate_base64_key(32)}
ANON_KEY={generate_base64_key(32)}
SERVICE_ROLE_KEY={generate_base64_key(32)}
DASHBOARD_USERNAME=admin
DASHBOARD_PASSWORD={generate_random_string(16)}
POOLER_TENANT_ID={generate_random_string(16)}

############
# Langfuse credentials
############
CLICKHOUSE_PASSWORD={generate_random_string(16)}
MINIO_ROOT_PASSWORD={generate_random_string(16)}
LANGFUSE_SALT={generate_random_string(32)}
NEXTAUTH_SECRET={generate_random_string(32)}
ENCRYPTION_KEY={generate_random_string(32)}

############
# Google Gemini API
############
GOOGLE_API_KEY=your-gemini-api-key
'''

with open('.env', 'w') as f:
    f.write(env_template)

print("Generated .env file with secure random values.")
print("Please update the GOOGLE_API_KEY with your actual Gemini API key.") 