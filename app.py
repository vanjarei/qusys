from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Q-SYS Cloud</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f4f4f9;
                margin: 0;
                padding: 0;
            }
            header {
                background-color: #007bff;
                color: white;
                padding: 20px 0;
            }
            marquee {
                font-size: 18px;
                color: #444;
            }
            .content {
                margin: 20px auto;
                max-width: 800px;
                padding: 20px;
                background: #fff;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                border-radius: 8px;
            }
            footer {
                margin-top: 20px;
                background: #007bff;
                color: white;
                padding: 10px 0;
                font-size: 14px;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Welcome to Q-SYS Cloud</h1>
        </header>
        <marquee behavior="scroll" direction="left">
            Empowering Cloud-Managed AV Solutions for the Modern World!
        </marquee>
        <div class="content">
            <h2>About Us</h2>
            <p>Q-SYS delivers innovative audio, video, and control solutions to revolutionize collaboration and elevate your experiences.</p>
            <p>Explore integrations with Microsoft Teams, AI-powered automation, and scalable solutions for your enterprise needs.</p>
        </div>
        <footer>
            &copy; 2025 Q-SYS Cloud - All Rights Reserved.
        </footer>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
