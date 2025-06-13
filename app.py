from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    table = None  # Initialize table as None
    if request.method == 'POST':
        try:
            # Get the number from the submitted form
            number = int(request.form.get('number'))
            
            # Generate the multiplication table (from 1 to 10)
            table = [f"{number} x {i} = {number * i}" for i in range(1, 11)]
            
        except (ValueError, TypeError):
            # Handle cases where the input is not a valid number
            pass
            
    # Render the HTML page, passing the table data to it
    return render_template('index.html', table=table)

if __name__ == '__main__':
    # Run the app in debug mode for development
    app.run(host="0.0.0.0", debug=True)