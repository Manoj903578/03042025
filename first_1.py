from flask import Flask, render_template
# This is a simple Flask application that serves a landing page for an e-commerce website.
# The landing page includes a welcome message and buttons to navigate to the shop and contact pages. this is a simple example of how to create a landing page using Flask.
# Flask is a micro web framework for Python that allows you to build web applications quickly and easily.
app = Flask(__name__)

@app.route('/')
def landing_page():
  return '''
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-Commerce Landing Page</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f4f4f4;
      }
      header {
        background-color: #333;
        color: white;
        padding: 1rem 0;
        text-align: center;
      }
      .container {
        padding: 2rem;
        text-align: center;
      }
      .btn {
        display: inline-block;
        margin: 1rem;
        padding: 0.5rem 1rem;
        background-color: #007BFF;
        color: white;
        text-decoration: none;
        border-radius: 5px;
      }
      .btn:hover {
        background-color: #0056b3;
      }
    </style>
  </head>
  <body>
    <header>
      <h1>Welcome to Our E-Commerce Store</h1>
    </header>
    <div class="container">
      <h2>Find the best products at unbeatable prices!</h2>
      <a href="/shop" class="btn">Shop Now</a>
      <a href="/contact" class="btn">Contact Us</a>
    </div>
  </body>
  </html>
  '''

if __name__ == '__main__':
  app.run(debug=True)