import pytest
import os
import tempfile
from DAL import init_db, get_projects, insert_project

@pytest.fixture
def temp_db():
    """Create a temporary database for testing."""
    db_fd, db_path = tempfile.mkstemp()
    os.environ['DATABASE_PATH'] = db_path
    
    # Initialize the database
    init_db()
    
    yield db_path
    
    # Cleanup
    os.close(db_fd)
    os.unlink(db_path)

def test_init_db(temp_db):
    """Test that database initialization works."""
    # Database should be created and accessible
    projects = get_projects()
    assert isinstance(projects, list)

def test_get_projects_empty(temp_db):
    """Test getting projects from empty database."""
    projects = get_projects()
    assert projects == []

def test_insert_and_get_project(temp_db):
    """Test inserting and retrieving a project."""
    # Insert a test project
    insert_project("Test Project", "Test Description", "test.jpg")
    
    # Get all projects
    projects = get_projects()
    
    # Should have one project
    assert len(projects) == 1
    assert projects[0]['title'] == "Test Project"
    assert projects[0]['description'] == "Test Description"
    assert projects[0]['image_filename'] == "test.jpg"

def test_insert_multiple_projects(temp_db):
    """Test inserting multiple projects."""
    # Insert multiple projects
    insert_project("Project 1", "Description 1", "image1.jpg")
    insert_project("Project 2", "Description 2", "image2.jpg")
    insert_project("Project 3", "Description 3", "image3.jpg")
    
    # Get all projects
    projects = get_projects()
    
    # Should have three projects
    assert len(projects) == 3
    
    # Check that all projects are there
    titles = [project['title'] for project in projects]
    assert "Project 1" in titles
    assert "Project 2" in titles
    assert "Project 3" in titles
