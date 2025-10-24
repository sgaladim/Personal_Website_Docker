import pytest
import os
import tempfile
from app import app, init_db

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    # Create a temporary database for testing
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    
    with app.test_client() as client:
        with app.app_context():
            init_db()
        yield client
    
    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def test_index_page(client):
    """Test that the index page loads successfully."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Personal' in response.data or b'Portfolio' in response.data

def test_about_page(client):
    """Test that the about page loads successfully."""
    response = client.get('/about')
    assert response.status_code == 200

def test_resume_page(client):
    """Test that the resume page loads successfully."""
    response = client.get('/resume')
    assert response.status_code == 200

def test_projects_page(client):
    """Test that the projects page loads successfully."""
    response = client.get('/projects')
    assert response.status_code == 200

def test_contact_page(client):
    """Test that the contact page loads successfully."""
    response = client.get('/contact')
    assert response.status_code == 200

def test_new_project_page(client):
    """Test that the new project page loads successfully."""
    response = client.get('/projects/new')
    assert response.status_code == 200

def test_create_project_post(client):
    """Test creating a new project via POST request."""
    response = client.post('/projects', data={
        'title': 'Test Project',
        'description': 'This is a test project',
        'image_filename': 'test.jpg'
    })
    assert response.status_code == 302  # Should redirect after successful creation

def test_create_project_validation(client):
    """Test that project creation validates required fields."""
    response = client.post('/projects', data={
        'title': '',
        'description': 'Missing title',
        'image_filename': 'test.jpg'
    })
    assert response.status_code == 200  # Should return form with error
    assert b'All fields are required' in response.data

def test_thankyou_page(client):
    """Test that the thankyou page loads successfully."""
    response = client.get('/thankyou')
    assert response.status_code == 200
