
# this file is only for testing purpose
import firebase_admin
from firebase_admin import auth
import pyrebase
from firebase_admin import credentials
import os
firebaseConfig = {
  "apiKey": "AIzaSyCuZ_R09bCzZyRAu2twyPn4BU_Nf1dcZaI",
        "authDomain": "carpet-backend.firebaseapp.com",
        "projectId": "carpet-backend",
        "storageBucket": "carpet-backend.appspot.com",
        "messagingSenderId": "277283782041",
        "appId": "1:277283782041:web:743b398865973c4c242708",
        "measurementId": "G-REKX8ZKYTP",
        "databaseURL":""
}

firebase = pyrebase.initialize_app(firebaseConfig)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\nihal\\Desktop\\carpet_backend\\carpet_backend\\firebase_key.json"
# Initialize Firebase Admin SDK
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "carpet-backend",
    "private_key_id": "002787380be525fc08de8e3862207564412bb811",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC68NnarYMVL8TW\nP5rkOdS3S218mDbMk/ADtL75BTlLGg/+44vb5Calnc1o78pfeVPN0kV/8i0+LtI2\nIOmFl+xYqGFiCU0/+ZoVIv7BWi33VGVOJw2J0SpvtJapCzFUGy+aeht1r9smGvZ3\nfYFtPyuYDUM3A3sxKlccQYEb/y1XIXAoS57UF94sPC2jp7hBYhVll6K6p+mHbRDq\nepOKAiToybIqwuXSL4Hau7U6JMYRjqXPJW3EVKdJ/VDST1/eO8+qFAPcXDHR5kFK\nKoiUzhegBAkBKjzK+Fkpe9rFM4SB8HFbE0zCWfI6K9aGffrltzNcqxoNKZyGlinN\nQY6KE7dhAgMBAAECggEADx6/dCdAGLTYJh8XY1nFGX01khQKrKHTki0qnCAeyfMF\n868KZyLtOEyK6m+ore+1hkp5WhenrqWhVYT0dlx7HpGh7MjFUYUaABcoRVHKsXxH\nRFq2xtye4tGXtP0FhKC9STCSq4Jphou8Px5s2z32g/Igq2Cx9GBREuU+cNoDHA6h\n/Y9rSL6fKJqB5Nl3LuQFgxZ1MradN1oBXJoWPImDprSJlRvF5b6UJJrLn87SoGpL\nWxWpiYi+nRVokiplaak+odeRRIvtkCmTxTsL/gYHMtD39c8R+s0T/vDYcCcBdBxj\nTsaD2aISWaFJMTxzbCYeuicsHICzQa8HAahA5djLkQKBgQDyVsXMslDHcZkqj1wd\nU6+wdWnhGN5eQ+VoiGJdPHR1cQLpijQZd0SJI0HbtuURDULIee7/+LHinrCSoo8X\nHZuf8N0Gf78sFiHal3kAZ5hzM+VoxBR61Q5UGVwrGf63J0Rh2Rs6dhfkL3J/8Ctc\nsTH+8QZRoF/Oo4XfS4jyBYCj2QKBgQDFep7CuuCnU1yiWehI6xpqGbnbzLTdc5jQ\n+2jifjLYbG4ctsGg5pzJjDf56ecNeEGvdVojHy9Jojs3Z03YZChBcY84LfyzoKSK\nr+a0wvi1FF8cUcD5TQYHVPndba5bDu3Rdv2PGONQFnP+v9+rCOVRYmNRelUDqDPQ\noA/gvepiyQKBgGSsu7uQEJLqlHDj4aalT4WFIZlL1YVfu3wzvHlzVgY8DrOqoH47\n2BMIvKFkV8E/uxDB5xIb5Pp6ZmxkcAFwYWiOjaPXijnsb9/5sWEDqIejdZiSbNei\njzNM3cdiIzk/bN8hbHha+w3m0DBqO/lj+5sn0jIy59pWgJUFMj0pIAnxAoGAc0ZQ\nxnswCHyw5lR1M5uJn8XEqHmmWl7QJa2cXBoutAcXf8tu2+3COCSRyGCxbztznGh0\nZWwevmzlBEJZPqe4l/siDzlI+dIcOpjTo1DsvUdW/cD7VIuRqVYBRTBxRtZAHLXI\n7W8pweZZb6uxdLWMpyU3tKgkWC4nkPDeU+KIn4ECgYA+3NO5jhMGCB083EnRd/9j\n698GCAaIKr18jx9evWbj1ueW3y9sRWUSCykP9dKPXOMWoSM6UTj+Ag4WvqXF4HG7\nMM0b5vTkkjj3Zz7nx8QYMkiXBcG1E/CgDKyN3aXZOXRo5zdIzxAA3KqG0HTqVSyR\nCei39oK2YoclHVVjEJfr9A==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-c55ut@carpet-backend.iam.gserviceaccount.com",
    "client_id": "107685603975566237206",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-c55ut%40carpet-backend.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
  })
a=firebase_admin.initialize_app(cred)

def is_valid_uid(uid):
    try:
        user = auth.get_user(uid)
        print(user.__dict__)
        return True
    except Exception as e:
        print("Error checking UID validity:", e)
        return False

def get_firebase_token(uid):
    if not is_valid_uid(uid):
        print("Error: UID does not exist in Firebase Authentication.")
        return None

    try:
        # Generate Firebase custom token for the given UID
        custom_token = auth.create_custom_token(uid)
        token= firebase.auth().sign_in_with_email_and_password(
            email = "nihaljai2000@gmail.com",
            password = "Hyderbad@123"
        )
        print("******************************************************************")
        print(token['idToken'])
        print("*******************************************************************")
        return custom_token
    except Exception as e:
        print("Error generating custom token:", e)
        return None


# Example usage
uid = "7yc84Dv1iYaEnzrSg3DiS1K3WWi2"  # Replace with the UID of the user you created in Firebase
try:
    firebase_token = get_firebase_token(uid)
    if firebase_token:
        print("Firebase Token:", firebase_token)
except Exception as e:
    print(e)
