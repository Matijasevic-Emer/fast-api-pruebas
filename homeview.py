def homeview():
    MOCK = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>¡Bienvenido Humano!</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #CDC5B4;
                color: #85756E;
                margin: 0;
                padding: 0;
            }
            h1 {
                font-size: 3rem;
                margin-top: 50px;
                color: #6D3D14;
            }
            p {
                font-size: 1.2rem;
                margin: 20px 0;
                color: #85756E;
            }
            .paw-container {
                position: relative;
                width: 100%;
                height: 100vh;
                overflow: hidden;
            }
            .paw-print {
                position: absolute;
                width: 70px;
                height: 70px;
                background-color: #6D3D14;
                border-radius: 50%;
            }
            .paw-print::before,
            .paw-print::after {
                content: '';
                position: absolute;
                width: 40px;
                height: 40px;
                background-color: #85756E;
                border-radius: 50%;
            }
            .paw-print::before {
                top: -30px;
                left: 15px;
            }
            .paw-print::after {
                top: -10px;
                left: -30px;
            }
            .toe {
                position: absolute;
                width: 20px;
                height: 20px;
                background-color: #85756E;
                border-radius: 50%;
            }
            .toe.one {
                top: -40px;
                left: 10px;
            }
            .toe.two {
                top: -50px;
                left: 30px;
            }
            .toe.three {
                top: -40px;
                left: 50px;
            }
            .paw {
                position: absolute;
                animation: float 5s infinite;
            }
            @keyframes float {
                0% {
                    transform: translateY(0) rotate(0);
                }
                50% {
                    transform: translateY(-20px) rotate(15deg);
                }
                100% {
                    transform: translateY(0) rotate(0);
                }
            }
        </style>
    </head>
    <body>
        <h1>¡Bienvenido Humano!</h1>
        <p>Explora, aprende y disfruta con nuestra FastAPI 🐾</p>
        <div class="paw-container">
            <div class="paw" style="top: 10%; left: 30%;">
                <div class="paw-print"></div>
                <div class="toe one"></div>
                <div class="toe two"></div>
                <div class="toe three"></div>
            </div>
            <div class="paw" style="top: 40%; left: 70%;">
                <div class="paw-print"></div>
                <div class="toe one"></div>
                <div class="toe two"></div>
                <div class="toe three"></div>
            </div>
            <div class="paw" style="top: 60%; left: 20%;">
                <div class="paw-print"></div>
                <div class="toe one"></div>
                <div class="toe two"></div>
                <div class="toe three"></div>
            </div>
            <div class="paw" style="top: 80%; left: 50%;">
                <div class="paw-print"></div>
                <div class="toe one"></div>
                <div class="toe two"></div>
                <div class="toe three"></div>
            </div>
        </div>
    </body>
    </html>
    """
    return MOCK
