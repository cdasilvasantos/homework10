# test_token_schema.py

import pytest
from app.schemas.token_schemas import Token, TokenData, RefreshTokenRequest

# Test cases for Token model
def test_token_model():
    access_token = "jhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    token_type = "bearer"
    token = Token(access_token=access_token, token_type=token_type)
    assert token.access_token == access_token
    assert token.token_type == token_type

def test_token_model_default_token_type():
    access_token = "jhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    token = Token(access_token=access_token)
    assert token.token_type == "bearer"

# Test cases for TokenData model
def test_token_data_model():
    username = "user@example.com"
    token_data = TokenData(username=username)
    assert token_data.username == username

def test_token_data_model_optional_username():
    token_data = TokenData()
    assert token_data.username is None

# Test cases for RefreshTokenRequest model
def test_refresh_token_request_model():
    refresh_token = "jhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    request = RefreshTokenRequest(refresh_token=refresh_token)
    assert request.refresh_token == refresh_token

# Run tests
if __name__ == "__main__":
    pytest.main()
