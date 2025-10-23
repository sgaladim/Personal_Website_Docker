#!/usr/bin/env python3
"""
Simple script to run the Flask application
"""

from app import app

if __name__ == '__main__':
    print("Starting Personal Portfolio Website...")
    print("Open your browser to: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    app.run(debug=True, host='0.0.0.0', port=5000)
